import qrcode

# Đường dẫn đến menu của bạn (URL của trang menu)
url = "http://127.0.0.1:5000"

# Tạo mã QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Tạo hình ảnh mã QR
img = qr.make_image(fill='black', back_color='white')

# Lưu mã QR vào file
img.save("restaurant_menu_qr.png")
