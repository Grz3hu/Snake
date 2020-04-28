from enum import Enum

class Directions(Enum):
    TOP=(0,-1)
    BOTTOM=(0,1)
    LEFT=(-1,0)
    RIGHT=(1,0)
    NONE=(0,0)

class SnakeNode:
    w=0
    h=0

    def __init__(self,*,w,h):
       self.w=w 
       self.h=h 

    def __str__(self):
        return "dupa"
    
    def __repr__(self):
        return "{} {}".format(self.w, self.h)

class Snake:
    length=0
    nodes=[]
    direction=Directions.BOTTOM
    append=False

    def __init__(self):
       self.nodes.append(SnakeNode(w=1,h=1))
       length=1

    def getHead(self):
        return self.nodes[0]

    def changeDirection(self,direction):
        self.direction=direction

    def move(self):
        newNode=SnakeNode( w=self.nodes[0].w+self.direction.value[0], h=self.nodes[0].h+self.direction.value[1])
        if self.append==False:
            for n in reversed(range(1,len(self.nodes))):
                self.nodes[n]=self.nodes[n-1]
            self.nodes[0]=newNode
        else:
            self.length+=1
            self.nodes.insert(0,newNode)

        self.append=False
