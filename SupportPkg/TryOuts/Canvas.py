import urllib.request

import tkinter as tk
from tkinterhtml import HtmlFrame

root = tk.Tk()

frame = HtmlFrame(root)#, horizontal_scrollbar="auto")
#frame.grid(sticky=tk.NSEW)

#frame.html(root)

#frame.set_content("<!DOCTYPE html>><html><body><h1>Hello world!</h1></body></html>")
#https://rive.app/a/fellowBeginner/files/flare/erza-scarlet/embed
frame.set_content(urllib.request.urlopen("https://rive.app/a/fellowBeginner/files/flare/erza-scarlet/embed"))
# print(frame.html.cget("zoom"))

root.mainloop()
