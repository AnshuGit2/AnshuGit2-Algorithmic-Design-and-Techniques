# Uses python3

def calGCD (a, b):
    if b==0:
        return a
    else:
        return calGCD(b, a%b)
user_input = input()
a, b = map(int, user_input.split())
print(calGCD(a, b))
