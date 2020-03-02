#!/usr/bin/python3.7

import json
import adjacencyList as alist

def readDataFromFile(fileName):
    data = {}
    try:
        with open(file=fileName, mode="r") as file:
            data = json.load(file)
            # print(data)
    except OSError:
        print("Err while opening file")
        exit(-1)

    if data['type'] == 'adjacency_list':
        return alist.AdjacencyList(data['data'])
