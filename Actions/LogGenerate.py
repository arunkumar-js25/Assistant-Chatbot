#----------------------------------------------------------------------------------------#
#Standard Imports
import logging
import os

#Custom Imports
from Settings import *
#----------------------------------------------------------------------------------------#
#www.machinelearningplus.com/python/python-logging-guide/

#Log Level
#DEBUG    Value=10  Detailed information, for diagnosing problems.      
#INFO     Value=20  Confirm things are working as expected.             
#WARNING  Value=30  Something unexpected happened, or indicative of some problem. But the software is still working as expected.
#ERROR    Value=40  More serious problem, the software is not able to perform some function. 
#CRITICAL Value=50  A serious error, the program itself may be unable to continue running.
#----------------------------------------------------------------------------------------#

logger = logging.getLogger("Kiddo")

def log2ConsoleConfig():
    #%(asctime)s :: %(levelname)s :: Module %(module)s :: Line No %(lineno)s :: %(message)s
    logging.basicConfig(level=logging.INFO, format='%(message)s')

# WRITING LOG TO FILE #
def log2FileConfig():
        global logger

        # Gets or creates a logger
        #logger = logging.getLogger(config.get('logsetup','loggername'))  

        # set log level
        logger.setLevel(int(config['logsetup']['loglevel']))

        # define file handler and set formatter
        file_handler = logging.FileHandler(os.getcwd() + config['logsetup']['filename'])

        #logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        formatter    = logging.Formatter(rawconfig['logsetup']['logformat'])
        file_handler.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(file_handler)
