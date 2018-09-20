import sys
import time

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from playsound import playsound

#
app =QApplication(sys.argv)


due = input ("Enter time for alert : (hh:mm) : ")


message = input("Enter the message for alert : ")

try:
	# split the time string to hours and seconds
	hours, mins= due.split(":")
	# convert hours and mins to integers and pass it to the Qtime function
	due=QTime(int(hours), int(mins))

	if not due.isValid():
		raise ValueError

except ValueError:
	message="The value entered is not valid"

# checks the time from due and checks it with the current time. if current time is less than the due time
# it helps to share resourses for cpu , instead of just allocating it to this program
while QTime.currentTime()<due:
	# in every 2o sec the program pauses to give resources to other tasks for the cpu
	time.sleep(40)


# use of html tags to make the message
label= QLabel("<font color = red size = 72<b>  "+ message + "</b> </font")
# creates the display window
label.setWindowFlags(Qt.SplashScreen)

label.show()

# sound should be in the same directory
playsound("king.mp3")

# the program runs for 60000 secs and then auomatically executes
QTimer.singleShot(60000, app.quit)


sys.exit(app.exec_())




