# coding: utf-8
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def GSSWrite(argList):
    scope = ['https://spreadsheets.google.com/feeds']
    docId = os.environ['GOOGLE_GS_ID01']
    keyPath = os.path.expanduser(os.environ['GS_PUBKEY_PATH01'])

    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyPath, scope)
    client = gspread.authorize(credentials)
    gsheet   = client.open_by_key(docId)
    worksheet  = gsheet.sheet1
    worksheet.append_row(argList)

def main():
	GSSWrite([1,2,3,4]) #デフォルトのシートであれば、1001行目のA,B,C,D列に1,2,3,4が追加されるはず

if __name__ == '__main__':
    main()