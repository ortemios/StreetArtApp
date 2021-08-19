import speech_recognition as sr
import threading


class Recognizer:
    def __init__(self, callback):
        self.callback = callback

    def start(self):
        threading.Thread(target=self.loop).start()

    def loop(self):
        while True:
            self.tick()

    def tick(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Sound recorded....")
            text = r.recognize_google(audio, language='ru-RU')
            print("Google Speech Recognition thinks you said " + text)
            self.callback(text.split(' '))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
