from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
import random

# Load token dari .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Fungsi command /start
def start(update, context):
    update.message.reply_text("✅ Bot nyala bro! 🚀")

# Fungsi command /checkweb
def checkweb(update, context):
    responses = [
        "Test 1: OK ✅",
        "Test 2: Running 🔄",
        "Test 3: Success 🎯",
        "Test 4: All good 👍",
        "Test 5: Random UAT 🌟"
    ]
    update.message.reply_text(random.choice(responses))

# Setup bot
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Daftarkan command
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("checkweb", checkweb))

# Jalankan bot
updater.start_polling()
updater.idle()
