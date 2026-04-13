import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from http.server import HTTPServer, BaseHTTPRequestHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello, I'm QB! To launch me please go to the chat interface or to my profile menu, and click 'Open App'"
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

    from threading import Thread

    Thread(target=run_health_server, daemon=True).start()

    application.run_polling()


if __name__ == "__main__":
    main()
