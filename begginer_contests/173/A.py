N = int(input())
p_count = N % 1000
if p_count == 0:
    print(0)
else:
    print(1000 - p_count)