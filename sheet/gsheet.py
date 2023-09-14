from google.oauth2.service_account import Credentials
import gspread
import pandas as pd


def init():
    # google-api setup
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = Credentials.from_service_account_file(
        "sheet/gmail-api-81225-f2d876f6c9b6.json", scopes=scope)
    gs = gspread.authorize(creds)
    sheet = gs.open_by_url(
        'https://docs.google.com/spreadsheets/d/10YKEf2rSzc7REUuZWQjCqa_zTQkSrr6JSY61QViCSvo/edit#gid=912871586')
    worksheet = sheet.get_worksheet(2)
    return worksheet


def write_records(data: list):
    worksheet = init()
    # Columns: [MISSION_ID, LINE_ID, SHOP_ID, CONSUMPTION, TIMESTAMP]
    worksheet.append_row(data)


def get_logs(user_id):
    worksheet = init()
    logs = pd.DataFrame(worksheet.get_all_records())
    mission = logs[logs["LINE_ID"] == user_id]
    if mission.empty:
        return "任務尚未開始"
    else:
        return list(mission["SHOP_ID"])


get_logs("Ubde456327c21bd7d0aae2f9f37d873d")