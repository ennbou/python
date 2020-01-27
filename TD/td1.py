G = [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0]

T = []

l = len(G)


def rec(index, v):
    if index > l or index < 0:
        return 0
    if G[index] == 1:
        return rec(index+v, v) + 1
    return 0


for i in range(len(G)):
    if G[i] == 1:
        T.append(rec(i, 1)+rec(i, -1) - 1)
    else:
        T.append(0)

for e in T:
    print(e)
