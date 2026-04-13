import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from http.server import HTTPServer, BaseHTTPRequestHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello, I'm QBot! To launch me please go to the chat interface or to my profile menu, and click 'Open App'"
    )
    await update.message.reply_text("If this is confusing, use /help")

    poc_username = os.getenv("POC_USERNAME")
    poc_text = f" (POC: @{poc_username})" if poc_username else ""
    await update.message.reply_text(
        f"For event organisers who want to use QBot, please message NUSCC Tech Directorate{poc_text}"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm QBot.\n\n"
        "To launch me:\n"
        "1. Go to the chat interface or my profile menu\n"
        "2. Click 'Open App'\n"
        "3. Join a queue and get a unique nickname\n\n"
        "That's it! Have fun!"
    )
    await update.message.reply_text("Chat interface:")
    await update.message.reply_photo(photo=open("chat_interface.png", "rb"))
    await update.message.reply_text("Profile menu:")
    await update.message.reply_photo(photo=open("profile_menu.png", "rb"))
    await update.message.reply_text(
        "Once you join the queue, you will be identified by a unique nickname:"
    )
    await update.message.reply_photo(photo=open("nickname.png", "rb"))
    await update.message.reply_text("HAVE FUN!")

    poc_username = os.getenv("POC_USERNAME")
    poc_text = f" (POC: @{poc_username})" if poc_username else ""
    await update.message.reply_text(
        f"P.S. For event organisers who want to use QBot, please message NUSCC Tech Directorate{poc_text}"
    )


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


def run_health_server():
    server = HTTPServer(("0.0.0.0", 8080), HealthHandler)
    server.serve_forever()


def main():
    load_dotenv()
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    from threading import Thread

    Thread(target=run_health_server, daemon=True).start()

    application.run_polling()


if __name__ == "__main__":
    main()
