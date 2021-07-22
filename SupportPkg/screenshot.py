#----------------------------------------------------------------------------------------#
#Standard Imports
import os
from PIL import Image, ImageGrab
from tkinter import *
import configparser
from tkinter import filedialog

#Custom Imports
from Settings import *
#----------------------------------------------------------------------------------------#
snapcount = 0

def Snapshot1():
    global snapcount 
    snapcount += 1
    rawconfigsetting('config.ini')
    snapshot = ImageGrab.grab()

    try:
        save_path = filedialog.asksaveasfilename(defaultextension='.png')
        snapshot.save(save_path)
    except:
        save_path = os.getcwd() + rawconfig['path']['snapshotdefaultpath'] + rawconfig['path']['snapshotname']+str(snapcount)+".jpg"
        snapshot.save(save_path)

def Snapshot():
    global snapcount 
    snapcount += 1

    rawconfigsetting('config.ini')
    snapshot = ImageGrab.grab()
    #print(rawconfig.sections())
    save_path = os.getcwd() + str(rawconfig["path"]['snapshotdefaultpath']) + str(rawconfig['path']['snapshotname'])+ str(snapcount)+".jpg"   # snapshot_path + snapshot_name
    snapshot.save(save_path)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        text = Label(self, text="Screenshot Name: ")
        text.place(x=10,y=20)
        #text.pack()

        # create button, link it to clickExitButton()
        SaveButton = Button(self, text="Save", command=self.clickSaveButton)
        # place button at (0,0)
        SaveButton.place(x=80, y=80)

        SaveAsButton = Button(self, text="SaveAs", command=self.clickSaveAsButton)
        # place button at (0,0)
        SaveAsButton.place(x=80, y=120)

    def clickSaveButton(self):
        Snapshot()

    def clickSaveAsButton(self):
        Snapshot1()
        

def ScreenshotSaveOption():
    
    # initialize tkinter
    root = Tk()
    app = Window(root)

    # set window title
    root.wm_title("ScreenShot Save option")
    root.geometry("320x200")

    # show window
    root.mainloop()