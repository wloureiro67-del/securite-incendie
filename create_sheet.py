import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds


def main():
    creds = get_credentials()
    service = build("sheets", "v4", credentials=creds)

    spreadsheet = service.spreadsheets().create(body={
        "properties": {"title": "Articles Sécurité Incendie"},
        "sheets": [{
            "properties": {"title": "Articles", "index": 0}
        }]
    }).execute()

    sheet_id = spreadsheet["spreadsheetId"]

    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range="Articles!A1:E1",
        valueInputOption="RAW",
        body={"values": [["titre", "slug", "statut", "date_publication", "url"]]}
    ).execute()

    service.spreadsheets().batchUpdate(
        spreadsheetId=sheet_id,
        body={"requests": [{
            "repeatCell": {
                "range": {"sheetId": 0, "startRowIndex": 0, "endRowIndex": 1},
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"bold": True},
                        "backgroundColor": {"red": 0.2, "green": 0.2, "blue": 0.2},
                        "foregroundColor": {"red": 1, "green": 1, "blue": 1}
                    }
                },
                "fields": "userEnteredFormat(textFormat,backgroundColor,foregroundColor)"
            }
        }, {
            "autoResizeDimensions": {
                "dimensions": {"sheetId": 0, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 5}
            }
        }]}
    ).execute()

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
    print(f"Spreadsheet créé : {url}")


if __name__ == "__main__":
    main()
