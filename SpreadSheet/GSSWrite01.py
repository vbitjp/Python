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
    workbook = cl1.open("GAStest1") # ワークブック名を指定して開く
    # worksheet1 = workbook.add_worksheet(title="worksheetABC", rows="20", cols="20") # ワークシートを作成する
    '''
    既に存在するワークシート名を指定すると、以下のエラーが発生する
    gspread.exceptions.RequestError: (400, "400: b'シート名「worksheetABC」はすでに存在しています。別の名前を入力してください。'")
    '''
    # worksheet2 = workbook.add_worksheet(title="worksheetDEF", rows="20", cols="20") # ワークシートを作成する
    # cl1.del_worksheet(worksheet2) # ワークシートを削除する
    print(workbook.worksheets()) # 存在するワークシートのオブジェクト一覧をリストで返す [<Worksheet 'worksheetABC' id:yyyyyyy>, <Worksheet 'worksheetDEF' id:xxxxxxx>]
    worksheet = workbook.worksheet("newSpreadSheet01") # 指定したワークシートのオブジェクトを返す <Worksheet 'newSpreadSheet01' id:od6>
    print(worksheet)


if __name__ == '__main__':
    main()