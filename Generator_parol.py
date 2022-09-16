import tkinter as tk
import random as r


# функция генерации пароля из 8 символов
def password():
    par_list = []
    sym = list("QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCc"
               "VvBbNnMm[{]};:\'\",<.>/?1234567890!@#$%^&*()")
    for i in range(0, 8):
        par_list.append(r.choice(sym))
    label["text"] = "".join(par_list)


window = tk.Tk()
window.title("Генератор паролей")
window.rowconfigure(0, weight=30)
window.columnconfigure(0, weight=2)
label = tk.Label(width=30, height=2, relief=tk.SUNKEN, borderwidth=3, text="")
button = tk.Button(width=20, height=2, relief=tk.GROOVE,
                   borderwidth=3, text="Сгенерировать", command=password)

label.grid(row=0, column=0, sticky="nswe")
button.grid(row=1, column=0, sticky="nswe")
window.mainloop()
