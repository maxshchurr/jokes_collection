import requests
from bs4 import BeautifulSoup

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def insert_into_file(final_result):
    file = open("minutka_yumora.txt", "w+", encoding='utf-8')
    file.write(final_result)
    file.close()


class Shtirliz:

    @staticmethod
    def get_jokes_about_shtirliz():

        for_editing = ' Минутка юмора \n \n'
        final_result = f'{for_editing}'

        for page_number in range(1, 13):
            url = f'https://anekdoty.ru/pro-shtirlica/page/{page_number}/'
            page = requests.get(url)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            joke_body = soup.find_all('div', class_='holder-body')

            for jokes in joke_body:
                joke = jokes.text
                final_result += joke.replace('\n', '')

                final_result += f'\n \n {for_editing}'

        insert_into_file(final_result)


class Programmers:

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

        insert_into_file(final_result)


if __name__ == '__main__':
    root = Tk()
    root.title("JOKES")
    root.geometry("550x450")
    icon = ImageTk.PhotoImage(Image.open("icons/icon_smile.jpg"))

    # Create a Label Widget to display the text or Image
    root.iconphoto(False, icon)

    shtirliz = Shtirliz()
    shtirliz_jokes_btn = ttk.Button(text="Анекдоты про Штирлица",
                                    command=shtirliz.get_jokes_about_shtirliz).grid(
                                    row=0, column=0, sticky=NW, pady=5, padx=10)

    programmers = Programmers()
    programmers_jokes_btn = ttk.Button(text="Анекдоты про программистов",
                                       command=Programmers.get_jokes_about_programmers).grid(
                                       row=1, column=0, sticky=W, pady=5, padx=10)

    root.mainloop()


