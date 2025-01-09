from gurobipy import * 
import pandas as pd 
import random 
df = pd.read_csv('March Madness.csv', index_col=0) 
p1 = [df.iloc[i,i+1] if i%2==0 else df.iloc[i,i-1] for i in range(64)] 

p2 = [p1[i]*(p1[i+2]*df.iloc[i,i+2]+p1[i+3]*df.iloc[i,i+3]) if i%4 ==0 else 
p1[i]*(p1[i+1]*df.iloc[i,i+1]+p1[i+2]*df.iloc[i,i+2]) if i%4 ==1 else 

p1[i]*(p1[i-1]*df.iloc[i,i-1]+p1[i-2]*df.iloc[i,i-2]) if i%4 ==2 else 
p1[i]*(p1[i-2]*df.iloc[i,i-2]+p1[i-3]*df.iloc[i,i-3]) for i in range(64)] 

p3=[p2[i]*(p2[i+4]*df.iloc[i,i+4]+p2[i+5]*df.iloc[i,i+5]+p2[i+6]*df.iloc[i,i+6]+p2[ 
i+7]*df.iloc[i,i+7]) if i%8 ==0 else 

p2[i]*(p2[i+3]*df.iloc[i,i+3]+p2[i+4]*df.iloc[i,i+4]+p2[i+5]*df.iloc[i,i+5]+p2[i+6] 
*df.iloc[i,i+6]) if i%8 ==1 else 

p2[i]*(p2[i+2]*df.iloc[i,i+2]+p2[i+3]*df.iloc[i,i+3]+p2[i+4]*df.iloc[i,i+4]+p2[i+5] 
*df.iloc[i,i+5]) if i%8 ==2 else 

p2[i]*(p2[i+1]*df.iloc[i,i+1]+p2[i+2]*df.iloc[i,i+2]+p2[i+3]*df.iloc[i,i+3]+p2[i+4] 
*df.iloc[i,i+4]) if i%8 ==3 else 

p2[i]*(p2[i-7]*df.iloc[i,i-7]+p2[i-6]*df.iloc[i,i-6]+p2[i-5]*df.iloc[i,i5]+
p2[i-4]*df.iloc[i,i-4]) if i%8 ==7 else 

p2[i]*(p2[i-6]*df.iloc[i,i-6]+p2[i-5]*df.iloc[i,i-5]+p2[i-4]*df.iloc[i,i4]+
p2[i-3]*df.iloc[i,i-3]) if i%8 ==6 else 

p2[i]*(p2[i-5]*df.iloc[i,i-5]+p2[i-4]*df.iloc[i,i-4]+p2[i-3]*df.iloc[i,i3]+
p2[i-2]*df.iloc[i,i-2]) if i%8 ==5 else 

p2[i]*(p2[i-4]*df.iloc[i,i-4]+p2[i-3]*df.iloc[i,i-3]+p2[i-2]*df.iloc[i,i2]+
p2[i-1]*df.iloc[i,i-1]) for i in range(64)] 

