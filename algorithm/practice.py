N = 10

_list = []
for i in range(1, N/2+1):
    if N%i == 0:
        _list.append(i)

print(_list)