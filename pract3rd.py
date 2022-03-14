# -*- coding: utf-8 -*-

"""
 Implement Dynamic programming algorithm for computing the edit distance between strings s1 and s2.
 
The Levenshtein distance is a string metric for measuring difference between two sequences. Informally, 
the Levenshtein distance between two words is the minimum number of single
character edits (i.e. insertions, deletions or substitutions) required to change one 
word into the other. It is named after Vladimir Levenshtein, who considered this distance in 1965.
Levenshtein distance may also be referred to as edit distance, although it may also denote 
a larger family of distance metrics. It is closely related to pairwise string alignments

"""
import numpy as np 
def levenshelin(s1,s2):
    size_x=len(s1)+1
    size_y=len(s2)+1
    matrix=np.zeros((size_x,size_y))
    for x in range(size_x):
        matrix[x,0]=x
        for y in range(size_y):
            matrix[0,y]=y
            for x in range(1,size_x):
                for y in range(1,size_y):
                    if s1[x-1]==s2[y-1]:
                        matrix[x,y]=min(matrix[x-1,y]+1,matrix[x-1,y-1],matrix[x,y-1]+1) 
                    else:
                        matrix[x,y]=min(matrix[x-1,y]+1,matrix[x-1,y-1]+1,matrix[x,y-1]+1)
            print(matrix) 
            return(matrix[size_x-1,size_y-1])
s1="Anuja" 
s2="Anoja"
print( levenshelin(s1,s2))
