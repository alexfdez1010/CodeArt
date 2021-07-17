import drawBot as draw
from numpy import array, count_nonzero, zeros, pad

BORN: list = [3]
LIVE: list = [2, 3]
BOARD_SIZE = 1000
FRAME_DURATION = 0.025


def count_adjacent(board: array, pos: tuple) -> int:
    n = board.shape[0]
    x_1 = max(0, pos[0] - 1)
    x_2 = min(n - 1, pos[0] + 1)
    y_1 = max(0, pos[1] - 1)
    y_2 = min(n - 1, pos[1] + 1)

    return count_nonzero(board[x_1:x_2 + 1, y_1:y_2 + 1])


def update_board(board: array) -> array:
    n = board.shape[0]
    new_board = zeros(shape=(n, n))

    for i in range(n):
        for j in range(n):
            count_adj = count_adjacent(board, (i, j))
            if board[i, j] == 0 and count_adj in BORN:
                new_board[i, j] = 1
            elif board[i, j] == 1 and count_adj - 1 in LIVE:
                new_board[i, j] = 1

    return new_board


def draw_board(board: array) -> array:
    n = board.shape[0]
    square_size = BOARD_SIZE / n
    draw.newPage(BOARD_SIZE, BOARD_SIZE)
    draw.frameDuration(FRAME_DURATION)
    for i in range(n):
        for j in range(n):
            if board[i,j] == 0:
                draw.fill(0, 0, 0, 1)
            else:
                draw.fill(255, 255, 255, 1)
            draw.rect(square_size * j, square_size * i, square_size, square_size)


def simulation(steps: int, initialBoard: array) -> None:
    board = array(initialBoard, copy=True)
    for step in range(steps):
        draw_board(board)
        board = update_board(board)
        print(f"{step+1}/{steps}")
    draw.saveImage("LifeGame.mp4")


board = array([
    [1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
])

if __name__ == "__main__":
    board = pad(board,pad_width=46)
    simulation(800,board)
