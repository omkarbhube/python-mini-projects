#this program gives the user aa reminder in a form of notification every hour
# this program only give the reminder one time. 
# Every hour reminder aspect is done via Microsoft's Task Scheduler
import time
from plyer import notification

def remind_to_drink():
    notification.notify(
        title="💧 Time to Drink Water!",
        message="Stay hydrated. Take a sip now! 🥤",
        timeout=10
    )

remind_to_drink()


  
