from pprint import pprint

from checkmate import checkmate
from board_chess import board_to_list
from board_chess import get_board_size
from board_chess import create_check_range


def print_board(board):
    print("[", end="")

    for i, row in enumerate(board):
        if i == 0:
            print(row, end="")
        else:
            print(" " + str(row), end="")

        if i < len(board) - 1:
            print(",")

    print("]")


def main():

    board = """\
R...
.K..
P.P.
...."""

    # แสดง Board
    board_list = board_to_list(board)
    print_board(board_list)

    # แสดงขนาด Board
    board_size = get_board_size(board)
    print(board_size)

    # แสดง Check Range
    print("Check Range:")

    check_range = create_check_range(board)
    print_board(check_range)

    # ตรวจว่า King ถูก Check หรือไม่
    checkmate(board)


if __name__ == "__main__":
    main()
