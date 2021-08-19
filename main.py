from tkinter import *
from words_renderer import WordsRenderer
from recognizer import Recognizer
import win32api


width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

root = Tk()
root.attributes('-fullscreen', True)

c = Canvas(root, bg='black', bd=0, highlightthickness=0, relief='ridge')
c.pack(fill=BOTH, expand=True)

words_renderer = WordsRenderer(canvas=c)
recognizer = Recognizer(callback=words_renderer.render_words)
recognizer.start()

root.mainloop()

