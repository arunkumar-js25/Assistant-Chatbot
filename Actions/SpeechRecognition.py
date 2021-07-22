#----------------------------------------------------------------------------------------#
#Standard Imports
import speech_recognition as sr
import pyaudio

#Custom Imports
#----------------------------------------------------------------------------------------#

# define the audio file
def ReadAudio(Filename):
    audio_file = sr.AudioFile(Filename)
    with audio_file as source: 
       r.adjust_for_ambient_noise(source) 
       audio = r.record(source)
    result = r.recognize_google(audio)
    return result

# Understand user speech
def Listen():
    print("...")
    r1 = sr.Recognizer()
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        
        audio = r1.listen(source,phrase_time_limit = 10)# listen to the source , time_limit [5 secs]
        try:
            result = r1.recognize_google(audio)    # use recognizer to convert our audio into text part.
            #print("You said : {}".format(result))
            #WriteToFile('test.txt',result)
        except:
            result = "Sorry could not recognize your voice"
            #print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
        return result



#write content to File
def WriteToFile(Filename,Message):
    # exporting the result 
    with open(Filename,mode ='a') as file: 
       file.write("Recognized text: ") 
       file.write(Message) 
       file.write("\n") 


#MAIN
#while True:
#    print(Listen())