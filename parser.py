import os
import imaplib
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def connect_to_gmail(creds):
    try:
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        # Login to Gmail using OAuth 2.0 credentials
        mail.authenticate('XOAUTH2', lambda x: creds.token)
        print("Connected to Gmail successfully!")
        mail.logout()
    except imaplib.IMAP4.error as e:
        print("Failed to connect to Gmail:", e)

def main():
    # Authenticate and get credentials
    creds = authenticate()
    # Connect to Gmail using obtained credentials
    connect_to_gmail(creds)

if __name__ == "__main__":
    main()