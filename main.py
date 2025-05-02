import os
import time
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN", "BOT_TOKENİNİ_BURAYA_YAZ")
CHAT_ID = os.getenv("CHAT_ID", "CHAT_IDİNİ_BURAYA_YAZ")

bot = Bot(token=TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

def main():
    while True:
        send_message("✅ Bu bir test mesajıdır.")
        time.sleep(900)

if __name__ == "__main__":
    main()
