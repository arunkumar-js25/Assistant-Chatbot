#----------------------------------------------------------------------------------------#
#Standard Imports
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os
import random
import time

#Custom Imports
from Actions.LogGenerate import *
#----------------------------------------------------------------------------------------#

count = 0

def talk(speech): 
    # num to rename every audio file  
    # with different name to remove ambiguity 
    global count 
    count = str(random.randrange(1,1000)) + str(random.randrange(1,1000))

    #print("-->", speech) 
    logger.info("<Kiddo>: " + str(speech))
    toSpeak = gTTS(text = speech, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 

    try:
        file = "talk"+count+".mp3"
        toSpeak.save(file) 
    except:
        file = "talk"+count+str(random.randrange(1,1000))+".mp3"
        toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)
    os.remove(file) 
