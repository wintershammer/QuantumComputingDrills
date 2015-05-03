import numpy as np
import math
import pprint
import quantumMarbles

startState = np.array([3,1-2j])
endState = np.array([1,0])




def probAtXi(superpos,i):
    return np.absolute(superpos[i])**2/np.linalg.norm(superpos)**2



def braket(start,end):
    a = (np.dot(end.conj().T,start)) #compute inner product
    return a/(np.linalg.norm(start)*np.linalg.norm(end)) #normalised

def observation(observable,state):
    a = np.linalg.norm(braket(state,np.linalg.eig(obsv)[1][0]))
    b = np.linalg.norm(braket(state,np.linalg.eig(obsv)[1][1]))
    print("Eigenvalues of the observable: ",np.linalg.eigvals(obsv))
    print("Probabilities of transition to eigenstates:",a**2,b**2)
    return (a**2,b**2)

def dynamics(state,uSeq):
    newState = state
    for uniMat in uSeq:
        newState = np.dot(newState,uniMat)
    for i in range(len(newState)):
        print ('State[{}]: {}'.format(i, newState[i]),"|",('P(State[{}]): {}'.format(i, probAtXi(newState,i))))  
    return newState

a = braket(startState,endState)

#print("Transition amplitude from :",startState,"to",endState)
#print(a)
#print(abs(a)**2)
#print("Probability of :",startState,"to be found at Xi",endState)
#print(probAtXi(startState,0))

#obsv = np.array([[-1,-1j],[1j,1]])
#state = np.array([1/2,1/2])
#
#observation(obsv,state)

#vS = np.array([1,0,0,0])
#ad = np.array([[0,1/math.sqrt(2),1/math.sqrt(2),0],[1j/math.sqrt(2),0,0,1/math.sqrt(2)],[1/math.sqrt(2),0,0,1j/math.sqrt(2)],[0,1/math.sqrt(2),-1/math.sqrt(2),0]])

#stateTransitions = [ad,ad,ad,ad]

#b = dynamics(vS,stateTransitions)




