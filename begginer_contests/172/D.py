N = int(input())
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass
ans = 0
for i in range(N):
    ans += (i+1)*len(divisor(i+1))
print(ans)