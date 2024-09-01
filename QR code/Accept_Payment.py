
import qrcode  # type: ignore
from PIL import Image  # type: ignore # Import the Image module from Pillow

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Defining the payment URLs based on the UPI ID and payment apps
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=123'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=123'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=123'

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url)

# Save the QR Code to image files (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

# Open and display the QR codes using Pillow's Image module
Image.open('phonepe_qr.png').show()
Image.open('paytm_qr.png').show()
Image.open('gpay_qr.png').show()
