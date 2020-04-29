from board import *
from snake import *
from os import system
import time
import pygame

def main():
    pygame.init()
    pygame.display.set_mode((1, 1))
    pygame.key.set_repeat(100, 100)
    
    test=Board(height=25,width=44)
    s=Snake()
    
    test.generateFood()
    test.foodH=0
    test.foodW=11
    
    while(test.checkCollision(s)==False):
        test.drawSnake(s)
        test.drawFood()
        test.checkFood(s)
        s.move()
        print("Score: {}".format(s.length))
        test.printBoard()
        test.clearBoard()
        time.sleep(0.1)
        system("clear") 
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    s.changeDirection(Directions.TOP)
                if event.key == pygame.K_s:
                    s.changeDirection(Directions.BOTTOM)
                if event.key == pygame.K_d:
                    s.changeDirection(Directions.RIGHT)
                if event.key == pygame.K_a:
                    s.changeDirection(Directions.LEFT)
                if event.key == pygame.K_q:
                    return 0
main()
