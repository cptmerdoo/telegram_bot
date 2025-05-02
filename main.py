import asyncio
import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_message():
    await bot.send_message(chat_id=CHAT_ID, text="✅ Bu bir test mesajıdır.")

async def main():
    while True:
        await send_message()
        await asyncio.sleep(900)

if __name__ == "__main__":
    asyncio.run(main())
