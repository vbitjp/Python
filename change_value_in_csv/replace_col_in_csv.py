import fileinput

# 書き出し用のファイルを開く
out_file = open("csv_data_manipulation_output.csv","w")

# 編集したいファイル（元ファイル）を開く
with fileinput.input('csv_data_manipulation.csv', inplace=True) as f:
    # for文で1行ずつ取得
    for line in f:
    # 改行コードをブランクに置換
        line = line.replace("\n","")
    # カンマ区切りでリストに変換する
        line = line.split(",")
    # 変換後のカンマ区切りの雛形を作り、変換処理した値を入れ込む
        row = "{},{},{},{},{}\n".format(
            line[0],
            line[1],
            line[3],
            line[2],
            line[4],
            )
    # 書き出し用のファイルに出力
        out_file.write(row)
# 書き出し用ファイルを閉じる
out_file.close()