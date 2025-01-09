from gurobipy import *


Indices = [1,2,3,4,5,6]
m = Model("Beamlets")
x = m.addVars(Indices,lb=0, name="x")
m.setObjective(3*x[1] + 3*x[2] + 2.5*x[3] + 2*x[4] + 2*x[5] + 4.5 * x[6], GRB.MINIMIZE)
m.addConstr(1.5*x[3] + 1.5*x[4] >= 9)
m.addConstr(2*x[1] + 2*x[5] >= 9)
m.addConstr(2*x[2] + 2*x[5] <= 5)
m.addConstr(1.5*x[3] + 1.5*x[5] >= 9)
m.addConstr(2.5*x[2] + 2.5*x[6] >= 9)
m.optimize()

# Print optimal solution
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
        
# Print optimal value1.5*x[3] + 1.5*x[4] >= 9
print('Optimal value: %g' % m.objVal)

# Store optimal solution
X = m.getAttr(GRB.Attr.X, m.getVars())
print('Optimal solution: ' + str(X))