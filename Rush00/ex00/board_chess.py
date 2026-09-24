def board_to_list(board):
    rows = board.splitlines()

    result = []

    for row in rows:
        result.append(list(row))

    return result


def get_board_size(board):
    rows = board.splitlines()

    return (len(rows), len(rows))


def create_check_range(board):
    rows = board.splitlines()
    result = board_to_list(board)

    size = len(rows)

    for row in range(size):
        for col in range(size):

            piece = rows[row][col]

            if piece == "R":
                mark_rook(result, rows, row, col)

            elif piece == "B":
                mark_bishop(result, rows, row, col)

            elif piece == "Q":
                mark_rook(result, rows, row, col)
                mark_bishop(result, rows, row, col)

            elif piece == "P":
                mark_pawn(result, rows, row, col)

    return result


def mark_rook(result, board, row, col):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    mark_line(result, board, row, col, directions)


def mark_bishop(result, board, row, col):
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    mark_line(result, board, row, col, directions)


def mark_line(result, board, row, col, directions):

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        while 0 <= r < len(board) and 0 <= c < len(board):

            # เจอ piece
            if board[r][c] in "PBRQK":

                # ถ้าเป็น King ให้ X
                if board[r][c] == "K":
                    result[r][c] = "X"

                # piece ขวางทาง
                break

            # ช่องว่างที่โจมตีได้
            result[r][c] = "X"

            r += dr
            c += dc


def mark_pawn(result, board, row, col):

    target_row = row - 1

    for target_col in [col - 1, col + 1]:

        if (
            0 <= target_row < len(board)
            and 0 <= target_col < len(board)
        ):
            result[target_row][target_col] = "X"
