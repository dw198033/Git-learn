N = int(input())

print(N)
print(type(N))


s = [i for i in input().split()]
print(s)

data_list = []
for i in range(N):
    ll = int(s[i])
    print(ll)
    data_list.append(ll)
print(data_list)


def validUtf8(data):

    k = 0
    for x in data:
        if k:
            if x > 191 or x < 128: return False
            k -= 1
        else:
            if x > 247: return False
            if x > 239: k =3
            elif x > 223: k = 2
            elif x > 191: k = 1
            elif x > 127 or x < 0: return False
    return not k

res = validUtf8(data_list)
print(res)

