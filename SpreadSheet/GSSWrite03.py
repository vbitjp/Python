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
    # worksheet.add_rows(10) # セルを10行追加
    # worksheet.insert_row([7,8], 4) # 4行目のA列からB列に向かって順に値を入力
    # print("the value of Cell A4:{num}".format(num = worksheet.cell(4, 1))) # A列4行目のセルの値を返す
    # worksheet.delete_row(1) # 最終行から昇順に、入力した値の分だけ行を削除
    # worksheet.update_cell(4, 4, 1234) # セルD4に1234を代入
    # worksheet.update_acell('C4', 1234) # セルC4に1234を代入
    worksheet.update_acell('C', 1234) # C列全セルに1234を代入
    # worksheet.clear() # 全セルの値を削除


if __name__ == '__main__':
    main()