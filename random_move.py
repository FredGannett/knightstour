import random
import seaborn

def tryRandom() -> int:
    w=6
    h=6
    # Create an empty board
    board = [0] * (w * h)
    (px, py) = (0,0)
    move_count = 0
    while True:
        move_count += 1
        board[px + w * py] = move_count
        # Filter moves that do not exit the board and go to a non visited cell 
        validMoves = []
        for (dx, dy) in getMoves():
            nx = px + dx
            ny = py + dy
            if nx >= 0 and nx < w and ny >= 0 and ny < h and board[nx + w * ny] == 0:
                validMoves.append((nx, ny))

        # No more valid moves, stop
        if len(validMoves) == 0:
            return move_count

        # Do one of the possible moves at random
        (px, py) = random.choice(validMoves)

def getMoves():
    return [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]


def savePlot():
    data = [tryRandom() for _  in range(1000)]
    plot = seaborn.distplot(data)
    plot.get_figure().savefig("random_move.png")

            