p4=[p3[i]*(p3[i+8]*df.iloc[i,i+8]+p3[i+9]*df.iloc[i,i+9]+p3[i+10]*df.iloc[i,i+10]+p 
3[i+11]*df.iloc[i,i+11] + 
p3[i+12]*df.iloc[i,i+12]+p3[i+13]*df.iloc[i,i+13]+p3[i+14]*df.iloc[i,i+14]+p3[i+15] 
*df.iloc[i,i+15]) if i%16 ==0 else 

p3[i]*(p3[i+7]*df.iloc[i,i+7]+p3[i+8]*df.iloc[i,i+8]+p3[i+9]*df.iloc[i,i+9]+p3[i+10 
]*df.iloc[i,i+10] + 
p3[i+11]*df.iloc[i,i+11]+p3[i+12]*df.iloc[i,i+12]+p3[i+13]*df.iloc[i,i+13]+p3[i+14] 
*df.iloc[i,i+14] )if i%16 ==1 else 

p3[i]*(p3[i+6]*df.iloc[i,i+6]+p3[i+7]*df.iloc[i,i+7]+p3[i+8]*df.iloc[i,i+8]+p3[i+9] 
*df.iloc[i,i+9] + p3[i+10]*df.iloc[i,i+10] + 
p3[i+11]*df.iloc[i,i+11]+p3[i+12]*df.iloc[i,i+12]+p3[i+13]*df.iloc[i,i+13] ) if i 
%16 ==2 else 

p3[i]*(p3[i+5]*df.iloc[i,i+5]+p3[i+6]*df.iloc[i,i+6]+p3[i+7]*df.iloc[i,i+7]+p3[i+8] 
*df.iloc[i,i+8]+p3[i+9]*df.iloc[i,i+9] + p3[i+10]*df.iloc[i,i+10] + 
p3[i+11]*df.iloc[i,i+11]+p3[i+12]*df.iloc[i,i+12]) if i%16 ==3 else 

p3[i]*(p3[i+4]*df.iloc[i,i+4]+p3[i+5]*df.iloc[i,i+5]+p3[i+6]*df.iloc[i,i+6]+p3[i+7] 
*df.iloc[i,i+7]+p3[i+8]*df.iloc[i,i+8]+p3[i+9]*df.iloc[i,i+9] + 
p3[i+10]*df.iloc[i,i+10] + p3[i+11]*df.iloc[i,i+11]) if i%16 ==4 else 

p3[i]*(p3[i+3]*df.iloc[i,i+3]+p3[i+4]*df.iloc[i,i+4]+p3[i+5]*df.iloc[i,i+5]+p3[i+6] 
*df.iloc[i,i+6]+p3[i+7]*df.iloc[i,i+7]+p3[i+8]*df.iloc[i,i+8]+p3[i+9]*df.iloc[i,i+9 
] + p3[i+10]*df.iloc[i,i+10]) if i%16 ==5 else 

p3[i]*(p3[i+2]*df.iloc[i,i+2]+p3[i+3]*df.iloc[i,i+3]+p3[i+4]*df.iloc[i,i+4]+p3[i+5] 


*df.iloc[i,i+5]+p3[i+6]*df.iloc[i,i+6]+p3[i+7]*df.iloc[i,i+7]+p3[i+8]*df.iloc[i,i+8 
]+p3[i+9]*df.iloc[i,i+9]) if i%16 ==6 else 

p3[i]*(p3[i+1]*df.iloc[i,i+1]+p3[i+2]*df.iloc[i,i+2]+p3[i+3]*df.iloc[i,i+3]+p3[i+4] 
*df.iloc[i,i+4]+p3[i+5]*df.iloc[i,i+5]+p3[i+6]*df.iloc[i,i+6]+p3[i+7]*df.iloc[i,i+7 
]+p3[i+8]*df.iloc[i,i+8]) if i%16 ==7 else 

p3[i]*(p3[i-1]*df.iloc[i,i-1]+p3[i-2]*df.iloc[i,i-2]+p3[i-3]*df.iloc[i,i3]+
p3[i-4]*df.iloc[i,i-4]+p3[i-5]*df.iloc[i,i-5]+p3[i-6]*df.iloc[i,i-6]+p3[i7]*
df.iloc[i,i-7]+p3[i-8]*df.iloc[i,i-8]) if i%16 ==8 else 

p3[i]*(p3[i-2]*df.iloc[i,i-2]+p3[i-3]*df.iloc[i,i-3]+p3[i-4]*df.iloc[i,i4]+
p3[i-5]*df.iloc[i,i-5]+p3[i-6]*df.iloc[i,i-6]+p3[i-7]*df.iloc[i,i-7]+p3[i8]*
df.iloc[i,i-8]+p3[i-9]*df.iloc[i,i-9])if i%16 ==9 else 

p3[i]*(p3[i-3]*df.iloc[i,i-3]+p3[i-4]*df.iloc[i,i-4]+p3[i-5]*df.iloc[i,i5]+
p3[i-6]*df.iloc[i,i-6]+p3[i-7]*df.iloc[i,i-7]+p3[i-8]*df.iloc[i,i-8]+p3[i9]*
df.iloc[i,i-9]+p3[i-10]*df.iloc[i,i-10]) if i%16 ==10 else 

p3[i]*(p3[i-4]*df.iloc[i,i-4]+p3[i-5]*df.iloc[i,i-5]+p3[i-6]*df.iloc[i,i6]+
p3[i-7]*df.iloc[i,i-7]+p3[i-8]*df.iloc[i,i-8]+p3[i-9]*df.iloc[i,i-9]+p3[i10]*
df.iloc[i,i-10]+p3[i-11]*df.iloc[i,i-11]) if i%16 ==11 else 

p3[i]*(p3[i-5]*df.iloc[i,i-5]+p3[i-6]*df.iloc[i,i-6]+p3[i-7]*df.iloc[i,i7]+
p3[i-8]*df.iloc[i,i-8]+p3[i-9]*df.iloc[i,i-9]+p3[i-10]*df.iloc[i,i-10]+p3[i11]*
df.iloc[i,i-11]+ p3[i-12]*df.iloc[i,i-12]) if i%16 ==12 else 

p3[i]*(p3[i-6]*df.iloc[i,i-6]+p3[i-7]*df.iloc[i,i-7]+p3[i-8]*df.iloc[i,i8]+
p3[i-9]*df.iloc[i,i-9]+p3[i-10]*df.iloc[i,i-10]+p3[i-11]*df.iloc[i,i-11]+ p3[i12]*
df.iloc[i,i-12]+p3[i-13]*df.iloc[i,i-13]) if i%16 ==13 else 

p3[i]*(p3[i-7]*df.iloc[i,i-7]+p3[i-8]*df.iloc[i,i-8]+p3[i-9]*df.iloc[i,i9]+
p3[i-10]*df.iloc[i,i-10]+p3[i-11]*df.iloc[i,i-11]+ p3[i-12]*df.iloc[i,i12]+
p3[i-13]*df.iloc[i,i-13]+p3[i-14]*df.iloc[i,i-14]) if i%16 ==14 else 

p3[i]*(p3[i-8]*df.iloc[i,i-8]+p3[i-9]*df.iloc[i,i-9]+p3[i-10]*df.iloc[i,i10]+
p3[i-11]*df.iloc[i,i-11]+ p3[i-12]*df.iloc[i,i-12]+p3[i-13]*df.iloc[i,i13]+
p3[i-14]*df.iloc[i,i-14]+p3[i-15]*df.iloc[i,i-15]) for i in range(64)] 

