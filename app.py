from flask import Flask, render_template, request
import asyncio
from bot import send_telegram_message

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        order_details = request.form.get('order_details')
        total_amount = request.form.get('total_amount')
        customer_number = request.args.get('customer')  # Get customer number from the URL

        # Send Telegram notification
        message = f"Khách hàng số {customer_number} đã đặt hàng!\nChi tiết đơn hàng:\n{order_details}\nTổng tiền: {total_amount}đ"
        asyncio.create_task(send_telegram_message(message))  # Send message asynchronously

        return f'Khách hàng số {customer_number} đã đặt hàng. Chúng tôi sẽ liên hệ với bạn sớm.'

    # If GET request, render the order page with customer number
    customer_number = request.args.get('customer')  # Get customer number from URL
    return render_template('order_page.html', customer_number=customer_number)


if __name__ == '__main__':
    app.run(debug=True)
