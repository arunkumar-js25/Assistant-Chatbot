#----------------------------------------------------------------------------------------#
#Standard Imports
import os
import threading
import _thread
import time
from selenium import webdriver

#Custom Imports
from Actions.Speech import *
from Settings import *
#----------------------------------------------------------------------------------------#


def search_web(input): 
    #Configuration File
    #config = configparser.ConfigParser()
    #config.read('config.ini')

    driver = webdriver.Chrome(os.getcwd() + config['path']['driverpath']) 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
  
    if 'youtube' in input.lower(): 
  
        talk("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
  
    elif 'wikipedia' in input.lower(): 
  
        talk("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 

  
    else: 
  
        if 'google' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(input.split())) 

  
  
# function used to open application 
# present inside the system. 
def open_application(input): 
    try:
        for app in (config['app']['applist']).split('+'):
            if app.lower() in input:
                talk("Opening "+app+" app")
                os.startfile(config['app'][app]) 
    except: 
        talk("Application not available") 
