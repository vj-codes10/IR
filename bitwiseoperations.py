# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus=[
       'this is the first documnet.',
       'this document is second document.',
       'and this is third document.',
       'is this first document?'
       ]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus) 
print(X.toarray())
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
print(df)
anddata = df[(df['this']==1)&(df['first']==1)]
print(anddata.index.tolist())
ordata = df[(df['this']==1)|(df['first']==1)]
print(ordata.index.tolist())
notdata = df[(df['and']!=1)]
print(notdata.index.tolist())
