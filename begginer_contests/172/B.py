S = list(str(input()))
T = list(str(input()))
count = 0
for i in range(len(S)):
    if T[i] != S[i]:
        count += 1
print(count)

