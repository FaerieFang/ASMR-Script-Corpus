import nltk, re
import pprint
from nltk import word_tokenize
from nltk.collocations import *
from nltk.stem.wordnet import WordNetLemmatizer
with open('dialouge2.txt', 'r') as file:
     data = file.read().rstrip()
sentence = data
sentence = str.lower(sentence)
punc2= "'"
punc = '".!()[]*{}“”…’:;,'
for ele in sentence:
    if ele in punc:
        sentence = sentence.replace(ele, "")
for ele in sentence:
    if ele in punc2:
        sentence = sentence.replace(ele, "")
tokens = nltk.word_tokenize(sentence)
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(tokens)

finder.apply_freq_filter(3)

pprint.pprint(finder.nbest(trigram_measures.likelihood_ratio, 100))

lmtzr = WordNetLemmatizer()
lemmatized = [lmtzr.lemmatize(word) for word in tokens]
occurrence = {item: tokens.count(item) for item in tokens}
sortedTokens = sorted(occurrence.items(), key = lambda x: x[1], reverse = True)
pprint.pprint(sortedTokens[:50])


