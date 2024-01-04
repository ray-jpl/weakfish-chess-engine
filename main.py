import chess

pos_infinity = float('inf')
neg_infinity = float('-inf')

piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

## Board is visually reversed as A1 is square 0 and h8 is square 63
piece_table_white = {
    chess.PAWN:   [  0,  0,  0,  0,  0,  0,  0,  0,
                     5, 10, 10,-20,-20, 10, 10,  5,
                     5, -5,-10,  0,  0,-10, -5,  5,
                     0,  0,  0, 20, 20,  0,  0,  0,
                     5,  5, 10, 25, 25, 10,  5,  5,
                    10, 10, 20, 30, 30, 20, 10, 10,
                    50, 50, 50, 50, 50, 50, 50, 50,
                     0,  0,  0,  0,  0,  0,  0,  0],
    chess.KNIGHT: [-50,-40,-30,-30,-30,-30,-40,-50,
                   -40,-20,  0,  0,  0,  0,-20,-40,
                   -30,  0, 10, 15, 15, 10,  0,-30,
                   -30,  5, 15, 20, 20, 15,  5,-30,
                   -30,  0, 15, 20, 20, 15,  0,-30,
                   -30,  5, 10, 15, 15, 10,  5,-30,
                   -40,-20,  0,  5,  5,  0,-20,-40,
                   -50,-40,-30,-30,-30,-30,-40,-50],
    chess.BISHOP: [-20,-10,-10,-10,-10,-10,-10,-20,
                   -10,  5,  0,  0,  0,  0,  5,-10,
                   -10, 10, 10, 10, 10, 10, 10,-10,
                   -10,  0, 10, 10, 10, 10,  0,-10,
                   -10,  5,  5, 10, 10,  5,  5,-10,
                   -10,  0,  5, 10, 10,  5,  0,-10,
                   -10,  0,  0,  0,  0,  0,  0,-10,
                   -20,-10,-10,-10,-10,-10,-10,-20], 
    chess.ROOK:   [  0,  0,  0,  5,  5,  0,  0,  0,
                    -5,  0,  0,  0,  0,  0,  0, -5,
                    -5,  0,  0,  0,  0,  0,  0, -5,
                    -5,  0,  0,  0,  0,  0,  0, -5,
                    -5,  0,  0,  0,  0,  0,  0, -5,
                    -5,  0,  0,  0,  0,  0,  0, -5,
                     5, 10, 10, 10, 10, 10, 10,  5,
                     0,  0,  0,  0,  0,  0,  0,  0],
    chess.QUEEN:  [-20,-10,-10, -5, -5,-10,-10,-20,
                   -10,  0,  0,  0,  0,  0,  0,-10,
                   -10,  0,  5,  5,  5,  5,  0,-10,
                    -5,  0,  5,  5,  5,  5,  0, -5,
                     0,  0,  5,  5,  5,  5,  0, -5,
                   -10,  5,  5,  5,  5,  5,  0,-10,
                   -10,  0,  5,  0,  0,  0,  0,-10,
                   -20,-10,-10, -5, -5,-10,-10,-20],
    chess.KING:   [ 20, 30, 10,  0,  0, 10, 30, 20,
                    20, 20,  0,  0,  0,  0, 20, 20,
                   -10,-20,-20,-20,-20,-20,-20,-10,
                    20,-30,-30,-40,-40,-30,-30,-20,
                   -30,-40,-40,-50,-50,-40,-40,-30,
                   -30,-40,-40,-50,-50,-40,-40,-30,
                   -30,-40,-40,-50,-50,-40,-40,-30,
                   -30,-40,-40,-50,-50,-40,-40,-30]       
}

piece_table_black = {
    chess.PAWN:   list(reversed(piece_table_white[chess.PAWN])),
    chess.KNIGHT: list(reversed(piece_table_white[chess.KNIGHT])),
    chess.BISHOP: list(reversed(piece_table_white[chess.BISHOP])),
    chess.ROOK:   list(reversed(piece_table_white[chess.ROOK])),
    chess.QUEEN:  list(reversed(piece_table_white[chess.QUEEN])),
    chess.KING:   list(reversed(piece_table_white[chess.KING])),   
}

