import chess

board = chess.Board()

print("Welcome to Console Chess! (2 Players)")
print("Use algebraic notation (e.g., e2e4) to make a move.\n")

while not board.is_game_over():
    print(board)
    print("Turn:", "White" if board.turn else "Black")
    
    move_input = input("Your move: ")
    
    try:
        move = chess.Move.from_uci(move_input)
        if move in board.legal_moves:
            board.push(move)
        else:
            print("❌ Invalid move. Try again.")
    except:
        print("❌ Invalid format. Use moves like e2e4, g1f3.")

print("\nGame Over!")
print("Result:", board.result())
