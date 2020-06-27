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
    # 積読消化時間read_time_a[a_count]がKより大きい場合は処理をスルー
    if read_time_a[a_count] > K:
        continue
    a_read_time = read_time_a[a_count]
    max_b_count = 0
    r = len(read_time_b)
    # 消化時間の配列はソートされている状態だから二分探索
    # 計算量をlog(M)に削減
    while max_b_count + 1 < r:
        c = (max_b_count + r) // 2
        # bがインデックスcで時間がaの時間+bの時間でK以下ならmax_b_countを二分探索の開始位置に更新する。
        if a_read_time + read_time_b[c] <= K:
            max_b_count = c
        # 超えちゃったら二分探索の前方に探索領域の終端を絞る
        else:
            r = c
    # a_count + max_b_countの最大数が最大になるものをansに代入し続ける
    ans = max(ans, a_count + max_b_count)
print(ans)
