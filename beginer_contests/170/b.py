a = input().split()
# 奇数の時
x = int(a[0])
y = int(a[1])
if y % 2 != 0 or 2 * x > y:
    print('No')
elif 2 * x - y / 2 >= 0:
    print('Yes')
else:
    print('No')