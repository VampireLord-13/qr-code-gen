import qrcode as qr

img = qr.make("https://www.youtube.com/@vampire_lord_13")
img.save("qr.png")
