def snowball(n, k):
    m =  0.5
    r = n/2

    for i in range(n):
        print( k * " ", end = "")
        for j in range(n):
            if (i + m - r) ** 2 + (j + m -r) ** 2 <= r ** 2:
                print("X", end="")
            else:
                print(" ", end="")
        print()

def snowman(n):
    snowball(n, 2)
    snowball(n + 2, 1)
    snowball(n + 4, 0)
    print()
snowman(2)
