from gurobipy import *
b=0
while b <= 10:
    VarIndexes = [1,2,3,4]
    Costs = {1:6, 2:4, 3:2, 4:1}
    m = Model("Q4")
    x = m.addVars(VarIndexes,lb=0, name="x")
    m.setObjective(quicksum(Costs[i]*x[i] for i in range(1,5)), GRB.MAXIMIZE)
    m.addConstr(x[1] + x[2] + x[3] + x[4] <= b)
    m.addConstr(x[1] <= 2)
    m.addConstr(x[2] <= 3)
    m.addConstr(x[3] <= 1)
    m.addConstr(x[3] <= 4)
    m.optimize()
    for v in m.getVars():
            print('%s %g' % (v.varName, v.x))
    print('Optimal value: %g' % m.objVal)
    X = m.getAttr(GRB.Attr.X, m.getVars())
    print('Optimal solution: ' + str(X))
    b += 1