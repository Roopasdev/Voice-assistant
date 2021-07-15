import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import subprocess

r = sr.Recognizer()
t = datetime.datetime.now()
engine = pyttsx3.init()

count = 0
while count <= 10:
    input('press enter')
    with sr.Microphone() as source:
        engine.say('hi how can i help you ')
        engine.runAndWait()
        audio = r.listen(source)
        voice_data = r.recognize_google(audio)
        print(voice_data)

        def responce():
            if voice_data == 'what is the time':
                engine.say("the time is")
                engine.runAndWait()
                engine.say(t.time())
                engine.runAndWait()

            if voice_data == 'open web browser':
                engine.say('ok opening web browser')
                engine.runAndWait()
                webbrowser.open('google.com') 

            if voice_data == 'what is the programming language you have been written':
                engine.say('i was written in a popular programming language called python')
                engine.runAndWait()  

            if voice_data == 'open file explorer':
                engine.say('ok opening file explorer')
                engine.runAndWait()
                subprocess.Popen('explorer')

            if voice_data == "search":
                # so here we are gonna make a the assistant to ask what do you wanna search

                engine.say("what do you want to search")
                engine.runAndWait()
                with sr.Microphone()as s:
                    au = r.listen(s)
                    vd = r.recognize_google(au)
                    engine.say("ok here is what i got")
                    engine.runAndWait()
                    webbrowser.open('https://www.google.com/search?q=' + vd)
                    input('Enter a key')





    responce()
    count += 1            
