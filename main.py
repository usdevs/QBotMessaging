import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Define the function that runs on /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm QB! To launch me please go to the chat interface or to my profile menu, and click 'Open App'")
    await update.message.reply_text("Chat interface:")
    await update.message.reply_photo(photo=open("chat_interface.png", "rb"))
    await update.message.reply_text("Profile menu:")
    await update.message.reply_photo(photo=open("profile_menu.png", "rb"))
    await update.message.reply_text("Once you join the queue, you will be identified by a unique nickname:")
    await update.message.reply_photo(photo=open("nickname.png", "rb"))
    await update.message.reply_text("HAVE FUN!")

def main():
    load_dotenv()
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    # Register the handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
