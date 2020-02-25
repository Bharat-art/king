# Install Library
# pip install pyqrcode

# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode


# String which represent the QR code
s = "www.google.com"

# Generate QR code
url = pyqrcode.create(s)

#Print the output
print("qr", url)

# Create and save the png file naming "myqr.png"
url.svg("myqr.svg", scale = 8)



