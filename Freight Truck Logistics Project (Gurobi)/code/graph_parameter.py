# Zach Ellison, Wyatt Entrekin, Rocco Russo
import numpy as np
import pandas as pd

def graph_parameter(nodes, arcs, commodities):

    # Read In CSV Files
    N_df = pd.read_csv(nodes)
    arcs_df = pd.read_csv(arcs)
    commodities_df = pd.read_csv(commodities)
    
    # Commodities & Quantities, O, Sinks
    K_Q = {}
    O = {}
    D = {}
    for index, row in commodities_df.iterrows():
        K_Q[row['name']] = row['weight']
        O[row['name']] = row['source']
        D[row['name']] = row['sink']

    # N
    N = {}
    for index, row in N_df.iterrows():
        N[row['nodes']] = (row['nodes_x'], row['nodes_y'])

    # Arcs
    A = []
    for index, row in arcs_df.iterrows():
        A.append((row['Head'], row['Tail']))

    # Distances
    m = {}
    for arc in A:
        head = N[arc[0]]
        tail = N[arc[1]]
        distance = np.sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2)
        m[arc] = distance

    return K_Q, N, A, O, D, m

if __name__ == '__main__':
    result = graph_parameter('data/Nodes_Revised.csv', 'data/Arcs.csv', 'data/Commodities.csv')
    print(result)
