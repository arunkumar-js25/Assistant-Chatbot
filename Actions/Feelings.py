#----------------------------------------------------------------------------------------#
#Standard Imports
import random
import wolframalpha
import multiprocessing
from _thread import start_new_thread

#Custom Imports
from Actions.Speech import *
from Actions.SpeechRecognition import *
from Actions.Tasks import *
#from BotConfiguration.py import *
from SupportPkg.screenshot import *
#----------------------------------------------------------------------------------------#

#Greetings
def startgreeting(sentence):
    GREETING_INPUTS = ("hey boy","hey bot","hello", "hai", "hi", "greetings", "sup", "what's up","hey","hey kiddo",)
    GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me","yes Master! How can I help you"]

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

#EndGreetings
def endgreeting(sentence):
    GREETING_INPUTS = ("bye kiddo","bye bot","bye thank you", "catch you later bot","logout","bye",)
    GREETING_RESPONSES = ["Bye Master","Bye Master! see you later","Bye Master! Have a great day!"]

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

#small talk with bot
def small_talk(input):
    if "who are you" in input or "define yourself" in input: 
            configsetting('config.ini')
            talk(config['about']['define']) 
            return False
  
    elif "who made you" in input or "created you" in input: 
            configsetting('config.ini')
            talk(config['about']['creator']) 
            return False

    return True

#General Questions
def process_text(input): 
    try: 
        if 'search' in input or 'play' in input: 
            # a basic web crawler using selenium 
            search_web(input) 

        elif 'take' in input and ('screenshot' in input or 'snapshot' in input):
            ScreenshotSaveOption()

        elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            talk("The answer is " + answer) 
  
        elif 'open' in input and 'app' in input: 
              
            # another function to open  
            # different application availaible 
            open_application(input.lower())  
  
        #else: 
  
            #talk("I can search the web for you, Do you want to continue?") 
            #ans = Listen() 
            #print(ans)
            #if 'yes' in str(ans) or 'yeah' in str(ans): 
            #    search_web(input) 
            #else: 
            #    return
    except : 
  
        talk("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = Listen() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input) 