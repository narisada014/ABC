N = int(input())
X = str(input())

def toggle_nth_bit(num, n):
    return num ^ (1 << n)

Xis = []
for i in list(reversed(range(N))):
    Xis.append(toggle_nth_bit(int(X, 2),i))

def popcount(x):
    count = 0
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

for i in Xis:
    count = 0
    while True:
        i = i % popcount(i)
        count += 1
        if i == 0:
            break
    print(count)
