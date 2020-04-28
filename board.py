import random

class Board:
    height=0
    width=0
    board=[]
    foodW=0
    foodH=0

    def __init__(self,* ,height,width):
        self.board = [[" " for y in range(width)] for x in range(height)]
        self.height=height
        self.width=width

    def printBoard(self):
        print("-"*(self.width+1))

        for h in range(self.height):
            for w in range(self.width):
                if w==0 or w==self.width-1:
                    print("|",end="")
                else:
                    print(self.board[h][w],end="")
            print()

        print("-"*(self.width+1))

    def clearBoard(self):
        self.board = [[" " for y in range(self.width)] for x in range(self.height)]

    def generateFood(self):
        self.foodH=random.randint(0,self.height-1)
        self.foodW=random.randint(0,self.width-1)

        while self.board[self.foodH][self.foodW]!=" ":
            self.foodH=random.randint(0,self.height-1)
            self.foodW=random.randint(0,self.width-1)

    def drawFood(self):
        self.board[self.foodH][self.foodW]="x"

    def checkCollision(self,snake):
        head=snake.getHead()
        if head.w>=self.width-1 or head.w<=0 or head.h>=self.height or head.h<0:
            return True
        return False

    def drawSnake(self,snake):
        for s in snake.nodes:
            self.board[s.h][s.w]="O"

    def checkFood(self,snake):
        head=snake.getHead()
        if head.h==self.foodH and head.w==self.foodW:
            snake.append=True
            self.generateFood()
