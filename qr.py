import qrcode

# Đường dẫn cơ bản đến menu
url_base = "https://spadesorder.onrender.com/order?customer="  # Cung cấp URL của trang order với tham số customer

# Tạo mã QR cho 9 khách hàng
for i in range(1, 10):  # Tạo mã QR cho khách từ 1 đến 9
    url = url_base + str(i)  # Thêm số thứ tự khách hàng vào URL
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
    img.save(f"customer_{i}_qr.png")
