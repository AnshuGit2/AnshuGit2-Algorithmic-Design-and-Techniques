# python3

n = int(input())
a = [int(x) for x in input().split()]
largest_integer = max(a)
a.remove(largest_integer)
S_largest_integer = max(a)
print(largest_integer*S_largest_integer)
