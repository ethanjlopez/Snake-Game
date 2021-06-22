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
    MOVEEVENT, t = p.USEREVENT+1, 150
    gs.randomFood()    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                p.time.set_timer(MOVEEVENT, t)
                if e.key == p.K_r:
                    gs = snakeEngine.SnakeGame()
                    gs.randomFood()
                if e.key == p.K_DOWN:
                    if gs.direction != (-1,0):
                        gs.changeDirection((1,0))
                        gs.display()
                if e.key == p.K_RIGHT:
                    if gs.direction != (0,-1):
                        gs.changeDirection((0,1))
                        gs.display()
                if e.key == p.K_LEFT:
                    if gs.direction != (0,1):
                        gs.changeDirection((0,-1))
                        gs.display()
                if e.key == p.K_UP:
                    if gs.direction != (1,0):
                        gs.changeDirection((-1,0))
                        gs.display()
            elif e.type == MOVEEVENT:
                gs.autoMove()
        drawGameState(screen, gs.board, gs.body)
        p.display.flip()

def drawGameState(screen, board, body):
    drawGrid(screen, board)
    drawBody(screen, body)

def drawGrid(screen, board):
    global colors
    colors = [p.Color("#a7d470"), p.Color("#92cc4b")]
    
    for i in range(10):
        for j in range(10):
            color = colors[((i+j) % 2)]
            if board[i][j] == 'O':
                p.draw.rect(screen, 'white', p.Rect((j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE)))
            elif board[i][j] =='--':
                p.draw.rect(screen, color, p.Rect((j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE)))

def drawBody(screen, body):
    for piece in body:
        p.draw.rect(screen, "#476ac4", p.Rect((piece.currentSq[1]*(SQ_SIZE), piece.currentSq[0]*(SQ_SIZE), SQ_SIZE, SQ_SIZE)))
        if piece.previousNode is None:
            p.draw.rect(screen, colors[(piece.previousSq[1]+piece.previousSq[0]) % 2], p.Rect((piece.previousSq[1]*(SQ_SIZE), piece.previousSq[0]*(SQ_SIZE), SQ_SIZE, SQ_SIZE)))

if __name__ == "__main__":
    main()