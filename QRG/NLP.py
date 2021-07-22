import urllib.request
from bs4 import BeautifulSoup
import nltk
import matplotlib
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem import SnowballStemmer,PorterStemmer,WordNetLemmatizer
#nltk.download()

# taking html data from site
response = urllib.request.urlopen('http://php.net/')
html = response.read()
print (html)

#Parsing html tags into text using soup
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)
#print(text)
tokens = [t for t in text.split()]

#print (tokens)
#print (len(tokens))
#freq = nltk.FreqDist(tokens)
#for key,val in freq.items():
#    print (str(key) + ':' + str(val))
#freq.plot(20, cumulative=False)

#Remove duplicate words which extracted from the site/tokens
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
#for key,val in freq.items():
#    print (str(key) + ':' + str(val))
#freq.plot(20,cumulative=False)

#TOKENIZE
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))  #print(sent_tokenize(mytext,"french")) if we are using different languges
print(word_tokenize(mytext))

#WORDNET - WordNet is a database that is built for natural language processing. It includes groups of synonyms and a brief definition.
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())

# SYNONYMS
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

# ANTONYMS
antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)

#STEMMING
french_stemmer = SnowballStemmer('french') #SnowballStemmer can stem 13 languages besides the English language.
print(french_stemmer.stem("French word"))

stemmer = PorterStemmer()
print(stemmer.stem('increases'))

#LEMMATIZE  - Word lemmatizing is similar to stemming, but the difference is the result of lemmatizing is a real word.
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))
print(lemmatizer.lemmatize('longest', pos="v"))
print(lemmatizer.lemmatize('long', pos="n"))
print(lemmatizer.lemmatize('longest', pos="a"))
print(lemmatizer.lemmatize('longer', pos="r"))

'''
Stemming works on words without knowing its context, and that’s why stemming has lower accuracy and faster than lemmatization.
In my opinion, lemmatizing is better than stemming. Word lemmatizing returns a real word even if it’s not the same word, it could be a synonym, but at least it’s a real word.
Sometimes you don’t care about this level of accuracy and all you need is speed; in this case, stemming is better.
'''