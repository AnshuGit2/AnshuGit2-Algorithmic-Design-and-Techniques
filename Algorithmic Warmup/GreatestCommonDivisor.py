# Uses python3

def calGCD (n1, n2):
    if b==0:
        return n1
    else:
        return calGCD(n2, n1%n2)
user_input = input()
n1, n2 = map(int, user_input.split())
print(calGCD(n1, n2))
