import nltk
import pprint
from pprint import *
from nltk import *
from nltk import word_tokenize
import os
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

corpusdir = 'newcorpus/'
newcorpus = CategorizedPlaintextCorpusReader(corpusdir, r'newcorpus_.*\.txt',cat_pattern=r'newcorpus_(\w)\.txt')

searchwords =['babe', 'sweetie', 'neko', 'headpat', 'i-i', 'darling', 'good boy', 'good girl']

cfd = ConditionalFreqDist(
    (genre,word)
    for genre in ['M', 'F']
    for word in newcorpus.words(categories=genre)if word in searchwords)
#max(samples, default=0)
cfd.tabulate()
