'''import pandas
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#path  = r'C:\Users\V S K HARSHAVARDHAN\Desktop\assem\jarvis'
csv_name=input()
ap = os.path.join(path,csv_name)

data = pandas.read_csv(ap)
speak(data.describe)
print(data.describe)
print(data)'''

dic = {1:'harry',2:'jerry'}
print(dic[1])