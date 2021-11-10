import qrcode

qr = qrcode.QRCode(
    box_size = 12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    border = 6
)
qr.add_data('https://www.instagram.com/yoshikonome/')
qr.make()
img = qr.make_image(fill_color='black', back_color='green')
img.save('qrcode2.png')
