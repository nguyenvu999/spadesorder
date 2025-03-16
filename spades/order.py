from flask import Flask, render_template, request

app = Flask(__name__)

# Trang menu đơn giản
@app.route('/')
def menu():
    return render_template('menu.html')

# Nhận đơn hàng từ khách
@app.route('/order', methods=['POST'])
def order():
    order_details = request.form.get('order_details')
    # Gửi thông báo hoặc lưu đơn hàng vào cơ sở dữ liệu
    # Gửi thông báo cho quản lý qua app hoặc email
    send_order_notification(order_details)
    return 'Đơn hàng đã được gửi!'

def send_order_notification(order_details):
    # Logic để gửi thông báo qua ứng dụng hoặc email
    pass

if __name__ == '__main__':
    app.run(debug=True)
