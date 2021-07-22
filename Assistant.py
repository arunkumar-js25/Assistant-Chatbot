#----------------------------------------------------------------------------------------#
#Standard Imports
import os
from multiprocessing import Process,Value,Array
from _thread import start_new_thread

#Custom Imports
from Actions.Speech import *
from Actions.SpeechRecognition import *
from Actions.Feelings import *
from Settings import *
from Actions.LogGenerate import *
from SupportPkg.screenshot import *
#----------------------------------------------------------------------------------------#

#Variables  
        
#Configuration
rawconfigsetting('config.ini')
configsetting('config.ini')

#LoggerSetup
log2ConsoleConfig()
log2FileConfig()

#Main      
procs = []
BotInactive = True

if __name__ == "__main__":

    if(BotInactive):
        talk(config['mypy']['welcomemsg'])
        BotInactive = False

    while True:
        listen = str(input())#str(Listen()).lower()

        if(listen != 'sorry could not recognize your voice'):
            logger.info("<me>: "+listen)

        if(listen != None):
            CheckGreeting = startgreeting(listen)
            CheckEndGreeting = endgreeting(listen)
            if(CheckGreeting != None):
                talk(CheckGreeting)
                continue
            elif(CheckEndGreeting != None):
                talk(CheckEndGreeting)
                break
            elif(small_talk(listen)):
                proc = Process(target=process_text, args=(listen,))
                procs.append(proc)
                proc.start()