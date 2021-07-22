#----------------------------------------------------------------------------------------#
#Standard Imports
import configparser

#Custom Imports
#----------------------------------------------------------------------------------------#

rawconfig = configparser.RawConfigParser()
config = configparser.ConfigParser()

def rawconfigsetting(File):
    global rawconfig
    rawconfig.read(File)

def configsetting(File):
    global config
    config.read(File)

#An application which requires initial values to be loaded from a 
#   file should load the required file or files using readfp() before calling read() 
#   for any optional files:
#import configparser, os
#config = configparser.ConfigParser()
#config.readfp(open('defaults.cfg'))
#config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])