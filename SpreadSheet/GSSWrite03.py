# coding: utf-8
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
docId = os.environ['GOOGLE_GS_ID01']
keyPath = os.path.expanduser(os.environ['GS_PUBKEY_PATH01'])

def getWorkSheet(argDocId, argKeyPath):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(argKeyPath, scope)
    client = gspread.authorize(credentials)
    gsheet = client.open_by_key(argDocId)
    return gsheet.sheet1

def main():
    worksheet = getWorkSheet(docId, keyPath)
    worksheet.append_row([2, 3, 4])
    worksheet.update_title("newSpreadSheet01") # シート名をnewSpreadSheet01に変更する
    worksheet.resize(10, 10) # 10行10列のセルに整える
    output = worksheet.export(format='csv') # b'7,8,,,,,,\r\n0.7180067625,'
    print(output)
    print(worksheet.row_values(6)) # 6行目のセル全ての値をリストで返す。空白は''で返す
    print(worksheet.col_values(1)) # A列全てのセルの値もリストで返す。空白は''で返す
    print(worksheet.range('A1:D7')) # [<Cell R1C1 '7'>, <Cell R1C2 '8'> 〜 <Cell R7C4 '0.5887971373'>]のように指定セル全ての値をRxCx付きで返す
    print(worksheet.get_all_values()) # 1列もしくは1行まるごと空白セルであるラインを除く全てのセル値をリストで返す
    worksheet.add_rows(10) # 10行セルを最終行に追加
    worksheet.add_cols(3) # 3列セルを最終列に追加
    worksheet.insert_row([7,8], 4) # 4行目のA列からB列に向かって順に値を入力
    print("the value of Cell A4:{num}".format(num = worksheet.cell(4, 1))) # A列4行目のセルの値を返す
    worksheet.delete_row(1) # 最終行から昇順に、入力した値の分だけ行を削除
    worksheet.update_cell(4, 4, 1234) # セルD4に1234を代入
    worksheet.update_acell('C5', 5678) # セルC5に1234を代入

    worksheet.clear() # 全セルの値を削除


if __name__ == '__main__':
    main()