def eval_board(board):
    """
    Evaluate board by going over each square and summing piece value
        Positive score indicates WHITE has an advantage
        Negative score indicates BLACK has an advantage        
    """
    eval_total = 0.0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece != None:
            piece_colour = 1 if piece.color == chess.WHITE else -1
            
            eval_total += piece_colour * (piece_value[piece.piece_type] + eval_piece_table_value(piece, square))
    return eval_total

def eval_piece_table_value(piece, square):
    """
    Evaluate the additional piece value from the piece table
    """
    if (piece.color == chess.WHITE):
        return piece_table_white[piece.piece_type][square]
    else:
        return piece_table_black[piece.piece_type][square]

def search_all_captures(board, is_white):
    """
    Evaluate board with possible captures

    Continues to search until all possible captures are searched
    """
    
    # Current piece value and position evaluation
    cur_evaluation = eval_board(board)

    # Check all current capturing moves
    # No depth checked as we need to account for all captures/trades
    legal_moves = list(board.legal_moves)
    if is_white:
        for move in legal_moves:
            if (board.is_capture(move)):
                board.push(move)
                eval = search_all_captures(board, False)
                cur_evaluation = max(cur_evaluation, eval)
                board.pop()
    else:
        for move in legal_moves:
            if (board.is_capture(move)):
                board.push(move)
                eval = search_all_captures(board, False)
                cur_evaluation = min(cur_evaluation, eval)
                board.pop()
    
    return cur_evaluation


def search(board, depth, is_white):
    """
    Searches tree of possible moves and returns the best evaluation score

    Evaluation gives a positive score if white advantage or negative score for black advantage
    Therefore white is trying to get maximum score and black is minimising the score. 
    """
    if (depth == 0):
        return search_all_captures(board, is_white)
    
    ## Check if player is in checkmate
    legal_moves = list(board.legal_moves)
    if (len(legal_moves) == 0):
        if (board.is_checkmate()):
            return neg_infinity if is_white else pos_infinity
        ## No legal moves and no checkmate means a draw
        return 0.0
    
    if is_white:
        max_eval = neg_infinity
        for move in legal_moves:
            board.push(move)
            eval = search(board, depth - 1, False)
            max_eval = max(max_eval, eval)
            board.pop()
        return max_eval
    else:
        min_eval = pos_infinity
        for move in legal_moves:
            board.push(move)
            eval = search(board, depth - 1, True)
            min_eval = min(min_eval, eval)
            board.pop()
        return min_eval

def get_best_move(board, depth):
    """
    Searches current legal moves for current colour
    
    Returns best move
    """
    is_white = (board.turn == chess.WHITE)
    best_eval = neg_infinity if is_white else pos_infinity

    legal_moves = list(board.legal_moves)
    best_move = legal_moves[0]

    for move in legal_moves:
        board.push(move)
        value = search(board, depth - 1, is_white)
        board.pop()
        if is_white and (value > best_eval):
            best_eval = value
            best_move = move
        elif not is_white and (value < best_eval):
            best_eval = value
            best_move = move
    # print("WHITE" if is_white else "BLACK")
    # print(f"evaluation: {best_eval}")
    return best_move

def uciCommandLoop():
    """
    Reads UCI commands from stdin and returns output in stdout
    
    Implemented basic UCI commands from the UCI protocol to interface with lichess-bot
    - https://github.com/lichess-bot-devs/lichess-bot
    - https://www.wbec-ridderkerk.nl/html/UCIProtocol.html
    """
    # Init board
    board = chess.Board()
    while True:
        args = input().split()
        if args[0] == "uci":
            print("id name Weakfish")
            print("id author Raymond")
            # acknowledge the uci mode
            print("uciok") 
        elif args[0] == "isready":
            print("readyok")
        elif args[0] == "quit":
            break
        elif args[0] == "position":
            if args[1] == "startpos":
                board.reset()            
            elif args[1] == "fen":
                fen = " ".join(args[2:8])
                board.set_fen(fen)
            
            hasMoves = False
            for arg in args:
                if arg == "moves":
                    hasMoves = True
                elif hasMoves:
                    board.push_uci(arg)
                
        elif args[0] == "go":
            # Evaluate Position
            move = get_best_move(board, 3)
            board.push(move)
            print(f"bestmove {move}")

            # print(board)
            # print("\n")

##################### 
## Start Game Loop ##
#####################
uciCommandLoop()