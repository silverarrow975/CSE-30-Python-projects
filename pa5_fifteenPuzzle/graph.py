# assignment: PA 5 - 15 Puzzle
# author: Harshita Bhardwaj
# date: 11/30/22
# file: This file sets up the graph ADT to be used in fifteen.py
# input: this file does not take any input alone, but can set up a graph ADT to be used in conjuction with other files
# output: there is no output to this file alone

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        pass

    def getVertex(self,n):
        pass

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        pass

    def getVertices(self):

        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s):
        pass

    def depth_first_search(self):
        pass

    def DFS(self, vid, path):
        pass