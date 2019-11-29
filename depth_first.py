def printBoard(board, w, h):
    for y in range(h):
        for x in range(w):
            print(f"{board[x + w * y]}\t", end='')
        print()


def isValid(board, w, h, pos):
    (x, y) = pos
    return x >= 0 and x <  w and y >= 0 and y <  h and board[x + w * y] == 0

def getMoves():
    return [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]


def getSuccessors(board, w, h, pos, count):
    (px, py) = pos
    for (dx, dy) in getMoves():
        nx = px + dx
        ny = py + dy
        if isValid(board, w, h, (nx, ny)):
            new_board = board.copy()
            new_board[nx + w * ny] = count+1
            yield (new_board, (nx, ny), count+1)

def findSolution(w, h):
    init_board = [0] * (w*h)
    init_board[0] = 1
    stack = [(init_board, (0,0), 1)]
    while len(stack) > 0:
        (board, pos, count) = stack.pop()
        if count == w*h:
            printBoard(board, w, h)
            return
        for succ in getSuccessors(board, w, h, pos, count):
            stack.append(succ)
        
