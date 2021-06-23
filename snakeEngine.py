import random
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
        self.direction = (0,0)
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
        self.gameState = True

    def autoMove(self):
        if self.gameState == True:
            snake = self.snake
            r, c = snake.currentSq[0] + self.direction[0], snake.currentSq[1] + self.direction[1]
            self.moveSnake(snake, (r,c))

    def changeDirection(self, direction):
        self.direction = direction

    def moveSnake(self, snake, current):
        openBody = self.getSnakeBody(self.body)
        if current in openBody:
            self.gameOver()
        else:
            if current[0] > 9 or current[0] < 0:
                return self.gameOver()
            if current[1] > 9 or current[1] < 0:
                return self.gameOver()
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
                self.randomFood()
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


    def getOpenBoard(self, board):
        openList = []
        for i in range(10):
            for r in range(10):
                if board[r][i] == '--':
                    openList.append((r,i))
        return openList
    
    def getSnakeBody(self, body):
        openBody = []
        for i in body:
            openBody.append((i.currentSq[0], i.currentSq[1]))
        return openBody

    def randomFood(self):
        openList = self.getOpenBoard(self.board)
        randomNum = random.randint(0,len(openList)-1)
        coord = openList[randomNum]
        self.board[coord[0]][coord[1]] = 'O'

    def gameOver(self):
        self.gameState = False

    def display(self):
        """Displays the board"""
        for space in self.board:
            print(space)

