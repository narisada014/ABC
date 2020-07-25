N,K = map(int, input().split())
a_arr = list(map(int, input().split()))

k_idx = K - 1
ans_arr = []
for i in range(N - K):
    if a_arr[i] < a_arr[k_idx + 1]:
        ans_arr.append('Yes')
    else:
        ans_arr.append('No')
    k_idx += 1
for i in ans_arr:
    print(i)