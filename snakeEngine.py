class SnakeObject: 

    def __init__(self, previousSq, currentSq):
        self.previousNode = None
        self.previousSq = previousSq
        self.currentSq = currentSq

    def __repr__(self):
        return str(self.currentSq)

class SnakeGame:

    def __init__ (self):
        self.snake = SnakeObject((0,-1), (0,0))
        self.direction = (0,1)
        self.board = [
                    [self.snake,'--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--'],
                    ['--','--','--', '--', '--', '--','--','--', '--', '--']
                    ]
        self.body = [self.snake]

    def autoMove(self):
        snake = self.snake
        r, c = snake.currentSq[0] + self.direction[0], snake.currentSq[1] + self.direction[1]
        self.moveSnake(snake, (r,c))

    def changeDirection(self, direction):
        self.direction = direction

    def moveSnake(self, snake, current):
        if current[0] < 0 or current[1] < 0:
            print( "Hit Outside Box" )
        else:
            if self.board[current[0]][current[1]] == 'O':
                if snake.previousNode is None:
                    snake.previousNode = SnakeObject(snake.previousSq, snake.currentSq)
                    snake.previousSq = snake.currentSq
                    snake.currentSq = current
                    self.body.append(snake.previousNode)
                else:
                    newSnake = SnakeObject(snake.currentSq, current)
                    newSnake.previousNode = snake
                    self.snake = newSnake
                    self.body.insert(0, newSnake)
                    # while snake.previousNode != None:
                    #     snakeNext = snake.previousNode
                    #     snakeNext.previousSq = snakeNext.currentSq 
                    #     snakeNext.currentSq = snake.currentSq
                        
                    #     snake.previousSq = snake.currentSq
                    #     snake = snake.previousNode
                    # self.snake.currentSq = current
                    # snake.previousNode = SnakeObject(None, snake.previousSq)
                    # self.body.append(snake.previousNode)
            else: # (new square is '--')
                snake.previousSq = snake.currentSq
                snake.currentSq = current
                temp = snake
                while temp.previousNode != None:
                    snakeNext = temp.previousNode
                    snakeNext.previousSq = snakeNext.currentSq
                    snakeNext.currentSq = temp.previousSq
                    temp = temp.previousNode
            for i in self.body:
                if i.previousNode == None:
                    self.board[i.currentSq[0]][i.currentSq[1]] = i
                    if i.previousSq != None:
                        self.board[i.previousSq[0]][i.previousSq[1]] = '--'
                else:
                    self.board[i.currentSq[0]][i.currentSq[1]] = i
                    self.board[i.previousSq[0]][i.previousSq[1]] = '--'

    def display(self):
        """Displays the board"""
        for space in self.board:
            print(space)



gs = SnakeGame()
gs.display()

gs.autoMove()
gs.display()
gs.autoMove()
gs.display()
gs.changeDirection((1,0))
gs.autoMove()
gs.display()
gs.changeDirection((-1,0))

gs.autoMove()
gs.display()
gs.autoMove()
gs.display()
gs.autoMove()
gs.display()
gs.autoMove()
gs.display()