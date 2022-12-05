# Install openCV using the command (pip install opencv-python)
import cv2

# Read the qrcode
img = cv2.imread("myQR.png")

# Show the qrcode
cv2.imshow("img", img)

# Using this until we pressed the key for infinite amount of time the image will show on
# on the screen
cv2.waitKey(0)

# Destroy the image 
cv2.destroyAllWindows()

# Open the qrcode scanner and scan the QR code