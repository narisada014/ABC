K = int(input())

# 剰余の世界はたかだかKで数列がループする性質がある。
mod = 7 % K
for i in range(K):
    if mod == 0:
        print(i+1)
        exit()
    mod = (mod * 10 + 7) % K
print(-1)
