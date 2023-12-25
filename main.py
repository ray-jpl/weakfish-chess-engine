import chess

# from chessboard import display

def uciCommandLoop():
    board = chess.Board()
    # game_board = display.start(board.fen())
    while True:
        args = input().split()
        # print(args)
        if args[0] == "uci":
            print("id name Weakfish")
            print("id author Raymond")
            # acknowledge the uci mode
            print("uciok") 
        elif args[0] == "isready":
            print("readyok")
        elif args[0] == "quit":
            break
        # elif args[0] == ["position"]:
        #     if args[1] == "startpos":
        #         board.reset()
        #     elif args[1] == "fen":
        #         fen = " ".join(args[2:8])
        #         board.set_fen(fen)
        
        elif args[0] == "go":
            # Evaluate Position
            board.push(chess.Move.from_uci("e2e4"))
            print(f"bestmove e2e4")
            # display.check_for_quit()
            # display.update(board.fen(), game_board)

uciCommandLoop()