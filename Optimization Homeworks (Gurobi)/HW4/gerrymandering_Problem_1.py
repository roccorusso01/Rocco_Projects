from gurobipy import *

scenario1 = [42941,-917,-6650,1941,116,-5194,-299,9790,-6436,1723,870,-66,99,-8412,-3009,395,-81,9943,1361,-5504,-812,8016,-2313,2707,-13091,6473,34523,-965,1285,9145,-1107,-760,685]
scenario2 = [43411 ,18,-6244,1449,-871,-4241,223,8856,-6787,1993,260,-349,510,-7585,-2233,-347,233,9995,1780,-5578,-992,7948,-2665,1984,-13942,7008,34516,-658,1491,9779,-1980,-606,-304]
scenario3 = [11336,-716,-6436,1025,-1099,-5093,567,8251,-6736,1121,183,-286,1014,-8062,-1678,1984,-371,9711 ,975,-5135,-942,44329,-2263,5668,-13488,7571,12145,-173,3004,10226,-2245,-1368,909]
dist1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
dist2 = [0,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1]
dist3 = [0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,1,0]
m= Model("Rig")
# Create variables with nonnegativity constraints
x = m.addVars(33,3, name="x", vtype=GRB.BINARY)

# Set objective: 
#m.setObjective(quicksum(x[i,1]*scenario1[i] for i in range(33)), GRB.MAXIMIZE)
m.setObjective(quicksum(x[i,1]*dist1[i] for i in range(33)) + quicksum(x[i,1]*dist2[i] for i in range(33)) + quicksum(x[i,1]*dist3[i] for i in range(33)), GRB.MAXIMIZE)

# Add constraints: 
m.addConstr(quicksum(x[i,0]*scenario3[i] for i in range(33)) >=12000)
m.addConstr(quicksum(x[i,1]*scenario3[i] for i in range(33)) >=12000)
m.addConstr(quicksum(x[i,2]*scenario3[i] for i in range(33)) >=12000)
m.addConstrs(quicksum(x[i,j]for i in range(33)) >=1 for j in range(3))
m.addConstrs(x[i,0]+x[i,1]+x[i,2] == 1 for i in range(33))
m.addConstr(x[28,0]==x[30,0])
m.addConstr(x[28,1]==x[30,1])
m.addConstr(x[28,2]==x[30,2])
m.addConstr(x[27,2] + x[8,2] == 1)
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