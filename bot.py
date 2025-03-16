from telegram import Bot
from telegram.error import TelegramError
import asyncio

# Khởi tạo bot với token của bạn
bot_token = "7766748543:AAHzFojHsNjKwqdGKWXO2uqumcQYjqDtofU"
chat_id = "-1002533580592"

# Hàm gửi thông báo Telegram (bất đồng bộ)
async def send_telegram_message(order_details, total_amount):
    try:
        bot = Bot(token=bot_token)
        message = f"Có đơn hàng mới!\nChi tiết đơn hàng:\n{order_details}\nTổng tiền: {total_amount}.000đ"
        await bot.send_message(chat_id=chat_id, text=message)  # Gửi thông báo đến Telegram
        print("Đã gửi thông báo")
    except TelegramError as e:
        print(f"Không thể gửi thông báo: {e}")
