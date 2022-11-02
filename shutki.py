import requests
from bs4 import BeautifulSoup

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def insert_into_file(final_result):
    file = open("minutka_yumora.txt", "w+", encoding='utf-8')
    file.write(final_result)
    file.close()


def get_jokes_about_shtirliz():
    url = 'https://anekdoty.ru/pro-shtirlica/'
    page = requests.get(url)
    data = page.text

    for_editing = ' Минутка юмора \n \n'
    final_result = f'{for_editing}'

    soup = BeautifulSoup(data, 'html.parser')
    joke_body = soup.find_all('div', class_='holder-body')
    for jokes in joke_body:
        joke = jokes.text
        final_result += joke.replace('\n', '')

        final_result += f'\n \n {for_editing}'

    insert_into_file(final_result)


def get_jokes_about_programmers():
    url = 'https://anekdoty.ru/pro-programmistov/'

    page = requests.get(url)
    data = page.text

    for_editing = ' Минутка юмора \n \n'
    final_result = f'{for_editing}'

    soup = BeautifulSoup(data, 'html.parser')
    joke_body = soup.find_all('div', class_='holder-body')
    for jokes in joke_body:
        joke = jokes.text
        final_result += joke.replace('\n', '')

        final_result += f'\n \n {for_editing}'

    insert_into_file(final_result)


root = Tk()
root.title("JOKES")
root.geometry("550x450")
icon = ImageTk.PhotoImage(Image.open("icons/icon_smile.jpg"))

# Create a Label Widget to display the text or Image
root.iconphoto(False, icon)

shtirliz_jokes_btn = ttk.Button(text="Анекдоты про Штирлица", command=get_jokes_about_shtirliz)
shtirliz_jokes_btn.place(relx=0.1, rely=0.1, anchor='nw', relwidth=0.35, relheight=0.15)

programmers_jokes_btn = ttk.Button(text="Анекдоты про программистов", command=get_jokes_about_programmers)
programmers_jokes_btn.place(relx=0.1, rely=0.4, anchor='w', relwidth=0.35, relheight=0.15)


root.mainloop()


