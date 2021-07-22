from pywinauto import application
from subprocess import Popen
from pywinauto import Desktop

Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Calculator
dlg.wait('visible')

app = application.Application()
app.start('notepad.exe', timeout=10)
main = app.Notepad

#main = app.window(title='Untitled - Notepad')
#app.Start('notepad.exe')

# Connect to already running process:
# By PID
# # app = Application(backend="uia").connect(process=1234)
# # By path to executable
# # app = Application(backend="uia").connect(path=r"C:\Windows\System32\Notepad.exe")
# # By regular expression
# # app = Application(backend="uia").connect(title_re=".*Notepad*")

print(main.print_control_identifiers())
#Gives controls it can do - print(main.print_control_identifiers())
main.Edit.type_keys("Hello pywinauto!\n\t It’s a sample text^A",
                    with_spaces=True,
                   with_newlines=True,
                    pause=0.5,
                   with_tabs=True)

font_menu = main.menu_select('Format->Font...')
font_type = app.Font.ComboBox
font_type.select('Comic Sans MS')
font_style = app.Font.ComboBox2
font_style.select('Bold')
font_size = app.Font.ComboBox3
font_size.type_keys('18')
app.Font.OK.click()