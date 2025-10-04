def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+---")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+---")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    # Returns True if there are no empty spaces and no winner
    return all(space != " " for space in board)

def play_game():
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"
    else:
        print("invalid move. Try again.")
# run the game
play_game()
    