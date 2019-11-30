from timeit import default_timer as timer

def printBoard(board, w, h):
    for y in range(h):
        for x in range(w):
            print(f"{board[x + w * y]}\t", end='')
        print()


def isValid(board, w, h, pos):
    (x, y) = pos
    return x >= 0 and \
           x <  w and \
           y >= 0 and \
           y <  h and \
           board[x + w * y] == 0 \

def getMoves():
    return [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

def backtrack(board, w, h, x, y, move_c, show=True):
    if move_c == w * h:
        if show:
            printBoard(board, w, h)
        return True
    
    for (dx, dy) in getMoves():
        nx = x + dx;
        ny = y + dy;
        if not isValid(board, w, h, (nx, ny)):
            continue
        move_c += 1
        board[nx + w * ny] = move_c
        if backtrack(board, w, h, nx, ny, move_c, show):
            return True
        move_c-=1
        board[nx + w * ny] = 0

    return False

def findSolution(w, h, show=True):
    board = [0] * (w*h)
    board[0] = 1
    backtrack(board, w, h, 0, 0, 1, show)
    

def benchmark(w, h):
    ping = timer()
    findSolution(w, h, False)
    pong = timer()
    return pong - ping

def makeMeasurements():
    tests = [(3,4), (4,5), (5,5), (5,6), (6,6), (7,7), (8,8)]
    for (w,h) in tests:
        print(f"{w}x{h}: {benchmark(w,h)}")
