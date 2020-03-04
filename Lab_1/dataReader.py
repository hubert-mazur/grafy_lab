#!/usr/bin/python3.7

import json
import adjacencyList 
import incidenceMatrix
import adjacencyMatrix


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
        return adjacencyList.AdjacencyList(data['data'])
    elif data['type'] == 'incidence_matrix':
        return incidenceMatrix.IncidenceMatrix(data['data'])
    elif data['type'] == 'adjacency_matrix':
        return adjacencyMatrix.AdjacencyMatrix(data['data'])
    else:
        print("Unknown type of data!")
        exit()
