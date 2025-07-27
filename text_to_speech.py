#this program uses win32com to convert text into speech 
#in this code we use a list of strings which store names
#and then convert these names into speech one by one
import win32com.client as win32
speaker = win32.Dispatch("SAPI.SpVoice")
list1 = ["Omkar","Niraj","Amit","Sonu","Harsh"]
for i in range(len(list1)):
    s = list1[i]
    speaker.Speak(s)
