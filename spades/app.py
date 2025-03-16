from flask import Flask, render_template, request
import asyncio
from bot import send_telegram_message

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/order', methods=['POST'])
def order():
    order_details = request.form.get('order_details')
    total_amount = request.form.get('total_amount')

    # Send Telegram notification
    asyncio.run(send_telegram_message(order_details, total_amount))

    return 'Đơn hàng đã được gửi! Chúng tôi sẽ liên hệ với bạn sớm.'

if __name__ == '__main__':
    app.run(debug=True)
