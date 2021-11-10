import qrcode
img = qrcode.make('https://www.instagram.com/yoshikonome/')
type(img)
img.save('qrcode.png')
