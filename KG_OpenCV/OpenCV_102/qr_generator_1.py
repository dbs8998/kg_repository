import qrcode  # pip install qrcode[pil]

qr_data = "1234"
qr_img = qrcode.make(qr_data)

qr_path = qr_data + '.png'
qr_img.save('./images/'+qr_path)
