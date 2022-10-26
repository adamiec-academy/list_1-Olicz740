def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def report():
     factorial = 1
     print(f"{0 : >3}! is {1 : >3} digits long")
     for i in range(1, 101):
         factorial *= i
         print(f"{i : >3}! is {len(str(factorial)) : >3} digits long")
report()
