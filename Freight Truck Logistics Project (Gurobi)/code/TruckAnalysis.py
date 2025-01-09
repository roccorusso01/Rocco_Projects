# Zach Ellison, Wyatt Entrekin, Rocco Russo
import numpy as np
import pandas as pd
from gurobipy import GRB, Model
from graph_parameter import graph_parameter
from datetime import timedelta

def get_data(): # Setting Up the Data for Use in the Model

    K_Q, N, A, O, D, m = graph_parameter('data/Nodes_Revised.csv', 'data/Arcs.csv', 'data/Commodities.csv') # Read Data from graph_parameter

    K = list(K_Q.keys())
    b_kn = {k: {n: 0 for n in N} for k in K} # Demand of Commodity k at Node n
    t_a = {a: 0 for a in A} # Number of Trucks on Arcs
     # Commodities

    for k in O.keys(): # Iterate through all commodities that are sources
        if k not in b_kn.keys(): # If a commodity is specified in the demand dictionary, make it a key
            d_k[k] = {}
        o_k = O[k] # Source of Commodity k
        d_k = D[k] # Sink of Commodity k

        b_kn[k][o_k] = -1 # Set Demand at Source Node of Commodity K to -1
        b_kn[k][d_k] = 1 # Set Demand at Sink Node of Commodity K to 1

    return K, A, N, K_Q, b_kn, m, t_a, O, D

def build_model(K, A, N, K_Q, b_kn, m, t): # Making the Model

    model = Model('ModelA')

    t_a = model.addVars(t, vtype = GRB.INTEGER, lb = 0, name = 't_a') # Decision Variable representing the number of trucks 't' on arc a
    c_ak = model.addVars(K, A, vtype = GRB.BINARY, name = 'c_ak') # Binary Decision Variable representing whether commodity k is sent on arc a

    model.addConstrs((sum(K_Q[k] * c_ak[k, a[0], a[1]] for k in K) <= t_a[a] for a in A)) # Fractional Number of Trucks Constraint
    model.addConstrs((c_ak.sum(k, '*', i) - c_ak.sum(k, i, '*') == b_kn[k][i] for i in N for k in K)) # Conservation of Flow of Demand Constraint

    model.setObjective(sum(t_a[a] * m[a] for a in A), GRB.MINIMIZE) # Objective Function minimizes the cost of trucks on each arc

    return model, c_ak, t_a

def optimize_model(model, c_ak, t_a):

    model.optimize() #Run Model

    return model.getAttr('x', c_ak), model.getAttr('x', t_a), model.objVal, model.Runtime

if __name__ == '__main__':

    # Building & Running Model
    K, A, N, K_Q, b_kn, m, t_a, O, D = get_data()
    model, c_ak, t_a = build_model(K, A, N, K_Q, b_kn, m, t_a)
    c_ak_solution, t_a_solution, objVal, runtime = optimize_model(model, c_ak, t_a)

    # Generating Output
    print('\n\n\n')
    print('###########################')
    print('#   OBJ VALUE SOLUTION    #')
    print(f'#         $ {round(objVal, 2)}         #')
    print('###########################')
    print('\n\n')

    # Path of Each Commodity
    print('Path of Each Commodity:')

    for k in K:

        print(f'\nPath for Commodity: {k} with Quantity: {K_Q[k]} from Source: {O[k]} to Sink: {D[k]})')

        first_arc = [f"Arc ({i[1]} -> {i[2]}) at Quantity: {K_Q[k]} for Price: ${round(m[i[1], i[2]] * K_Q[k], 2)}" for i, j in c_ak_solution.items() if j != 0 and i[0] == k and i[1] == O[k]][0]
        print(first_arc) #Arc the commodity leaves the source node at

        mid_arcs = [f"Arc ({i[1]} -> {i[2]}) at Quantity: {K_Q[k]} for Price: ${round(m[i[1], i[2]] * K_Q[k], 2)}" for i, j in c_ak_solution.items() if j != 0 and i[0] == k and i[1] != O[k] and i[2] != D[k]]
        for arc in mid_arcs:
            print(arc) # Arcs in the middle of the path

        last_arc = [f"Arc ({i[1]} -> {i[2]}) at Quantity: {K_Q[k]} for Price: ${round(m[i[1], i[2]] * K_Q[k], 2)}" for i, j in c_ak_solution.items() if j != 0 and i[0] == k and i[2] == D[k]][0]
        print(last_arc) # Arc the commodity enters the sink node at
    print('\n')

    # Number of Trucks and Commodities on Each Arc
    print('Number of Trucks on Each Arc:\n')
    for i, j in A:

        a_k = [s[0] for s, t in c_ak_solution.items() if t != 0 and s[1] == i and s[2] == j]
        a_w = sum([K_Q[k] for k in a_k])

        print(f'Arc ({i}->{j}) has {abs(round(t_a_solution[i, j], 2))} trucks carrying {len(a_k)} commodities with a total weight of {round(a_w, 2)}.')
        print('This arc carries the following commodities: ', (", ".join(a_k) if a_k else ""),'\n')

    # Runtime
    print(f'Gurobi Runtime: {timedelta(seconds=runtime)}')
