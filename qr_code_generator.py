# QR Code Generator
import qrcode
data = input("Enter text/URL: ")
qrcode.make(data).save("qrcode.png")
print("QR Code saved as qrcode.png")
