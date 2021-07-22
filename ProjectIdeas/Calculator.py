from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


expression = ""


def input_number(number, equation):
    global expression
    # concatenation of string
    expression = expression + str(number)
    equation.set(expression)

def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("0")


def evaluate(equation,ans):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        ans.set(result)
        expression = result
    except:
        expression = ""


def main():
    # APPLICATION
    app = Tk()
    app.title("Calc")
    app.geometry('240x400')

    equation = StringVar()
    equation.set("Enter the expression")
    screen = Entry(app, justify=RIGHT, textvariable=equation,bg="white", relief=SUNKEN, cursor="tcross", xscrollcommand=BOTH)
    screen.place(bordermode=INSIDE, width=236, height=40, x=2, y=0)

    ans = StringVar()
    ans.set(" ")
    answer = Label(app ,textvariable=ans,relief=FLAT,fg="grey")
    answer.place(y=53,x=100, height = 40, width=200)

    KeyboardFrame = Frame(app)
    KeyboardFrame.place(x=2,y=110)

    Button(KeyboardFrame, text="1", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(1, equation)).grid(column=0, row=4)
    Button(KeyboardFrame, text="2", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(2, equation)).grid(column=1, row=4)
    Button(KeyboardFrame, text="3", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(3, equation)).grid(column=2, row=4)
    Button(KeyboardFrame, text="C", width=7, height=4, bg="black", fg='white', relief=RAISED,
           command=lambda: clear_input_field(equation)).grid(column=3, row=4)

    Button(KeyboardFrame, text="4", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(4, equation)).grid(column=0, row=5)
    Button(KeyboardFrame, text="5", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(5, equation)).grid(column=1, row=5)
    Button(KeyboardFrame, text="6", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(6, equation)).grid(column=2, row=5)
    Button(KeyboardFrame, text="*", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number("*", equation)).grid(column=3, row=5)

    Button(KeyboardFrame, text="7", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(7, equation)).grid(column=0, row=6)
    Button(KeyboardFrame, text="8", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(8, equation)).grid(column=1, row=6)
    Button(KeyboardFrame, text="9", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(9, equation)).grid(column=2, row=6)
    Button(KeyboardFrame, text="/", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number("/", equation)).grid(column=3, row=6)

    Button(KeyboardFrame, text="0", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number(0, equation)).grid(column=0, row=7)
    Button(KeyboardFrame, text="+", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number("+", equation)).grid(column=1, row=7)
    Button(KeyboardFrame, text="-", width=7, height=4, bg="magenta", relief=RAISED,
           command=lambda: input_number("-", equation)).grid(column=2, row=7)
    Button(KeyboardFrame, text="=", width=7, height=4, bg="green", fg="black" , relief=RAISED,
           command=lambda: evaluate(equation,ans)).grid(column=3, row=7)

    app.mainloop()