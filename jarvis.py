import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import pyjokes

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
newVoiceRate=150
engine.setProperty('rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning maam")

    elif hour >= 12 and hour< 18:
        speak("good afternoon maam")

    else:
        speak("good evening maam")

    speak("hello I am your Robo. How may i help you ?")
  

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query= r.recognize_google(audio,language='en=in')
        print(f"User said:{query}\n")    

    except Exception as e:
         print(e)   
         print("Say that again please...") 
         return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tapaswinitripathy044@gmail.com','jotumerahumdard')
    server.sendmail('tapaswinitripathy044@gmail.com',to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\TAPASWINI TRIPATHY\\Desktop\\video")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishMe()
    while True: 
   # if 1:
        query = takeCommand().lower()


        if "wikipedia" in query:
            speak('searching...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "who are you" in query:
            speak("Im your handsome robo jarvis.and im at your service")

        elif "who made you" in query:
            speak("The most beautiful girl in this world Do i need to say her name. okay its tapaswini tripathy")

        elif "my mom" in query:
            speak("yes. how is your health mom ?")

        elif " like" in query:
            speak("As much as memory you can feed me")

        elif "grandfather" in query:
            speak("Hello Anand chandra tripathy how are you?")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")     

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'search' in query:
            speak("what do you want me to search?")
            Chromepath="C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe" 
            search=takeCommand().lower()
            webbrowser.get(Chromepath).open_new_tab(search +".com")

            

        elif 'play music' in query:
            music_dir = 'C:\\Users\\TAPASWINI TRIPATHY\\Desktop\\video'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam, the time is {strTime}")

        elif 'open Studio' in query:
            codePath= "C:\\Users\\TAPASWINI TRIPATHY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("what should i say?")
                content= takeCommand()
                to = "tapaswinitripathy15@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry could not send the mail")
        elif "bye" in query:
            speak("okay bye")
            quit()

        elif "screenshot" in query:
            screenshot()
            speak("i took the screenshot")

        elif "joke" in query:
            jokes()

        elif "shut down" in query:
            os.system("shutdown /s /t 1")