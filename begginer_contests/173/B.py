N = int(input())
words = []
for i in range(N):
    w = input()
    words.append(w)
ac_len = words.count('AC')
wa_len = words.count('WA')
tl_len = words.count('TLE')
re_len = words.count('RE')
print(f'AC x {ac_len}')
print(f'WA x {wa_len}')
print(f'TLE x {tl_len}')
print(f'RE x {re_len}')