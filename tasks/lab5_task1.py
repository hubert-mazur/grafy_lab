from random import randrange, random

def getNumberOfV(layers, n):
    if n == 0:
        return 0
    return sum(len(k) for k in layers[:n])

def random_flow_net(numberOfBetweenLayers):
    lastIndex = numberOfBetweenLayers + 1
    layers = [[] for _ in range(lastIndex+1)]
    alledges = []
    layers[0] = [{'v': 0, 'edges': []}]
    layers[lastIndex] = [{'v': 0, 'edges': []}]
    for i in range(1, lastIndex):
        layers[i] = [{'v': i, 'edges': []} for i in range(randrange(3, lastIndex+1))]
    for i in range(lastIndex):
        nw = len(layers[i+1])
        for j in layers[i]:
            k = randrange(1, nw) if nw > 1 else 1
            while k > 0:
                w = randrange(nw)
                we = randrange(1, 11)
                if {'dest': w, 'l': i+1} not in j['edges']:
                    j['edges'].append({'dest': w, 'l': i+1, 'weight': we})
                    layers[i+1][w]['edges'].append({'src': j['v'], 'l': i, 'weight': we})
                    alledges.append((j['v'] + getNumberOfV(layers, i), w + getNumberOfV(layers, i+1), {'weight': we}))
                    k = k - 1
    l = 2*numberOfBetweenLayers
    while l >= 0:
        n = randrange(1, lastIndex)
        n2 = n - 1 if random() < 0.5 and n > 1 else n + 1
        nw = len(layers[n])
        nw2 = len(layers[n2])
        ni = randrange(nw)
        ni2 = randrange(nw2)
        we = randrange(1, 11)
        dire = 'src' if random() >= 0.5 else 'dest'
        dire2 = 'src' if dire == 'dest' else 'dest'
        edge1 = {dire: ni2, 'l': n2, 'weight': we}
        edge2 = {dire2: ni, 'l': n, 'weight': we}
        if edge1 not in layers[n][ni]['edges'] and edge2 not in layers[n2][ni2]['edges']:
            layers[n][ni]['edges'].append(edge1)
            layers[n2][ni2]['edges'].append(edge2)
            if 'src' in edge1.keys():
                alledges.append((ni2 + getNumberOfV(layers, n2), ni + getNumberOfV(layers, n), {'weight': we}))
            else:
                alledges.append((ni + getNumberOfV(layers, n), ni2 + getNumberOfV(layers, n2), {'weight': we}))
            l = l - 1
    return layers, alledges


def random_flow_net_v2(numberOfBetweenLayers):
    lastIndex = numberOfBetweenLayers + 1
    layers = [[] for _ in range(lastIndex+1)]
    alledges = []
    layers[0] = [[]]
    layers[lastIndex] = [[]]
    for i in range(1, lastIndex):
        layers[i] = [[] for _ in range(randrange(3, lastIndex+1))]
    for iv, v in enumerate(layers[1]):
        we = randrange(1, 11)
        layers[0][0].append({'dest': iv, 'l': 1, 'weight': we})
        v.append({'src': 0, 'l': 0, 'weight': we})
        alledges.append((0, iv + getNumberOfV(layers, 1), {'weight': we}))
    for iv, v in enumerate(layers[lastIndex-1]):
        we = randrange(1, 11)
        layers[lastIndex][0].append({'src': iv, 'l': lastIndex-1, 'weight': we})
        v.append({'dest': 0, 'l': lastIndex, 'weight': we})
        alledges.append((iv + getNumberOfV(layers, lastIndex-1), getNumberOfV(layers, lastIndex), {'weight': we}))
    for l in range(1, lastIndex-1):
        il, il2, ln = (l, l+1, len(layers[l])) if len(layers[l]) > len(layers[l+1]) else (l+1, l, len(layers[l+1]))
        for i in range(ln):
            i2 = i if i < len(layers[il2]) else len(layers[il2])-1
            we = randrange(1, 11)
            if il2 > il:
                layers[il][i].append({'dest': i2, 'l': il2, 'weight': we})
                layers[il2][i2].append({'src': i, 'l': il, 'weight': we})
                alledges.append((i + getNumberOfV(layers, il), i2 + getNumberOfV(layers, il2), {'weight': we}))
            else:
                layers[il][i].append({'src': i2, 'l': il2, 'weight': we})
                layers[il2][i2].append({'dest': i, 'l': il, 'weight': we})
                alledges.append((i2 + getNumberOfV(layers, il2), i + getNumberOfV(layers, il), {'weight': we}))
    l = 2*numberOfBetweenLayers
    while l >= 0:
        n = randrange(1, lastIndex)
        n2 = None
        if n > 2 and n < lastIndex-1:
            n2 = randrange(n-1, n+1)
        elif n == 1:
            n2 = randrange(n, n+1)
        else:
            n2 = randrange(n-1, n)
        nw = len(layers[n])
        nw2 = len(layers[n2])
        ni = randrange(nw)
        ni2 = randrange(nw2)
        we = randrange(1, 11)
        dire = 'src' if random() >= 0.5 else 'dest'
        dire2 = 'src' if dire == 'dest' else 'dest'
        edge1 = {dire: ni2, 'l': n2, 'weight': we}
        edge1_2 = {dire2: ni2, 'l': n2, 'weight': we}
        edge2 = {dire2: ni, 'l': n, 'weight': we}
        edge2_2 = {dire: ni2, 'l': n, 'weight': we}
        if edge1 not in layers[n][ni] and edge2 not in layers[n2][ni2] and edge1_2 not in layers[n][ni] and edge2_2 not in layers[n2][ni2]:
            layers[n][ni].append(edge1)
            layers[n2][ni2].append(edge2)
            if 'src' in edge1.keys():
                alledges.append((ni2 + getNumberOfV(layers, n2), ni + getNumberOfV(layers, n), {'weight': we}))
            else:
                alledges.append((ni + getNumberOfV(layers, n), ni2 + getNumberOfV(layers, n2), {'weight': we}))
            l = l - 1
    return layers, alledges 
