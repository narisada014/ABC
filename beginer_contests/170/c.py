first_input = input().split()
x = int(first_input[0])
n = int(first_input[1])
if n != 0:
    second_input = map(int, input().split())
    p_a = list(map(int, second_input))
else:
    second_input = input()

def create_full_array(minimum, maximum):
    full_list = []
    for i in range(minimum,maximum+1):
        full_list.append(int(i))
    return full_list

if n == 0:
    print(x)
elif x > max(p_a) + 1 or x < min(p_a):
    ans = x - 1
    print(ans)
elif x == max(p_a) + 1:
    ans = x + 1
    print(ans)
else:
    full_array = create_full_array(min(p_a), max(p_a))
    if x in p_a:
        target_list = list(set(p_a)^set(full_array))
        abs_key = {}
        if len(target_list) == 0:
            if abs(x - min(p_a)) <= abs(x - max(p_a)):
                print(min(p_a) - 1)
            else:
                print(max(p_a) + 1)
        else:
            for i in target_list:
                abs_key[i] = abs(x-i)
            minimum = min(abs_key.values())
            t_k = []
            t_v = []
            [t_k.append(k) for k, v in abs_key.items() if v == minimum]
            print(min(t_k))

    else:
        print(x)

