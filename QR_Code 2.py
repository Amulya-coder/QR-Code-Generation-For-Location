# Open the Command Line and type (pip install qrcode[pil]) for importing the qrcode package
import qrcode

# Generating the qrcode for the given location
qr= qrcode.make('https://goo.gl/maps/KKwY3inokUSiJA2c6')

#save the qrcode in png file
qr.save('myQR.png')


