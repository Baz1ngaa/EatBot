import datetime
from datetime import date
import pytz
global timeInput
timeInput=0 
#timeInput=input()

tz_Vienna = pytz.timezone('Europe/Vienna')
currentime=datetime.datetime.now(tz_Vienna)
currentdate=date.today()
print("timeNow:", currentime.hour, ":",currentime.minute)
print(currentdate.weekday())
if(currentime.minute == int(timeInput)):
    print("yes")