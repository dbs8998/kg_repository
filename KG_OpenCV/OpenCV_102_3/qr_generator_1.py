import qrcode  # pip install qrcode[pil]

qr_data = "We_Great"
qr_img = qrcode.make(qr_data)

qr_path = qr_data + '.png'
qr_img.save('./images/'+qr_path)
