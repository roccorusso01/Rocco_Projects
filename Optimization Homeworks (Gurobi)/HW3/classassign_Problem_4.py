from gurobipy import *
import csv


# Create a new model
m = Model("SCHOOOL")
# Create variables with nonnegativity constraints
x = m.addVars(40, 2, vtype = GRB.BINARY, name="x")
with open('ClassAssignments.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        valList = [row for row in spamreader]
valList = valList[1:]
studentNumber = [row[0] for row in valList]
c1Pref = [int(row[1]) - 1 for row in valList]
c2Pref = [int(row[2]) - 1 for row in valList]
gender = [row[3] for row in valList]
print(c2Pref)
print(gender[:23])
# Set objective: 
m.setObjective(sum([pref * x[index,0] for index, pref in enumerate(c1Pref)]) + sum([pref2 * x[index2,1] for index2, pref2 in enumerate(c2Pref)]), GRB.MINIMIZE)

# Add constraints:
m.addConstrs(x[i,0]+x[i,1] == 1 for i in range(40))
m.addConstr(sum([x[int(ind) - 1, 0] for ind in studentNumber]) == 20)
m.addConstr(sum([x[int(ind) - 1, 1] for ind in studentNumber]) == 20)
m.addConstr(sum([x[int(ind) - 1, 0] for ind in studentNumber[:23]]) <= 12)
m.addConstr(sum([x[int(ind) - 1, 1] for ind in studentNumber[:23]]) <= 12)
m.addConstr(x[9, 0] + x[10, 0] == 1)
m.addConstr(x[9, 1] + x[10, 1] == 1)
m.addConstr(x[3, 0] + x[8, 0] + x[14, 0] + x[24, 0] + x[29, 0] + x[35, 0] >= 2)
m.addConstr(x[3, 1] + x[8, 1] + x[14, 1] + x[24, 1] + x[29, 1] + x[35, 1] >= 2)
m.addConstr(x[19,0] == x[20, 0])
m.addConstr(x[19,1] == x[20, 1])
m.addConstr(x[0, 1] == 1)
m.addConstr(x[39, 1] == 1)


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