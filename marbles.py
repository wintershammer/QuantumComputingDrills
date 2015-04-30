import operator
import pprint

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


def boolMatrixSqr(m):
    msquared = [[0 for i in range(len(m))] for j in range(len(m))] #remeber: its always a square matrix
    for i in range(len(m)):
        for j in range(len(m)):
            accum = 0
            for k in range(0,len(m)):
                accum = accum or (m[i][k] and m[k][j])
            msquared[i][j] = accum
    return msquared

def boolMatrixMult(m1,m2):
    mk = [[0 for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            accum = 0
            for k in range(0,len(m1)):
                accum = accum or (m1[i][k] and m2[k][j])
            mk[i][j] = accum
    return mk


def boolMatrixExp(n,m):
    newM = m
    for i in range(n):
        newM = boolMatrixMult(newM,m)
    return newM
        


def marbles(v,m,steps):
    mAfter = boolMatrixExp(steps-1,m)
    return applySteps(v,mAfter)

    


########### Figure 3.3 ################

boolAdjM = [[0 for i in range(6)] for j in range(6)]

boolAdjM[5][0] = 1
boolAdjM[2][1] = 1
boolAdjM[4][2] = 1
boolAdjM[3][3] = 1
boolAdjM[5][4] = 1
boolAdjM[2][5] = 1

stateV = [6,2,1,5,3,10]

print("\nState of System 3.3 after 1 step:")
pprint.pprint(marbles(stateV,boolAdjM,1))

print("\nState of System 3.3 after 2 steps:")
pprint.pprint(marbles(stateV,boolAdjM,2))

print("\nState of System 3.3 after 3 steps:")
pprint.pprint(marbles(stateV,boolAdjM,3))



########### Figure 3.12 ################
boolAdjM = [[0 for i in range(9)] for j in range(9)]

boolAdjM[0][1] = 1
boolAdjM[1][0] = 1
boolAdjM[3][3] = 1
boolAdjM[5][2] = 1
boolAdjM[8][5] = 1
boolAdjM[8][8] = 1
boolAdjM[8][7] = 1
boolAdjM[7][4] = 1
boolAdjM[7][6] = 1


stateV = [1,1,1,1,1,1,1,1,1]

print("\nState of System 3.12 after one step:")
pprint.pprint(marbles(stateV,boolAdjM,1)) # 0 and 1 exchange their marbles, 3 just stays the same  and everything else accumulates to 8
print("\nState of System 3.12 after two steps:")
pprint.pprint(marbles(stateV,boolAdjM,2))

