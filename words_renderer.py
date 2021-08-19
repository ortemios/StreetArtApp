import tkinter as tk
import random
import pyglet
import os


class WordsRenderer:
    def __init__(self, canvas: tk.Canvas):
        self._canvas = canvas
        self._load_fonts_and_settings()

    def _load_fonts_and_settings(self):
        settings = {}
        with open('settings.txt', 'r') as file:
            for line in file.readlines():
                tokens = line.strip().split('=')
                key = tokens[0]
                value = tokens[1]
                settings[key] = value
        self._font_size_min = int(settings['font_size_min'])
        self._font_size_max = int(settings['font_size_max'])
        self._words_count_max = int(settings['words_count_max'])
        self._delay_milliseconds_max = int(settings['delay_milliseconds_max'])
        self._font_names = [token.strip() for token in settings['font_names'].split(',')]
        fonts_dir = os.path.join(os.path.dirname(__file__), 'fonts')
        for filename in os.listdir(fonts_dir):
            font_path = 'fonts/' + filename
            pyglet.font.add_file(font_path)

    def render_words(self, words):
        self._canvas.delete("all")
        for word in words:
            self._render_word(word)

    @staticmethod
    def rgb_to_hex(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def _render_word(self, word: str):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        text = word.capitalize()
        font_name = random.choice(self._font_names)
        font_size = random.randint(self._font_size_min, self._font_size_max)
        max_font_size = width/len(word)
        font_size = min(int(max_font_size), font_size)
        x = random.randint(0, width - font_size*len(word))
        y = random.randint(0, height - font_size)
        color = self.rgb_to_hex(
            random.randint(30, 255),
            random.randint(30, 255),
            random.randint(30, 255)
        )
        self._canvas.create_text(
            x,
            y,
            text=text,
            anchor=tk.NW,
            fill=color,
            font=(font_name, font_size),
        )
