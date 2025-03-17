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
    customer_number = request.args.get('customer')  # Lấy thông tin khách hàng từ URL

    # Gửi thông báo tới Telegram với thông tin khách hàng
    message = f"Khách hàng số {customer_number} đã đặt hàng!\nChi tiết đơn hàng:\n{order_details}\nTổng tiền: {total_amount}đ"
    asyncio.create_task(send_telegram_message(message))  # Gửi thông báo bất đồng bộ

    return f'Khách hàng số {customer_number} đã đặt hàng. Chúng tôi sẽ liên hệ với bạn sớm.'

if __name__ == '__main__':
    app.run(debug=True)
