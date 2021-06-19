
import pygame as p
import snakeEngine 

HEIGHT = WIDTH = 640
SQ_SIZE = 64
MAX_FPS = 15

"""
Main driver. This will handle user input and updating graphics.
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(p.Color("black"))
    running = True
    gs = snakeEngine.SnakeGame()
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_DOWN:
                    gs.changeDirection((1,0))
                    gs.autoMove()
                if e.key == p.K_RIGHT:
                    gs.changeDirection((0,1))
                    gs.autoMove()

        drawGameState(screen, gs.board, gs.body)
        p.display.flip()

def drawGameState(screen, board, body):
    drawGrid(screen)
    drawBody(screen, board, body)

def drawGrid(screen):
    for i in range(10):
        for j in range(10):
            p.draw.rect(screen, "green", p.Rect((j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE)), width = 1)

def drawBody(screen, board, body):
    for row in range(10):
        for col in range(10):
            piece = board[row][col]
            if piece != '--':
                p.draw.rect(screen, "light green", p.Rect((col*(SQ_SIZE), row*(SQ_SIZE), SQ_SIZE, SQ_SIZE)))
    
if __name__ == "__main__":
    main()