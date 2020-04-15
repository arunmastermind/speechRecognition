import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('speak now!!!!')
    audio = r3.listen(source)
    r2 = sr.Recognizer()
    # get = r3.recognize_google(audio)
    # print(get)

if 'a' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'www.google.com/'
    with sr.Microphone() as source:
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except:
            print('error!!!!')

