# -*- coding: utf-8 -*-

"""
Pagerank is an algorithm used by google search to rank websites in thier
search engine results.PageRank was named after larry page.
The pagerank algorithm outputs a probability didtribution used to 
represent the likelihood that a person randomly clicking the on links will 
arrive at any particular page.
It is given by
PR(A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))
PR(A) is the PageRank of page A,
PR(Ti) is the PageRank of pages Ti which link to page A,
C(Ti) is the number of outbound links on page Ti and
d is a damping factor which can be set between 0 and 1.


"""
import numpy as np
from scipy.sparse import csc_matrix
from fractions import Fraction

def float_format(vector,decimal):
    return np.round((vector).astype(np.float),decimals=decimal)
G = np.matrix([[1,1,0],
               [1,0,1],
               [0,1,0]])
n=len(G)
print(n)
M=csc_matrix(G,dtype=np.float)
rsums = np.array(M.sum(1))[:,0]
ri,ci = M.nonzero()
M.data/rsums[ri]
dp=Fraction(1,n)
E=np.zeros((3,3))
E[:]=dp
beta=0.85
A=beta*M+((1-beta)*E)
r=np.matrix([dp,dp,dp])
r=np.transpose(r)
previous_r=r
for it in range(1,30):
    r=A*r
    if(previous_r==r).all():
        break
    previous_r=r
    print("Final:\n",float_format(r, 3))
