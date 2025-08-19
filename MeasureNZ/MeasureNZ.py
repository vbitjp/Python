# iPhoneのマイクで騒音レベルを測定する。iOSのPythonista3で実行する想定のコード
# 主な機能:
# - 騒音レベル測定

from objc_util import *
import time

# --- 必要な Objective-C クラスを用意 ---
AVAudioRecorder = ObjCClass('AVAudioRecorder')
NSURL = ObjCClass('NSURL')
NSDictionary = ObjCClass('NSDictionary')
NSNumber = ObjCClass('NSNumber')

# --- 録音保存先(ダミー: /dev/null に捨てる) ---
url = NSURL.fileURLWithPath_('/dev/null')

# --- 設定を NSDictionary で用意 ---
settings = {
    'AVFormatIDKey': NSNumber.numberWithInt_(1633772320),   # kAudioFormatMPEG4AAC
    'AVSampleRateKey': NSNumber.numberWithFloat_(44100.0),
    'AVNumberOfChannelsKey': NSNumber.numberWithInt_(1),
}
ns_settings = NSDictionary.dictionaryWithDictionary_(settings)

# --- AVAudioRecorder 初期化 ---
error_ptr = c_void_p()
recorder = AVAudioRecorder.alloc().initWithURL_settings_error_(url, ns_settings, error_ptr)

# --- メータリングを有効化 ---
recorder.setMeteringEnabled_(True)

# --- 録音開始 ---
recorder.record()

print("録音開始、音量を表示します (Ctrl+C で停止)")

try:
    while True:
        recorder.updateMeters()
        peak = recorder.peakPowerForChannel_(0)   # dB値 (負の値、小さいほど静か)
        avg = recorder.averagePowerForChannel_(0) # 平均dB値
        print(f"Peak: {peak:.2f} dB, Avg: {avg:.2f} dB")
        time.sleep(1)
except KeyboardInterrupt:
    print("停止します")
    recorder.stop()
