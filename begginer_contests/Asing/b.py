N = int(input())
a_arr = list(map(int, input().split()))

count = 0
for i in range(1,N+1):
    if a_arr[i-1] % 2 != 0 and i % 2 != 0:
        count += 1
    else:
        next
print(count)