def envelope(n):
    p1 = 0
    p2 = n - 4
    print(9 * "*")
    for _ in range((n // 2) -1):
        print("*", " " * p1, "*", " " * p2, "*", " " * p1, "*", sep="")
        p1 = p1 + 1
        p2 = p2 - 2
    print("*", " " * (p1 - 2), "*", " " * (p1 - 2), "*")
    for _ in range((n // 2) - 1):
        print("*", " " * (p1 - 1), "*", " " * (p2 + 2), "*", " " * (p1 - 1), "*", sep="")
        p1 = p1 - 1
        p2 = p2 + 2
    print(9 * "*")

envelope(9)
