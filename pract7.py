# -*- coding: utf-8 -*-
"""
Aim: Write program for pre-processing of Text document: stop word removal
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sent= "We are students of CKT college"
stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize(example_sent)
filtered_sentence=[w for w in word_tokens if not w in stop_words]
filtered_sentence=[]
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print(word_tokens)
print(filtered_sentence) 


