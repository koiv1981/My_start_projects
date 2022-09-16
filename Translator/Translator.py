import tkinter as tk
import json as j


# функция перевод с английского на русский
def translate_eng_rus():
    a = tablo_1.get()
    tablo_2.delete(0, tk.END)
    b = a.lower().split(" ")
    for i in b:
        if i in d:
            tablo_2.insert(tk.END, d.get(i) + " ")
        else:
            tablo_2.insert(tk.END, "none")


# функция перевод с русского на английский
def translate_rus_eng():
    a = tablo_1.get()
    tablo_2.delete(0, tk.END)
    b = a.lower().split(" ")
    for i in b:
        if i in d_1:
            tablo_2.insert(tk.END, d_1.get(i) + " ")
        else:
            tablo_2.insert(tk.END, "none")


# функция очистки табло для перевода
def clear():
    tablo_1.delete(0, tk.END)
    tablo_2.delete(0, tk.END)


try:
    with open("dict.dct", "r") as f:  # открываем файл со словарем на чтение
        d = j.loads(f.read())  # преобразуем строку в словарь
    d_1 = dict(map(reversed, d.items()))  # меняем местами ключ и значение
    # в словаре/переворачиваем словарь

    window = tk.Tk()
    window.title("Переводчик")
    window.rowconfigure([0, 2], minsize=50, weight=2)
    window.columnconfigure(0, minsize=30, weight=2)

    tablo_1 = tk.Entry(relief=tk.SUNKEN, width=100, justify="right",
                       borderwidth=3, font="Arial 12")
    button_clear = tk.Button(text="Очистить", width=33, height=2,
                             font="Arial 12", command=clear)
    button_trans = tk.Button(text="Перевести Eng → Rus", width=33,
                             height=2, font="Arial 12",
                             command=translate_eng_rus)
    button_trans_1 = tk.Button(text="Перевести Rus → Eng", width=33,
                               height=2, font="Arial 12",
                               command=translate_rus_eng)
    tablo_2 = tk.Entry(relief=tk.SUNKEN, width=100, justify="right",
                       borderwidth=3, font="Arial 12")

    tablo_1.grid(row=0, column=0, columnspan=3, sticky="nsew")
    tablo_1.focus()
    button_clear.grid(row=1, column=0)
    button_trans.grid(row=1, column=1)
    button_trans_1.grid(row=1, column=2)
    tablo_2.grid(row=2, column=0, columnspan=3, sticky="nsew")

except FileNotFoundError:  # проверка на наличие в директории
    # программы файла со словарем
    window = tk.Tk()
    window.title("Ошибка!")
    label = tk.Label(text="Ошибка! Поместите файл dict.dct в "
                          "директорию программы!!!", fg="red", font="Arial 10")
    label.pack()

window.mainloop()
