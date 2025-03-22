import os
import math

# Reprezentacja planszy
board = [" " for _ in range(9)]


def print_board():
    os.system("clear")  # macOS/Linux (użyj "cls" dla Windows)
    print("\nAktualna plansza:")
    print()
    for i, row in enumerate([board[i * 3:(i + 1) * 3] for i in range(3)]):
        print(" | ".join(cell if cell != " " else str(i * 3 + j) for j, cell in enumerate(row)))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(b, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        if all(b[i] == player for i in combo):
            return True
    return False


def empty_cells(b):
    return [i for i in range(9) if b[i] == " "]


def is_draw(b):
    return " " not in b


def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in empty_cells(b):
            b[i] = "O"
            score = minimax(b, depth + 1, False)
            b[i] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in empty_cells(b):
            b[i] = "X"
            score = minimax(b, depth + 1, True)
            b[i] = " "
            best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = None
    for i in empty_cells(board):
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = "O"


def play():
    print_board()
    while True:
        try:
            move = int(input("Wybierz pole (0-8): "))
            if board[move] != " ":
                print("To pole jest zajęte! Wybierz inne.")
                continue
        except (ValueError, IndexError):
            print("Nieprawidłowy ruch. Spróbuj ponownie.")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("🎉 Wygrałeś!")
            break
        if is_draw(board):
            print("🤝 Remis!")
            break

        print("Ruch AI...")
        ai_move()
        print_board()

        if check_winner(board, "O"):
            print("💻 AI wygrało!")
            break
        if is_draw(board):
            print("🤝 Remis!")
            break


if __name__ == "__main__":
    play()
