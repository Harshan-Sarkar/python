import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import cv2
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your personal virtual assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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



def webcam():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Webam")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Webcam", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()

result = True

if __name__ == "__main__":
    wishMe()
    while result:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search wikipedia' in query:
            speak('What should I search?')
            new_query = takeCommand()
            results = wikipedia.summary(new_query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Do you want to know more?")
            extra_query = takeCommand()
            if extra_query == 'yes':
                webbrowser.open(f'https://en.wikipedia.org/wiki/Special:Search?search={new_query}&go=Go&ns0=1')
            elif extra_query == 'no':
                speak('ok')
                print('ok')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'search youtube' in query:
            
            speak('What should I search?')
            new_query = takeCommand()
            webbrowser.open('https://www.youtube.com/results?search_query=' + new_query)


        elif 'search google' in query:
            speak('What should I search?')
            new_query = takeCommand()
            webbrowser.open('https://www.google.com/results?search_query=' + new_query)



        elif 'search stack overflow' in query:
            speak('What should I search?')
            new_query = takeCommand()
            webbrowser.open(f'https://stackoverflow.com/search?q={new_query}&s=dd288cba-0fad-43f0-b1a4-7f424d738378')


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'take a picture of mine' in query:
            speak("Opening webcam window")
            print("'esc' for exit")
            print("'spacebar' for photos")
            webcam()
        
        elif 'exit' in query:
            speak('It was a pleasure helping you.')
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Have a Good Day")

            elif hour>=12 and hour<18:
                speak("Have a Pleasent Evening")   

            else:
                speak("Sweet Dreams")
            result = False
        elif 'joke' in query:
            speak(pyjokes.get_joke())