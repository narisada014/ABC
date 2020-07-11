# クソコード例
# x,y,zの取りうる範囲は1 ≤ x, y, z ≤ n^(1/2)程度なので105までくらい
# 最後に100 * 100 * 100をするのはいいが、これは各nに対して計算を回すことになるので
# 100000とか来たら100 * 100 * 100 * 100000になって無事死亡
N = int(input())
def shiki(a, b, c):
    return a ** 2 + b ** 2 + c ** 2 + a * b + b * c + c * a

def condition(n):
    count = 0
    i = 0
    j = 0
    k = 0
    for i in range(1, 105):
        for j in range(1, 105):
            for k in range(1, 105):
                if shiki(i, j, k) == n:
                    count += 1
    print(count)

for i in range(N):
    condition(i)

# いいコード例
# 先に配列を作っておいて、100 * 100 * 100の計算一回で全ての個数を記録しておき、
# インデックスアクセスで値を標準出力する
N = int(input())
ans = [0] * 100000
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            ans[x*x+y*y+z*z+x*y+y*z+z*x-1] += 1
for i in range(N):
    print(ans[i])