import math
import numpy as np

NodesCondition = []
ForcesCondition = []
def UBoundaryCondition(nU,u,i):
    nU[i][0] = u
    NodesCondition.append(i)

def FBoundaryCondition(nF,f,i):
    nF[i][0] = f
    ForcesCondition.append(i)
    
def AssemblyStiffness(nStiffnessMatrix,k,i,j):
    nStiffnessMatrix[i][i] += k
    nStiffnessMatrix[i][j] += -k
    nStiffnessMatrix[j][i] += -k
    nStiffnessMatrix[j][j] += k
def Initialize(nStiffnessMatrix,nU,nF):
    for i in range(0,Nodes):
        nU[i][0] = math.pi
        nF[i][0] = math.pi
    for i in range(0,NumberOfElement):
        AssemblyStiffness(nStiffnessMatrix,K[i][0],K[i][1],K[i][2])
def PreSolvingStiffness(nStiffnessMatrix):
    nsize = Nodes-len(NodesCondition)
    newStiffness = np.zeros((nsize,nsize))
    contr = -1
    for i in range(0,Nodes):
        contc = -1
        flagr = False
        for k in range(0,len(NodesCondition)):
            if(i == NodesCondition[k]):
                flagr = True
                break
        if(flagr):
            continue
        contr += 1
        for j in range(0,Nodes):
            flagc = False
            for k in range(0,len(NodesCondition)):
                if(j == NodesCondition[k]):
                    flagc = True
                    break
            if(flagc):
                continue
            contc += 1
            newStiffness[contr][contc] = nStiffnessMatrix[i][j]
    return newStiffness

def PreSolvingF(nF):
    nsize = Nodes-len(NodesCondition)
    newF = np.zeros(nsize).reshape(nsize,1)
    contr = -1
    for i in range(0,Nodes):
        flagr = False
        for k in range(0,len(NodesCondition)):
            if(i == k):
                flagr = True
                break
        if(flagr):
            continue
        contr += 1
        newF[contr][0] = nF[i][0]
    return newF
                      

def Solve(nStiffnessMatrix,nU,nF):
    newStiffness = PreSolvingStiffness(nStiffnessMatrix)
    newF = PreSolvingF(nF)
    u = np.linalg.solve(newStiffness,newF)
    contr = -1
    for i in range(0,Nodes):
        flagr = False
        for k in range(0,len(NodesCondition)):
            if(i == k):
                flagr = True
                break
        if(flagr):
            continue
        contr += 1
        nU[i][0] = u[contr][0]
    nnF = np.matmul(StiffnessMatrix,nU)
    for i in range(0,len(ForcesCondition)):
        nnF[ForcesCondition[i]][0] = nF[ForcesCondition[i]][0]
    
    return nU,nnF

NodesCondition = []
Nodes = 5
K = np.array([[120,0,2],[120,2,4],[120,2,4],[120,2,3],[120,4,3],[120,3,1]])
NumberOfElement = len(K)

StiffnessMatrix = np.zeros((Nodes,Nodes))
U = np.zeros(Nodes).reshape(Nodes,1)
F = np.zeros(Nodes).reshape(Nodes,1)


Initialize(StiffnessMatrix,U,F)
UBoundaryCondition(U,0,0)
UBoundaryCondition(U,0,1)
FBoundaryCondition(F,0,2)
FBoundaryCondition(F,0,3)
FBoundaryCondition(F,20,4)

U,F=Solve(StiffnessMatrix,U,F)

print("Stiffness Matrix:\n",StiffnessMatrix,'\n')
print("Displacements:\n",U,'\n')
print("Forces:\n",F)
