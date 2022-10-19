def chess_board(n,k):
    for p in range(0,2 * n):
        for i in range(0,2):
            print((" " * k + "#" * k ) * n)
        for j in range (2,4):
            print (("#" * k + " " * k ) * n)
chess_board(4,2)
