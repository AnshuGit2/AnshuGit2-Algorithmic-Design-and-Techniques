#python3
def fib_last_digit(n):
    if n < 2: return n
    else:
        fib1, fib2 = 0, 1
        for i in range(1,n):
            fib1, fib2 = fib2, (fib1+fib2) % 10
        print(fib2)

n = int(input())
fib_last_digit(n)
