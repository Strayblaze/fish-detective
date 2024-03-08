import imapclient
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

def connect_to_gmail(username, password):
    try:
        # OAuth2 authentication
        client = LegacyApplicationClient(client_id=None)
        oauth = OAuth2Session(client=client)
        oauth.fetch_token(token_url='https://accounts.google.com/o/oauth2/token',
                          username=username, password=password,
                          client_id=None, client_secret=None)
        
        # Connect to Gmail IMAP server
        with imapclient.IMAPClient('imap.gmail.com', ssl=True) as server:
            server.oauth2_login(username, oauth.token['access_token'])
            print("Connected to Gmail successfully!")
            # You can perform actions on the mailbox here
            # For example, you can list the available mailboxes
            print(server.list_folders())
    except Exception as e:
        print("Failed to connect to Gmail:", e)

def main():
    # Prompt the user to enter Gmail credentials
    gmail_username = input("Enter your Gmail username: ")
    gmail_password = input("Enter your Gmail password: ")

    # Connect to Gmail
    connect_to_gmail(gmail_username, gmail_password)

if __name__ == "__main__":
    main()
