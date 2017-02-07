import csv
from functions import *
from matrixFactorization import *
import numpy as np

if __name__=='__main__':
	prefs=loadMovieLens('../movielens','/u1.base')
	testprefs=loadMovieLens('../movielens','/u1.test')	

	#print(R)
	R=[[0 for i in xrange(1682)]for j in xrange(943)]
	
	R=np.array(R)
	#print(R)
	for i in xrange(943):
		for j in xrange(1682):
			if str(i+1) in prefs:
				if str(j+1) in prefs[str(i+1)]:
					R[i][j]=prefs[str(i+1)][str(j+1)]

				else:
					R[i][j]=0
			
	print(R)				
	N = len(R)
	M = len(R[0])
	K = 10

	P = np.random.rand(N,K)
	Q = np.random.rand(M,K)

	nP, nQ = matrix_factorization(R, P, Q, K)
	nR = np.dot(nP, nQ.T)

	total_err=[]
	for i in xrange(943):
		for j in xrange(1682):
			if str(i+1) in testprefs:
				if str(j+1) in testprefs[str(i+1)]:
					total_err.append(fabs(nR[i][j]-testprefs[str(i+1)][str(j+1)]))

			

	print("P:",nP)
	print("Q:",nQ)
	print("R^:",nR)
	print("MAE=%f" %(sum(total_err)/len(total_err)))		