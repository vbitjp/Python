# IP Messenger宛てにテキストを送受信するのみ(ファイルの送受信なし)。iOSのPythonista3で実行する想定のコード
# 主な機能:
# - テキスト送受信
import socket
import threading
import time
import struct

# --- 定数定義 ---
# iPhoneのIPアドレス。空文字""で全てのNICから受信
BIND_IP = "192.168.111.2"
# IP Messengerの標準ポート
PORT = 2425
# ★ 送信先Windows PCのIPアドレスに書き換えてください
DEST_IP = "192.168.111.3"
DEST_PORT = 2425

# 自分の情報
USERNAME = "pythonista"
HOSTNAME = "iphone"

# --- IP Messenger コマンド定数 ---
# Ver1: 1
# (オプションは省略)
IPMSG_BR_ENTRY    = 0x00000001 # ネットワーク参加を通知
IPMSG_BR_EXIT     = 0x00000002 # ネットワーク離脱を通知
IPMSG_ANSENTRY    = 0x00000003 # 参加通知への応答
IPMSG_SENDMSG     = 0x00000020 # メッセージ送信
IPMSG_RECVMSG     = 0x00000021 # メッセージ受信通知 (開封確認)

# --- グローバル変数 ---
# ソケット共通
# ブロードキャストを有効にする
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((BIND_IP, PORT))


def build_packet(command, extra=""):
    """
    IP Messengerのパケットを組み立てる関数
    書式: "バージョン:パケット番号:送信者名:ホスト名:コマンド:追加情報"
    """
    packet_no = int(time.time())
    # コマンドは16進数ではなく、整数として文字列に変換する
    return f"1:{packet_no}:{USERNAME}:{HOSTNAME}:{int(command)}:{extra}"


def send_message(dest_ip, message):
    """指定したIPアドレスにメッセージを送信する"""
    packet = build_packet(IPMSG_SENDMSG, message)
    # IP MessengerはShift_JISを標準とすることが多いので、Shift_JISでエンコード
    # Pythonista3がShift_JISをサポートしているか確認が必要
    # サポートしていない場合は utf-8 のままでも良い
    try:
        encoded_packet = packet.encode("sjis")
    except UnicodeEncodeError:
        encoded_packet = packet.encode("utf-8", errors="ignore")
        
    sock.sendto(encoded_packet, (dest_ip, DEST_PORT))
    print(f"[送信] to {dest_ip}: {message}")


def send_broadcast_entry():
    """ネットワークに自分の存在を知らせる (ログイン通知)"""
    # BR_ENTRYの追加情報は、自分のユーザ名
    packet = build_packet(IPMSG_BR_ENTRY, USERNAME)
    try:
        encoded_packet = packet.encode("sjis")
    except UnicodeEncodeError:
        encoded_packet = packet.encode("utf-8", errors="ignore")

    # ネットワーク全体にブロードキャスト
    sock.sendto(encoded_packet, ("255.255.255.0", PORT))
    print("[INFO] ログイン通知(BR_ENTRY)をブロードキャストしました")


def receiver():
    """メッセージを受信し、コマンドに応じて応答するスレッド"""
    print("[INFO] 受信スレッドを開始しました")
    while True:
        try:
            data, addr = sock.recvfrom(4096)
            
            # 受信データをデコードしてみる (Shift_JIS -> UTF-8)
            try:
                text = data.decode("sjis")
            except UnicodeDecodeError:
                text = data.decode("utf-8", errors="ignore")

            # パケットを":"で分割して解析
            parts = text.split(':', 5)
            if len(parts) < 5:
                print(f"[受信エラー] 不正なパケット from {addr}: {text}")
                continue

            version, packet_no, sender, host, command_str, extra = parts
            command = int(command_str)
            
            sender_ip = addr[0]

            # --- 受信コマンドに応じた処理 ---

            if command & IPMSG_BR_ENTRY:
                # 他の誰かがログインした
                print(f"[INFO] {sender}@{host} ({sender_ip}) がログインしました")
                # 応答として自分の情報を送り返す (ANSENTRY)
                response_packet = build_packet(IPMSG_ANSENTRY, USERNAME)
                try:
                    encoded_response = response_packet.encode("sjis")
                except UnicodeEncodeError:
                    encoded_response = response_packet.encode("utf-8", errors="ignore")
                sock.sendto(encoded_response, addr)
                print(f"[応答] {sender} にANSENTRYを送信しました")

            elif command & IPMSG_ANSENTRY:
                # 誰かが自分のログインに応答してくれた
                print(f"[INFO] {sender}@{host} ({sender_ip}) をユーザーとして認識しました")

            elif command & IPMSG_SENDMSG:
                # メッセージを受信した
                message = extra.split('\0', 1)[0] # NULL文字以降は添付ファイル情報など
                print(f"\n[受信] from {sender}@{host}: {message}")
                print(">> ", end="", flush=True) # 入力プロンプトを再表示

                # 受信確認を相手に送り返す (RECVMSG)
                # 追加情報として、受信したパケットの番号を送る
                response_packet = build_packet(IPMSG_RECVMSG, packet_no)
                try:
                    encoded_response = response_packet.encode("sjis")
                except UnicodeEncodeError:
                    encoded_response = response_packet.encode("utf-8", errors="ignore")
                sock.sendto(encoded_response, addr)
                print(f"[応答] {sender} に受信確認(RECVMSG)を送信しました")

            elif command & IPMSG_BR_EXIT:
                # 他の誰かがログアウトした
                print(f"[INFO] {sender}@{host} ({sender_ip}) がログアウトしました")
                
            else:
                # その他のコマンド
                print(f"[受信] from {addr}: Command={hex(command)}, Body={text}")

        except Exception as e:
            print(f"[受信スレッドエラー]: {e}")


def main():
    # 受信スレッドをデーモンとして開始
    threading.Thread(target=receiver, daemon=True).start()

    # ネットワークに自分の存在を通知
    send_broadcast_entry()
    
    # 2秒ほど待って、ネットワーク上の他PCからの応答を受信する時間を与える
    time.sleep(2)

    print("-" * 30)
    print("IP Messenger 送受信を開始します。")
    print(f"メッセージは {DEST_IP} のPCに送信されます。")
    print("終了するには 'exit' または 'quit' と入力してください。")
    print("-" * 30)
    
    try:
        while True:
            msg = input(">> ")
            if msg.lower() in ("exit", "quit"):
                # 終了時にはログアウト通知をブロードキャストするのが望ましい
                packet = build_packet(IPMSG_BR_EXIT, USERNAME)
                try:
                    encoded_packet = packet.encode("sjis")
                except UnicodeEncodeError:
                    encoded_packet = packet.encode("utf-8", errors="ignore")
                sock.sendto(encoded_packet, ("255.255.255.0", PORT))
                print("[INFO] ログアウト通知を送信しました。")
                break
            send_message(DEST_IP, msg)
    except KeyboardInterrupt:
        print("\n終了します。")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
