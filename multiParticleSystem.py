import numpy as np
import math



def multiSystem(states):
    #remember: tensor/kronecker product is associative!
    compositeState = states[0]
    for state in states[1:]:
       compositeState =  np.kron(compositeState,state)
    return compositeState

def printTwoCompo(composite): #just testing
    ai = 0
    je = 0
    for i in range(len(composite)):
        if je > math.sqrt(len(composite)-1):
           je = 0
           ai += 1
        print(('c{}{} : {}').format(ai,je,composite[i]))
        print("P:",np.absolute(composite[i])**2/np.linalg.norm(composite)**2)
        je += 1
        
                        


stateA = np.array([1,0,0,0])
stateB = np.array([0,0,0,1])

example = np.array([1,1,1,1]) #example page 134


a = multiSystem([stateA,stateB])

printTwoCompo(example)
