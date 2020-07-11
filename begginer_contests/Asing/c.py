N = int(input())
ans = [0] * 100000
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            ans[x*x+y*y+z*z+x*y+y*z+z*x-1] += 1
for i in range(N):
    print(ans[i])