import qrcode

qrImg = qrcode.make("Bastav Kakoty")
qrImg.save("bastavQr.png", "PNG")