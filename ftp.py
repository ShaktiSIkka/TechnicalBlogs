from ftplib import FTP
import time
import getpass
import cv2

upload = str(getpass.getuser())

camera = cv2.VideoCapture(0)
return_value, image = camera.read()
path = r"LOCATION TO CREATE THE FILE"
cv2.imwrite(path, image)
time.sleep(1)
del(camera)


try:
	host = '10.0.0.1'
	user = 'USER WITH FTP RIGHTS'
	password = 'PASSWORD FOR FTP USER'
	file = open('LOCATION OF THE CREATED FILE', 'rb')

	with FTP(host) as ftp:
		ftp.login(user=user, passwd=password)
		print(ftp.getwelcome())
	
		ftp.storbinary('STOR ' + f'{upload}.png', file)
		print("UPLOADING...")
		
		ftp.quit()
except Exception as e:
	print(e)
