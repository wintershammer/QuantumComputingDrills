import operator
import pprint
import math


def cvAddition(a,b):
    return list(map(operator.add,a,b))

def cvScalarMult(scalar,vector):
    return list(map(lambda v: v*scalar,vector))

def cvInverse(vector):
    return list(map(lambda x: -x,vector))


def applySteps(x,m):
    y= [0 for i in range(len(x))] #initialise y to a vector of length same as x
    accum = 0
    for i in range(len(y)):
        accum = 0
        for k in range(len(y)):
            accum += m[i][k] * x[k]
        y[i] = accum
    return y 



def matrixMult(m1,m2):
    mk = [[0 for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            accum = 0
            for k in range(0,len(m1)):
                accum += (m1[i][k] * m2[k][j])
                if (m1[i][k] != 0) and (m2[k][j] != 0):
                    if accum == 0:
                        print ('Interference at A[{}][{}]'.format(i, j))
            mk[i][j] = accum
    return mk



def matrixExp(n,m):
    newM = m
    for i in range(n):
        newM = matrixMult(newM,m)
    return newM
        


def doubleSlit(v,m,steps):
    mAfter = matrixExp(steps-1,m)
    return applySteps(v,mAfter)

    
def modSqr(m):
    modSqredM = [[0 for i in range(len(m))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range (len(m)):
            modSqredM[i][j] = abs(m[i][j])**2
    return modSqredM

def vectorModSqr(v):
    modSqredV = [0 for i in range(len(v))]
    for i in range (len(v)):
        modSqredV[i] = abs(v[i])**2         
    return modSqredV
    

adjMatrix = [[0 for i in range(8)] for j in range(8)]

adjMatrix[1][0] = 1/math.sqrt(2)
adjMatrix[2][0] = 1/math.sqrt(2)
adjMatrix[3][1] = (-1+1j)/math.sqrt(6)
adjMatrix[3][3] = 1
adjMatrix[4][1] = (-1-1j)/math.sqrt(6)
adjMatrix[4][4] = 1
adjMatrix[5][1] = (1-1j)/math.sqrt(6)
adjMatrix[5][2] = (-1+1j)/math.sqrt(6)
adjMatrix[5][5] = 1
adjMatrix[6][2] = (-1-1j)/math.sqrt(6)
adjMatrix[6][6] = 1
adjMatrix[7][2] = (1-1j)/math.sqrt(6)
adjMatrix[7][7] = 1

stateV = [1,0,0,0,0,0,0,0]


a = doubleSlit(stateV,adjMatrix,1)

print("Double slit experiment:")

print("State at start of experiment:",stateV,"(photon is at starting position State[0])")
print("Modulus squared of the adjecency matrix of this system:\n")
pprint.pprint(modSqr(adjMatrix))

print("\n\nState after one step\n\n",vectorModSqr(a))

print("\n\nState after two steps\n\n")
a = doubleSlit(stateV,adjMatrix,2)
print(vectorModSqr(a))
