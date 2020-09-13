a, b, c, d = map(int, input().split())

print(max(max(max(a * c, b * d), b * c), a*d))
# if (a <= 0 and b <= 0 and c >= 0 and d >= 0) or (a >= 0 and b >= 0 and c <= 0 and d <= 0):
#     print(b * c)
# elif a <= 0 and c <= 0:
#     print(max(a * c, b * d))
# elif a > 0 and c > 0:
#     print(b * d)
    