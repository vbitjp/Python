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
    worksheet.add_rows(10)
    worksheet.insert_row([7,8], 4)
    print("the value of Cell A4:{num}".format(num = worksheet.cell(4, 1)))
    worksheet.delete_row(1)
    worksheet.clear()

if __name__ == '__main__':
    main()