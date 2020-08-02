N,D = map(int, input().split())
import math
count = 0
for i in range(N):
    X,Y = map(int, input().split())
    if D >= math.sqrt(X**2 + Y**2):
        count += 1
print(count)