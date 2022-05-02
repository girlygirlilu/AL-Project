import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
# import os
# import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It take microphone input form the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMPT('smpt.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic For exceuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summery(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open quora' in query:
            webbrowser.open("quora.com")

        # elif 'play music' in query:
            # music_dir = ''

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"Sir, The time is {strTime}")


        elif 'open code' in query:
            # codepath = "C:\\Users\\"
            os.start(codePath)

        elif email to harry in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")








