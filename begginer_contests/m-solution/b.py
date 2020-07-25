a,b,c = map(int, input().split())
K = int(input())

for i in range(K):
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
if a < b and b < c:
    print('Yes')
else:
    print('No')
