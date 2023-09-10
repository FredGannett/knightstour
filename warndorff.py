import sys
# Allow for much more recursion to avoid failures on 50*50 and 70*70
sys.setrecursionlimit(2000000)
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

def countMoves(board, w, h, x, y):
    count=0
    for (dx, dy) in getMoves():
        if isValid(board, w, h, (x+dx, y+dy)):
            count += 1
    return count

def getMovesHeuristic(board, w, h, x, y):
    """Note that to calculate the heuristic, we already need
       to find the new absolute position, so be might as well give
       that back instead of doing it again later."""
    choices = []
    # Determine all valid moves add annotate them
    # with the heuristic, i.e. the number of follow
    # up moves.
    for (dx, dy) in getMoves():
        nx = x + dx
        ny = y + dy
        if isValid(board, w, h, (nx, ny)):
            choices.append(((nx, ny), countMoves(board, w, h, nx, ny)))
    # sort the position by their heuristic
    choices.sort(key=lambda x: x[1])
    # strip the heuristic and then return
    # the result
    return [m for (m, _) in choices]

def getMoves():
    return [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

def backtrack(board, w, h, x, y, move_c, show=True):
    if move_c == w * h:
        if show:
            printBoard(board, w, h)
        return True
    
    for (nx, ny) in getMovesHeuristic(board, w, h, x, y):
        # No need to check the move, the heuristic
        # function has already done that for us.
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
    if not backtrack(board, w, h, 0, 0, 1, show):
        print("No solution")
    

def benchmark(w, h):
    ping = timer()
    findSolution(w, h, False)
    pong = timer()
    return pong - ping

def makeMeasurements():
    tests = [(3,4),(4,5), (5,5), (5,6), (6,6),
             (7,7), (8,8), (15,15), (50, 50), 
             (70, 70), (40, 100)]
    for (w,h) in tests:
        print(f"{w}x{h}: {benchmark(w,h)}")
