#!/usr/bin/python3.7


def graphCenter(distanceMatrix):
    sums = list(map(sum, distanceMatrix))
    gCenter = sums.index(min(sums))
    maximum = list(map(max, distanceMatrix))
    minimax = maximum.index(min(maximum))

    return gCenter, minimax
