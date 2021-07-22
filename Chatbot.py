import nltk
import random
import string
import re, string, unicodedata
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import wikipedia as wk
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")
#nltk.download('punkt') 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

data = open('movie_lines.txt','r',errors = 'ignore')
raw = data.read()
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw)

def Normalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    #word tokenization
    word_token = nltk.word_tokenize(text.lower().translate(remove_punct_dict))
    
    #remove ascii
    new_words = []
    for word in word_token:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    
    #Remove tags
    rmv = []
    for w in new_words:
        text=re.sub("&lt;/?.*?&gt;","&lt;&gt;",w)
        rmv.append(text)
        
    #pos tagging and lemmatization
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    lmtzr = WordNetLemmatizer()
    return [lmtzr.lemmatize(token) for token in rmv]

welcome_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
welcome_response = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def welcome(user_response):
    for word in user_response.split():
        if word.lower() in welcome_input:
            return random.choice(welcome_response)


def generateResponse(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=Normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    #vals = cosine_similarity(tfidf[-1], tfidf)
    vals = linear_kernel(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0) or "tell me about" in user_response:
        print("Checking Wikipedia")
        if user_response:
            robo_response = wikipedia_data(user_response)
            return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

#wikipedia search
def wikipedia_data(input):
    reg_ex = re.search('tell me about (.*)', input)
    try:
        if reg_ex:
            topic = reg_ex.group(1)
            wiki = wk.summary(topic, sentences = 3)
            return wiki
    except Exception as e:
            print("No content has been found")


flag=True
print("My name is Chatterbot and I'm a chatbot. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response not in ['bye','shutdown','exit', 'quit']):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Chatterbot : You are welcome..")
        else:
            if(welcome(user_response)!=None):
                print("Chatterbot : "+welcome(user_response))
            else:
                print("Chatterbot : ",end="")
                print(generateResponse(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Chatterbot : Bye!!! ")