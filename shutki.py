import requests
from bs4 import BeautifulSoup

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jokes")
        self['background'] = '#d3db9e'
        self.iconphoto(False, ImageTk.PhotoImage(Image.open("icons/icon_smile.jpg")))
        self.geometry("550x450")
        self.put_frames()


    def put_frames(self):
        self.add_shtirliz_frame = ShtirlizFrame(self)
        self.add_programmers_frame = ProgrammersFrame(self)

    @staticmethod
    def insert_into_file(final_result):
        file = open("minutka_yumora.txt", "w+", encoding='utf-8')
        file.write(final_result)
        file.close()


class ShtirlizFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.shtirliz_jokes_btn = Button(height=3, bg="#9fe3c5", fg='#2b2a2a', text="Анекдоты про Штирлица",
                                         command=ShtirlizFrame.get_jokes_about_shtirliz).grid(
                                         row=0, column=0, sticky=NW, pady=5, padx=10)

    @staticmethod
    def get_jokes_about_shtirliz():

        for_editing = ' Минутка юмора \n \n'
        final_result = f'{for_editing}'

        for page_number in range(1, 23):
            url = f'https://anekdoty.ru/pro-shtirlica/page/{page_number}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='holder-body')

            for jokes in joke_body:
                joke = jokes.text
                final_result += joke.replace('\n', '')

                final_result += f'\n \n {for_editing}'
                print(joke)

        App.insert_into_file(final_result)

class ProgrammersFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.shtirliz_jokes_btn = Button(height=3, bg="#9fe3c5", fg='#2b2a2a', text="Анекдоты про программистов",
                                         command=ProgrammersFrame.get_jokes_about_programmers).grid(
                                         row=4, column=0, sticky=W, pady=5, padx=10)

    @staticmethod
    def get_jokes_about_programmers():

        for_editing = ' Минутка юмора \n \n'
        final_result = f'{for_editing}'

        for page_number in range(1, 13):
            url = f'https://anekdoty.ru/pro-programmistov/page/{page_number}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='holder-body')

            for jokes in joke_body:
                joke = jokes.text
                final_result += joke.replace('\n', '')
                final_result += f'\n \n {for_editing}'

                print(joke)
                # for future changes
                # list = root.grid_slaves()
                # for l in list:
                #     l.destroy()
        App.insert_into_file(final_result)


app = App()
app.mainloop()



