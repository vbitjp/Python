# coding: utf-8
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def AddRow(argList):
    scope = ['https://spreadsheets.google.com/feeds']
    docId = os.environ['GOOGLE_GS_ID01']
    keyPath = os.path.expanduser(os.environ['GS_PUBKEY_PATH01'])

    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyPath, scope)
    client = gspread.authorize(credentials)
    gsheet = client.open_by_key(docId)
    worksheet = gsheet.sheet1
    #worksheet.add_rows(arg)
    #worksheet.insert_row(argList,3)
    worksheet.insert_row(argList,4)

def main():
	AddRow([7,8])

if __name__ == '__main__':
    main()