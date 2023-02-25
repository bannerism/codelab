##https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

def is_solved(board):
    # TODO: Check if the board is solved!
    # 1 X 2 O
    def parse_board(board):
        row = []
        col = []
        main = []
        anti_r = []
        for i,x in enumerate(board):
            row.append(x)
            col.append([x[i] for x in board])
            main.append(board[i][i])
            draob = [s for s in reversed(board)]
            anti_r.append(draob[i][i])

        anti = anti_r[::-1]
        return row, col, main, anti

    def check_row(row):
        results = []
        for r in row:
            results.append(list(set(r)))

        winner = []
        for s in results:
            if len(s) == 1:
                if s[0] != 0:
                    winner.append(s[0])
            else:
                winner.append(-1)
        
        return winner[0]
    
    row, col, main, anti = parse_board(board)
    print(check_row(row))
