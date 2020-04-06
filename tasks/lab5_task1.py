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
                if {'dest': w, 'l': i+1} not in j['edges']:
                    j['edges'].append({'dest': w, 'l': i+1})
                    layers[i+1][w]['edges'].append({'src': j['v'], 'l': i})
                    alledges.append((j['v'] + getNumberOfV(layers, i), w + getNumberOfV(layers, i+1)))
                    k = k - 1
    l = 2*numberOfBetweenLayers
    while l >= 0:
        n = randrange(1, lastIndex)
        n2 = n - 1 if random() < 0.5 and n > 1 else n + 1
        nw = len(layers[n])
        nw2 = len(layers[n2])
        ni = randrange(nw)
        ni2 = randrange(nw2)
        dire = 'src' if random() >= 0.5 else 'dest'
        dire2 = 'src' if dire == 'dest' else 'dest'
        edge1 = {dire: ni2, 'l': n2}
        edge2 = {dire2: ni, 'l': n}
        if edge1 not in layers[n][ni]['edges'] and edge2 not in layers[n2][ni2]['edges']:
            layers[n][ni]['edges'].append(edge1)
            layers[n2][ni2]['edges'].append(edge2)
            if 'src' in edge1.keys():
                alledges.append((ni2 + getNumberOfV(layers, n2), ni + getNumberOfV(layers, n)))
            else:
                alledges.append((ni + getNumberOfV(layers, n), ni2 + getNumberOfV(layers, n2)))
            l = l - 1
    for ii, i in enumerate(layers):
        for v in i:
            for e in v['edges']:
                if 'src' in e.keys():
                    w = randrange(1, 11)
                    e['weight'] = w
                    layers[e['l']][e['src']]['edges'][layers[e['l']][e['src']]['edges'].index({'dest': v['v'], 'l': ii})]['weight'] = w


    return layers, alledges
