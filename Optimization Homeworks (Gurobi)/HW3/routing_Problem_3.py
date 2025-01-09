from gurobipy import *


# Create a new model
m = Model("Routing")
# Create variables with nonnegativity constraints
x = m.addVars(4, 4, lb = 0, ub = 1, vtype = GRB.CONTINUOUS, name="x")

# Set objective: 
m.setObjective(8*x[0,0] + 7*x[0,1] + 8*x[1,0] + 9*x[1,1] + 5*x[1,3] + 3*x[2,0] + 2*x[2,2] + 4*x[3,2] + 4*x[3,3], GRB.MINIMIZE)

# Add constraints: 
m.addConstr(x[0,0] + x[0,1]  == 1)
m.addConstr(x[1,0] + x[1,1] + x[1,3] == 1)
m.addConstr(x[2,0] + x[2,2] == 1)
m.addConstr(x[3,2] + x[3,3] == 1)
m.addConstr(x[0,0] + x[1,0] + x[2,0]  == 1)
m.addConstr(x[0,1] + x[1,1] == 1)
m.addConstr(x[2,2] + x[3,2] == 1)
m.addConstr(x[1,3] + x[3,3] == 1)

# Solve the model
m.optimize()

# Print optimal solution
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
        
# Print optimal value
print('Optimal value: %g' % m.objVal)

# Store optimal solution
X = m.getAttr(GRB.Attr.X, m.getVars())
print('Optimal solution: ' + str(X))