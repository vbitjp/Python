# coding: utf-8
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getClientAuth():
    scope = ['https://spreadsheets.google.com/feeds']
    docId = os.environ['GOOGLE_GS_ID01']
    keyPath = os.path.expanduser(os.environ['GS_PUBKEY_PATH01'])

    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyPath, scope)
    client = gspread.authorize(credentials)
    return client

def main():
	cl1 = getClientAuth()
    worksheet = cl1.add_worksheet(title="worksheetABC", rows="20", cols="20") # ワークシートを作成する
    cl1.del_worksheet(worksheet) # ワークシートを削除する


if __name__ == '__main__':
    main()