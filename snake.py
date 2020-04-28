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

#    def listenKeys(self):
#        keyboard.add_hotkey('w', self.changeDirection, args=(Directions.TOP))
#        keyboard.add_hotkey('s', self.changeDirection, args=(Directions.BOTTOM))
#        keyboard.add_hotkey('d', self.changeDirection, args=(Directions.RIGHT))
#        keyboard.add_hotkey('a', self.changeDirection, args=(Directions.LEFT))

    def move(self):
        newNode=SnakeNode( w=self.nodes[0].w+self.direction.value[0], h=self.nodes[0].h+self.direction.value[1])
        for n in range(1,self.length):
            self.nodes[n-1]=self.nodes[n]
        if self.append==False:
            self.nodes.pop() 
        self.append=False
        self.nodes.insert(0,newNode)
