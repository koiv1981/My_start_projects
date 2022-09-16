import tkinter as tk
import random as r
global a, window_1, entry


# Функция генерации пароля из a символов
def password():
    try:
        global a
        pas_list = []
        sym = list("QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCc"
                   "VvBbNnMm[{]};:<.>/?1234567890'!@#$,%^&*()")
        for i in range(0, a):
            pas_list.append(r.choice(sym))
            label["text"] = "".join(pas_list)
    except NameError:  # Если не выбирать длину пароля, то по умолчанию
        # будет 8 символов в пароле
        a = 8
        password()


# Функция создания окна с выбором длины пароля
def len_password():
    global a, window_1, entry
    window_1 = tk.Tk()
    lbl = tk.Label(window_1, width=25, height=2, relief=tk.SUNKEN,
                   borderwidth=3, text="Введите длину пароля: ")
    entry = tk.Entry(window_1, relief=tk.SUNKEN, borderwidth=3,
                     justify="center")
    button_ok = tk.Button(window_1, width=10, height=1, relief=tk.GROOVE,
                          borderwidth=4, text="ОК", command=close_window_1)

    lbl.grid(row=0, column=0, sticky="nswe")
    entry.grid(row=0, column=1, sticky="nswe")
    button_ok.grid(row=1, column=1, sticky="e")
    entry.focus()


# Функция считывает количество символов пароля и
# закрывает окно с выбором длины пароля
def close_window_1():
    global a, window_1, entry
    a = int(entry.get())
    window_1.destroy()


window = tk.Tk()
window.title("Генератор паролей")
window.rowconfigure(0, weight=30)
window.columnconfigure(0, weight=2)
mainmenu = tk.Menu(window)
window.config(menu=mainmenu)
label = tk.Label(width=30, height=2, relief=tk.SUNKEN, borderwidth=3, text="")
button = tk.Button(width=20, height=2, relief=tk.GROOVE,
                   borderwidth=3, text="Сгенерировать", command=password)

settingmenu = tk.Menu(mainmenu, tearoff=0)
settingmenu.add_command(label="Настроить длину пароля", command=len_password)
settingmenu.add_command(label="Выход", command=lambda: exit())
mainmenu.add_cascade(label="Настройки", menu=settingmenu)

label.grid(row=0, column=0, sticky="nswe")
button.grid(row=1, column=0, sticky="nswe")
window.mainloop()
