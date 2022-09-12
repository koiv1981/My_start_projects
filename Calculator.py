import tkinter as tk
import math as m
global a, b, z


def numb_plus():
    global a, z
    a = float(tablo.get())
    tablo.delete(0, tk.END)
    z = 1


def numb_minus():
    global a, z
    a = float(tablo.get())
    tablo.delete(0, tk.END)
    z = 2


def numb_umn():
    global a, z
    a = float(tablo.get())
    tablo.delete(0, tk.END)
    z = 3


def numb_razd():
    global a, z
    a = float(tablo.get())
    tablo.delete(0, tk.END)
    z = 4


def numb_step():
    global a, z
    a = float(tablo.get())
    tablo.delete(0, tk.END)
    z = 5


def numb_kor():
    global a
    a = float(tablo.get())
    tablo.delete(0, tk.END)
    tablo.insert(0, str(m.sqrt(a)))


def numb_ravno():
    global a, b, z
    b = float(tablo.get())
    tablo.delete(0, tk.END)
    if z == 1:
        tablo.insert(tk.END, a+b)
        a = a + b
    elif z == 2:
        tablo.insert(tk.END, a-b)
        a = a - b
    elif z == 3:
        try:
            tablo.insert(tk.END, a*b)
            a = a * b
        except OverflowError:
            tablo.insert(tk.END, "Ошибка! Слишком большой объем данных!!!")
    elif z == 4:
        tablo.insert(tk.END, a/b)
        a = a / b
    elif z == 5:
        try:
            tablo.insert(tk.END, a**b)
            a = a ** b
        except OverflowError:
            tablo.insert(tk.END, "Ошибка! Слишком большой объем данных!!!")


window = tk.Tk()
window.title("Калькулятор")
window.rowconfigure(0, minsize=40, weight=1)
window.columnconfigure(0, minsize=30, weight=1)

tablo = tk.Entry(width=40, relief=tk.SUNKEN, borderwidth=5,
                 justify="right", font="Arial 10")
tablo.grid(row=0, column=0, columnspan=5, sticky="we")
tablo.focus()

but0 = list("С√^")
but1 = list("123+-")
but2 = list("456*/")
but3 = list("7890=")

button_c = tk.Button(text=but0[0], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.delete(0, tk.END))
button_kor = tk.Button(text=but0[1], width=5, height=2, font="Arial 10",
                       command=numb_kor)
button_step = tk.Button(text=but0[2], width=5, height=2, font="Arial 10",
                        command=numb_step)
button_1 = tk.Button(text=but1[0], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "1"))
button_2 = tk.Button(text=but1[1], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "2"))
button_3 = tk.Button(text=but1[2], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "3"))
button_plus = tk.Button(text=but1[3], width=5, height=2, font="Arial 10",
                        command=numb_plus)
button_minus = tk.Button(text=but1[4], width=5, height=2, font="Arial 10",
                         command=numb_minus)
button_4 = tk.Button(text=but2[0], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "4"))
button_5 = tk.Button(text=but2[1], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "5"))
button_6 = tk.Button(text=but2[2], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "6"))
button_umn = tk.Button(text=but2[3], width=5, height=2, font="Arial 10",
                       command=numb_umn)
button_razd = tk.Button(text=but2[4], width=5, height=2, font="Arial 10",
                        command=numb_razd)
button_7 = tk.Button(text=but3[0], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "7"))
button_8 = tk.Button(text=but3[1], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "8"))
button_9 = tk.Button(text=but3[2], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "9"))
button_0 = tk.Button(text=but3[3], width=5, height=2, font="Arial 10",
                     command=lambda: tablo.insert(tk.END, "0"))
button_ravno = tk.Button(text=but3[4], width=5, height=2, font="Arial 10",
                         command=numb_ravno)

button_c.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
button_kor.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
button_step.grid(row=1, column=3, columnspan=4, padx=5, pady=5, sticky="ew")
button_1.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
button_2.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
button_3.grid(row=2, column=2, padx=5, pady=5, sticky="ew")
button_plus.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
button_minus.grid(row=2, column=4, padx=5, pady=5, sticky="ew")
button_4.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
button_5.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
button_6.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
button_umn.grid(row=3, column=3, padx=5, pady=5, sticky="ew")
button_razd.grid(row=3, column=4, padx=5, pady=5, sticky="ew")
button_7.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
button_8.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
button_9.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
button_0.grid(row=4, column=3, padx=5, pady=5, sticky="ew")
button_ravno.grid(row=4, column=4, padx=5, pady=5, sticky="ew")

window.mainloop()
