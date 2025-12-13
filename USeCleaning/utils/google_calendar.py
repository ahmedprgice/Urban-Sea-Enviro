# utils/google_calendar.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials/google_calendar.json'
CALENDAR_ID = 'ahmedageibemail01@gmail.com'

def create_calendar_event(summary, description, start_datetime, end_datetime):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Asia/Kuala_Lumpur',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Asia/Kuala_Lumpur',
        },
    }

    created_event = service.events().insert(
        calendarId=CALENDAR_ID,
        body=event
    ).execute()

    return created_event
