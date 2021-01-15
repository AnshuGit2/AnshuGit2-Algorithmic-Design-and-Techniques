# Python 3 
n = int(input())
list = []

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    list.append((a,b))

list.sort(key = lambda x: x[1])

index = 0
coordinates = []

while index < n:
    current = list[index]
    while index < n-1 and current[1]>=list[index+1][0]:
        index += 1
    coordinates.append(current[1])
    index += 1
print(len(coordinates))
print(' '.join([str(i) for i in coordinates]))
