N = int(input())
# 約数羅列
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
div_arr = make_divisors(N)

if len(div_arr) == 1:
    print(1)
elif len(div_arr) == 2:
    ans_num = max(div_arr)
    print(len(str(ans_num)))
else:
    memo = []
    if len(div_arr) % 2 == 0:
        last_idx = -1
        count = 0
        for i in range(len(div_arr)):
            count += 1
            if N == div_arr[i] * div_arr[last_idx] and count != len(div_arr) // 2:
                last_idx -= 1
                memo.append(len(str(div_arr[last_idx])))
            else:
                break
    else:
        target_index = len(div_arr) // 2
        memo.append(len(str(div_arr[target_index])))
    print(min(memo))

# https://drken1215.hatenablog.com/entry/2019/09/16/221500
# 桁を更新し続けて最後が一番小さくなる組み合わせになるのでこの方法でやった方がいい


