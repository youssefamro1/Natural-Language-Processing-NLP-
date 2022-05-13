import string 
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer

stopwords=nltk.corpus.stopwords.words('english')



dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
massage = dataset.iloc[:,0]


def remove_panc(text):
    text="".join([char for char in text if char not in string.punctuation])
    return text

def tokenize(text):
    token=re.split(" ",text)
    return token

def remove_stops(text):
    text=[word for word in x if word not in stopwords]
    return text


x=massage.apply(lambda x: remove_panc(x))
x=x.apply(lambda x: tokenize(x.lower()))
#y=x.apply(lambda c: remove_stops(c))

ps = PorterStemmer()
x = [ps.stem(word) for word in x if not word in set(stopwords.words('english'))]





















