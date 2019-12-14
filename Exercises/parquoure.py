G = {
    'A': {'B','C','D'},
    'B': {'E'},
    'C': {'B','D','E'},
    'D': {'E'},
    'E': {},
}

def parquore(g,visite,chemain):
    s = visite[-1]
    print("start")
    for v in g[s]:
        if v not in visite:
            visite.append(v)
            chemain.append((s,v))
            parquore(g,visite,chemain)


chemain = []
visite = ['A']
parquore(G,visite,chemain)

for a in visite:
    print(a)

for a in chemain:
    print(a)