p5 = [p4[i]*((sum([p4[i+j]*df.iloc[i,(i+j)] for j in range(16 - i%16,32 - i%16)]))) 
if i%32 <= 15 else 

p4[i]*((sum([p4[i-k]*df.iloc[i,(i-k)] for k in range(16 - i%16 ,32 - i 
%16)])))for i in range(64)] 

p6 = [p5[i]*((sum([p5[i+j]*df.iloc[i,(i+j)] for j in range(32 - i%32,64 - i%32)]))) 
if i%64 <= 31 else 

p5[i]*((sum([p5[i-k]*df.iloc[i,(i-k)] for k in range(32 - i%32 ,64 - i 
%32)])))for i in range(64)] 
m= Model("mad") 
# Create variables with nonnegativity constraints 
x = m.addVars(64,6, name="x", vtype=GRB.BINARY) 

# Set objective: 
m.setObjective(quicksum(p1[i]*x[i,0]+2*(p2[i]*x[i,1])+4*(p3[i]*x[i,2]) 
+8*(p4[i]*x[i,3])+16*(p5[i]*x[i,4])+32*(p6[i]*x[i,5]) for i in range(64)), 
GRB.MAXIMIZE) 

# Add constraints: 
m.addConstrs(x[i,0]+x[i+1,0] == 1 for i in range(0,64, 2)) 
m.addConstrs(x[i,1]+x[i+1,1] +x[i+2,1]+x[i+3,1] == 1 for i in range(0, 64, 4)) 
m.addConstrs(x[i,2]+x[i+1,2] +x[i+2,2]+x[i+3,2] + x[i+4,2]+x[i+5,2] 
+x[i+6,2]+x[i+7,2]== 1 for i in range(0, 64, 8)) 
m.addConstrs(x[i,3]+x[i+1,3] +x[i+2,3]+x[i+3,3] + x[i+4,3]+x[i+5,3] 
+x[i+6,3]+x[i+7,3]+ 

x[i+8,3]+x[i+9,3] +x[i+10,3]+x[i+11,3] + x[i+12,3]+x[i+13,3] 
+x[i+14,3]+x[i+15,3]== 1 for i in range(0, 64, 16)) 
m.addConstr(quicksum(x[i,4]for i in range(32)) ==1) 


m.addConstr(quicksum(x[i,4]for i in range(32,64)) ==1) 
m.addConstr(quicksum(x[i,5]for i in range(64)) ==1) 
m.addConstrs(x[i,k]>=x[i,k+1]for i in range(64) for k in range(5)) 
m.addConstr(quicksum(x[2*i,1] for i in range(32)) <=11) 
m.addConstr(x[0,5]+x[16,5]+x[32,5]+x[48,5] <=1) 

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


