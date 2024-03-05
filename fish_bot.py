from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Define your Telegram bot token
TOKEN: Final = '6514544505:AAHjFRB4GqLHVE---n5WelrfslFLNXWK53A'
BOT_USERNAME: Final = '@FishDetectiveBot'


# Define a command handler for the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Fish Detective. I can help you analyze your emails for suspicious content. Open the menu for more info.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To start analysing incoming messages from your mailbox, please use /connect command and enter your e-mail address. \nNote that, using this bot implies your consent to the usage of your personal data to scan for malicious content. The data will be encrypted and deleted as soon as it`s no longer needed.")

async def connect_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Note that, using this bot implies your consent to the usage of your personal data to scan for malicious content. The data will be encrypted and deleted as soon as it`s no longer needed. \nPlease, enter your valid e-mail address:")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('connect', connect_command))
    # Message handlers

    # Error handlers
    
    # Polling setup to check for new messages
    app.run_polling(poll_interval=10)