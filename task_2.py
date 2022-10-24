def chess_board(n,k):
    for _ in range(n):
        for _ in range(k):
            print((" " * k + "#" * k ) * n)
        for _ in range (k, k + 2):
            print (("#" * k + " " * k ) * n)
chess_board(4,2)
