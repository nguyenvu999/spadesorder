from telegram import Bot
from telegram.error import TelegramError
import asyncio

# Khởi tạo bot với token của bạn
bot_token = "7766748543:AAHzFojHsNjKwqdGKWXO2uqumcQYjqDtofU"
chat_id = "-1002533580592"

# Hàm gửi thông báo Telegram (bất đồng bộ)
async def send_telegram_message(message):
    try:
        bot = Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)  # Gửi thông báo đến Telegram
        print("Đã gửi thông báo")
    except TelegramError as e:
        print(f"Không thể gửi thông báo: {e}")
