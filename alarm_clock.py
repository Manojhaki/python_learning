import sys
import time

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from playsound import playsound

app =QApplication(sys.argv)


due = input ("Enter time for alert : (hh:mm) : ")


message = input("Enter the message for alert : ")

try:
	hours, mins= due.split(":")
	due=QTime(int(hours), int(mins))

	if not due.isValid():
		raise ValueError

except ValueError:
	message="The value entered is not valid"

while QTime.currentTime()<due:
	time.sleep(40)

label= QLabel("<font color = red size = 72<b>  "+ message + "</b> </font")

label.setWindowFlags(Qt.SplashScreen)

label.show()
playsound("king.mp3")

QTimer.singleShot(60000, app.quit)


sys.exit(app.exec_())




