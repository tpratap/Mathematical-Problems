# Simplex Method in Linear Programming Solution using Python 
import numpy as np 
from fractions import Fraction as f  
M = int(input("Enter the number of  equations:"))

print("Enter the maximizing equation coefficient separated by space:(Ax + By): ")
Xj=list(map(float,input().split()))
print(Xj)
for i in range(M):
    Xj.insert(i,float(0))
print(Xj)    

B=list()
matrix=list()
cb=list()  
print("Enter the equations coefficient separated by space:(Ax + By >= C): ")
for i in range(M):
    print("A B C ")
    entries=list(map(float,input().split()))
    matrix.append(entries)
A =np.array(matrix)
# c will contain coefficients of objective function Z       
for i in range(M):
    cb.append(0)
    B.append(i)
cb= np.array(cb)
cb=np.transpose([cb])

c= np.array(Xj)
c=np.transpose([c])
# B will contain the basic variables that make identity matrix  
B = np.array(B)
B=np.transpose([B])
 # cb contains their corresponding coefficients in Z                               
# combine matrices B and cb 
table = np.hstack((B, cb))

# combine matrices B, cb and xb 
# finally combine matrix A to form the complete simplex table
slack=np.identity(M)
table=np.append(table,slack,axis=1)
table = np.hstack((table, A))          
# change the type of table to float 
table = np.array(table, dtype ='float')

itr=0
v=""
for i in range(2,M):
        v=v+("\tx" +str(i+3))
print("Table before iteration: ") 
print("B \tCB \tx1 \tx2"+v+" \tx \ty \tRHS")
i=0
for row in table:
    for el in row:
        if i%(M+5)== 0:
            print('x'+str(int(el)+1), end ='\t')
        else:
            print(f(str(el)).limit_denominator(100), end ='\t')
        i=i+1
    print() 
print() 
    
while True:
    i=0
    Cj_Zj=[]
    theta=[]
    while i<len(Xj):
        Cj_Zj.append(Xj[i] - np.sum(table[:, 1]*table[:, 2 + i]))
        i = i + 1 

    print("Cj-Zj \t\t: ",Cj_Zj)
    if max(Cj_Zj)<=0:
        break
    ind=Cj_Zj.index(max(Cj_Zj))+2
    for i in range(M):
        theta.append((table[i,4+M]/table[i,ind]))
        if theta[i]<0:
            theta[i]=99999
    print("theta \t\t: ",theta)    
    jnd=theta.index(min(theta))
    pivot=table[jnd,ind]
    table[jnd, 2:M+5] = table[jnd, 2:M+5] / pivot
    i=0
    while i<M:
        if i != jnd:
            table[i, 2:M+5] = table[i,2:M+5] - table[i][ind]*table[jnd][2:M+5]
        i=i+1
    #assign the new basic variable 
    table[jnd][0] = ind-2 
    table[jnd][1] = Xj[ind-2]
    print() 
    print() 
    itr+= 1
    print(ind,jnd)
    print("Table at iteration: "+str(itr)) 
    print("B \tCB \tx1 \tx2"+v+"\tx \ty \tRHS")
    i=0
    for row in table: 
        for el in row:
            if i%(M+5)== 0:
                print('x'+str(int(el)+1), end ='\t')
            else:
                print(f(str(el)).limit_denominator(100), end ='\t')
            i=i+1
        print() 
    print()
print()
Z= np.sum(table[:, 1]*table[:,M+4])
print("Z=",Z)

  
        
  
