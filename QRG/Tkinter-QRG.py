from tkinter import *
import tkinter.ttk as ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from os import path
from tkinter import Menu

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

def clicked():
    res = "Welcome " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=1, row=0)

txt = Entry(window,width=10) #to make text field unedit - ,state='disabled'
txt.grid(column=0, row=1)

## ComboBox
combo = ttk.Combobox(window)              # ttk library
combo['values']= (1, 2, 3, 4, 5, "Text")  #we add the combobox items using the tuple.
combo.current(1)                          #set the selected item
combo.grid(column=0, row=2)
print(combo.get())
#To get the select item, you can use the get function like this: combo.get()

## CheckBox
chk_state = BooleanVar()
chk_state.set(True) #set check state
'''
we create a variable of type BooleanVar which is not a standard Python variable, 
it’s a Tkinter variable, and then we pass it to the Checkbutton class to set the check state

chk_state = IntVar()
chk_state.set(0) #uncheck
chk_state.set(1) #check
'''
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=3)
print(chk_state)


##RadioButton
selected = IntVar()

rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

def clicked():
   print(selected.get())

selected.set(2)
btn = Button(window, text="Click Me", command=clicked)
rad1.grid(column=0, row=5)
rad2.grid(column=1, row=5)
rad3.grid(column=2, row=5)
btn.grid(column=3, row=5)

#ScrolledText
txt2 = scrolledtext.ScrolledText(window,width=40,height=10)
txt2.grid(column=0,row=6)
txt2.insert(INSERT,'You text goes here') #Set scrolledtext content
txt2.delete(1.0,END)                     #Delete/Clear scrolledtext content

def messageBoxes():
    messagebox.showinfo('Message title', 'Message content')
    messagebox.showwarning('Message title', 'Message content')  # shows warning message
    messagebox.showerror('Message title', 'Message content')  # shows error message
    res = messagebox.askquestion('Message title', 'Message content')
    res = messagebox.askyesno('Message title', 'Message content')
    res = messagebox.askyesnocancel('Message title', 'Message content')
    res = messagebox.askokcancel('Message title', 'Message content')
    res = messagebox.askretrycancel('Message title', 'Message content')

btn2 = Button(window,text='Click here', command=messageBoxes)
btn2.grid(column=0, row=7)

##SPINBAR
var =IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable = var)
spin.grid(column=0,row=8 )

## ProgressBar
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 10
bar.grid(column=0, row=9)

## FILE OPEN DIALOG
def FileDialogs():
    file = filedialog.askopenfilename()
    file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    file = filedialog.askopenfilenames()
    dir = filedialog.askdirectory()  # TO select FOLDER

btn2 = Button(window,text='File Dialogs', command=FileDialogs)
btn2.grid(column=0, row=10)

## ADD MENU ITEM
menu = Menu(window)
#new_item = Menu(menu) #Dashed line at the beginning, well, if you click that line, it will show the menu items in a small separate window.
new_item = Menu(menu,tearoff=0) #You can disable this feature by disabling the tearoff feature
new_item.add_command(label='New' , command=clicked)
new_item.add_separator()
new_item.add_command(label='Edit' , command=clicked)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

## TABS
window2 = Tk()
tab_control = ttk.Notebook(window2)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
lbl1.grid(column=0, row=11)
lbl2 = Label(tab2, text= 'label2', padx=5, pady=5)
lbl2.grid(column=0, row=11)
tab_control.pack(expand=1, fill='both')
window2.mainloop()

window.mainloop()