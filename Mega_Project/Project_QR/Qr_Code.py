import qrcode

QR = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

data = "https://github.com/Mehul1940"
QR.add_data(data)
QR.make(fit=True)

img = QR.make_image(fill_color="black", back_color="white")
img.save("QR_Code.png")
