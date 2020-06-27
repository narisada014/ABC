N, M, K = map(int, input().split())
times_a = list(map(int, input().split()))
times_b = list(map(int, input().split()))
read_time = 0
read_time_a = [0]
read_time_b = [0]
for i in range(N):
    read_time_a.append(read_time_a[i]+times_a[i])
for i in range(M):
    read_time_b.append(read_time_b[i]+times_b[i])

ans = 0
for a_count in range(N+1):
    a_read_time = read_time_a[a_count]
    max_b_count = 0
    r = len(read_time_b)
    # 消化時間の配列はソートされている状態だから二分探索
    while max_b_count + 1 < r:
        # 2分探索で計算量をlog(r)に削減
        c = (max_b_count + r) // 2
        if a_read_time + read_time_b[c] <= K:
            max_b_count = c
        # 超えちゃったらwhileをr=cでストップ
        else:
            r = c
    # 積読消化時間がKより小さく、a_count + max_b_countの最大数が最大になるものをansに代入し続ける
    if read_time_a[a_count] + read_time_b[max_b_count] <= K:
        ans = max(ans, a_count + max_b_count)
print(ans)
