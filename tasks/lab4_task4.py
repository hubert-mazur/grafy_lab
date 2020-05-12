from tasks.lab4_task3 import generate_strongly_connected_graph
from utils.johnson import johnson


def lab4_task4(n):
    g_rep, g_tup = generate_strongly_connected_graph(n)

    weights = {(i, j): z['weight'] for i, j, z in g_tup}  # kluczem jest krotka z krawedzia, wartoscia jest waga
    D = johnson(g_rep, g_tup, weights, n)

    return g_rep, g_tup, weights, D
