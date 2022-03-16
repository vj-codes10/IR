# -*- coding: utf-8 -*-
"""
Write a program to Compute Similarity between two text documents

The cosine similarity is the cosine of the angle between two vectors. 
Figure 1 shows three 3- dimensional vectors and the angles between each pair. 
In text analysis, each vector can represent a document. The greater the value of θ,
the less the value of cos θ, thus the less the similarity between two documents.
"""


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def cosine_similarity(x, y):
    
    # Ensure length of x and y are the same
    if len(x) != len(y) :
        return None
    
    # Compute the dot product between x and y
    dot_product = np.dot(x, y)
    
    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum(x**2)) 
    magnitude_y = np.sqrt(np.sum(y**2))
    
    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    return cosine_similarity
corpus = ['data science is one of the most important fields of science',
            'this is one of the best data science courses',
            'data scientists analyze data']

# Create a matrix to represent the corpus
X = CountVectorizer().fit_transform(corpus).toarray()

print(X)
cos_sim_1_2 = cosine_similarity(X[0, :], X[1, :])
cos_sim_1_3 = cosine_similarity(X[0, :], X[2, :])
cos_sim_2_3 = cosine_similarity(X[1, :], X[2, :])

print('Cosine Similarity between: ')
print('\tDocument 1 and Document 2: ', cos_sim_1_2)
print('\tDocument 1 and Document 3: ', cos_sim_1_3)
print('\tDocument 2 and Document 3: ', cos_sim_2_3)
