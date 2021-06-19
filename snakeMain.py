
import pygame as p


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

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        
        drawGrid(screen)
        p.display.flip()


def drawGrid(screen):
    for i in range(10):
        for j in range(10):
            p.draw.rect(screen, "green", p.Rect((j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE)), width = 1)



if __name__ == "__main__":
    main()