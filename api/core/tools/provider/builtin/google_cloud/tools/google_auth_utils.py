import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def authenticate_google_api(runtime_credentials):
    creds = None

    # Save the credentials JSON to a file
    creds_json_content = runtime_credentials.get('google_creds_json')
    with open("credentials.json", "w") as creds_file:
        creds_file.write(creds_json_content)

    # Load credentials from runtime credentials or token.json file
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run in token.json
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds