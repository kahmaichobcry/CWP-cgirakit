def is_clear(board, row1, col1, row2, col2):

    row_step = 0
    col_step = 0

    if row2 > row1:
        row_step = 1
    elif row2 < row1:
        row_step = -1

    if col2 > col1:
        col_step = 1
    elif col2 < col1:
        col_step = -1

    row = row1 + row_step
    col = col1 + col_step

    while row != row2 or col != col2:

        if board[row][col] in "PBRQK":
            return False

        row += row_step
        col += col_step

    return True


def pawn_attacks(row, col, king_row, king_col):

    return (
        king_row == row - 1
        and abs(king_col - col) == 1
    )


def rook_attacks(board, row, col, king_row, king_col):

    if row != king_row and col != king_col:
        return False

    return is_clear(
        board,
        row,
        col,
        king_row,
        king_col
    )


def bishop_attacks(board, row, col, king_row, king_col):

    if abs(row - king_row) != abs(col - king_col):
        return False

    return is_clear(
        board,
        row,
        col,
        king_row,
        king_col
    )


def queen_attacks(board, row, col, king_row, king_col):

    return (
        rook_attacks(
            board,
            row,
            col,
            king_row,
            king_col
        )
        or
        bishop_attacks(
            board,
            row,
            col,
            king_row,
            king_col
        )
    )


def checkmate(board):

    rows = board.splitlines()

    if len(rows) == 0:
        return

    size = len(rows)

    # ตรวจว่า board เป็นสี่เหลี่ยม
    for row in rows:
        if len(row) != size:
            return

    # หา King
    king_row = -1
    king_col = -1

    for row in range(size):
        for col in range(size):

            if rows[row][col] == "K":
                king_row = row
                king_col = col

    # ไม่มี King
    if king_row == -1:
        return

    # ตรวจทุกตัว
    for row in range(size):
        for col in range(size):

            piece = rows[row][col]

            if piece == "P":

                if pawn_attacks(
                    row,
                    col,
                    king_row,
                    king_col
                ):
                    print("Success")
                    return

            elif piece == "R":

                if rook_attacks(
                    rows,
                    row,
                    col,
                    king_row,
                    king_col
                ):
                    print("Success")
                    return

            elif piece == "B":

                if bishop_attacks(
                    rows,
                    row,
                    col,
                    king_row,
                    king_col
                ):
                    print("Success")
                    return

            elif piece == "Q":

                if queen_attacks(
                    rows,
                    row,
                    col,
                    king_row,
                    king_col
                ):
                    print("Success")
                    return

    print("Fail")
