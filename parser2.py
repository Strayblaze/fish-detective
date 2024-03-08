import imaplib

def connect_to_gmail(username, app_password):
    try:
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        # Login to Gmail using app password
        mail.login(username, app_password)
        print("Connected to Gmail successfully!")
        # You can perform actions on the mailbox here
        # For example, you can list the available mailboxes
        print(mail.list())
        mail.logout()
    except imaplib.IMAP4.error as e:
        print("Failed to connect to Gmail:", e)

def main():
    # Prompt the user to enter Gmail username and app password
    gmail_username = input("Enter your Gmail username: ")
    app_password = input("Enter your app password: ")

    # Connect to Gmail
    connect_to_gmail(gmail_username, app_password)

if __name__ == "__main__":
    main()