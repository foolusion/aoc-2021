import re


def mark_boards(boards, n):
    for i in range(len(boards)):
        mark(boards[i], n)


def mark(board, n):
    for r, row in enumerate(board):
        for c, num in enumerate(row):
            if num[0] == n:
                board[r][c] = (n, True)
                return


def check_boards(boards):
    winners = []
    for i, board in enumerate(boards):
        if check(board):
            winners.append(i)
    return winners


def check(board: list[list[tuple[int, bool]]]):
    for i in range(5):
        if all(i[1] for i in board[i]):
            return True
        if all(
            i[1]
            for i in [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        ):
            return True
    return False


def score(board: list[list[tuple[int, bool]]], n: int):
    total = 0
    for row in board:
        for num, marked in row:
            if not marked:
                total += num
    return total * n


def main():
    lines = []
    with open("day_04.in", "r") as f:
        lines = f.readlines()

    numbers = [int(i) for i in lines[0].split(",")]
    lines.pop(0)

    boards = []
    num_boards = (len(lines) - 1) // 6

    for _ in range(num_boards):
        lines.pop(0)
        board = []
        for x in range(5):
            board.append([(int(i), False) for i in re.split(r"\s+", lines[0].strip())])
            lines.pop(0)
        boards.append(board)

    for n in numbers:
        mark_boards(boards, n)
        x = check_boards(boards)
        if x:
            for b in x:
                print(score(boards[b], n))
            for b in sorted(x, reverse=True):
                del boards[b]
        if len(boards) == 0:
            print("DONE")
            break


if __name__ == "__main__":
    main()
