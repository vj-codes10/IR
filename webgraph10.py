import networkx as nx
import matplotlib.pyplot as plt
from xml.dom.minidom import parse
import xml.dom.minidom
# Open xml document using minidom parser
DOMTree=xml.dom.minidom.parse("movies.xml")
collection=DOMTree.documentElement
if collection.hasAttribute("shelf"):
print "Root element: %s" % collection.getAttribute("shelf")

# get all the movies in the collection
movies = collection.getElementsByTagName("movie")
#print detail of each movie.
for movie in movies:
print"*****Movie*****"
if movie.hasAttribute("title"):
print"Title: %s" %movie.getAttribute("title")

type = movie.getElementsByTagName('type')[0]
print "Type: %s" % type.childNodes[0].data
format= movie.getElementsByTagName('format')[0]
print "format: %s" % format.childNodes[0].data
rating= movie.getElementsByTagName('rating')[0]
print "Rating: %s" % rating.childNodes[0].data
description=movie.getElementsByTagName('description')[0]
print"description: %s" % description.childNodes[0].data

def GenerateGraph():
G=nx.Graph()

# adding just one node:
G.add_node("a")

# adding a list of edges:
G.add_edges_from([("a","b"),("b","c"), ("c","d"), ("d","a"),("a","c")])

nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

GenerateGraph()