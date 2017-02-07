import csv
from functions import *

if __name__=='__main__':

	file = open('../movielens/u.data', 'rb')
	data = csv.reader(file, delimiter='\t')
	f=open("myfile","w")
	t = [row for row in data]

	fDomainDict,sDomainDict={},{}
	fDomainDict=loadMovieLens('../movielens','/u1.base')
	sDomainDict=loadMovieLens('../movielens','/u2.base')
	fDomainTest =loadMovieLens('../movielens','/u1.test')
	
	no=50;
	while no<=943:
		sumAccuracy=0
		lenCount=0
		for user in fDomainTest:
			pred = getRecommendations(fDomainDict,sDomainDict,user,no)
			count=-1
			preds={}
			for rating,item in pred:
				preds[item]=rating
				# print movies[item],rating,item
			accuracies=[]
			for movie in fDomainTest[user]:
				if not movie in preds:continue 
				actualRating = fDomainTest[user][movie]
				predcitedRating = preds[movie]
				mae = fabs((predcitedRating - actualRating))
				accuracies.append(mae)
			lenCount+=1
			#print (sum(accuracies)/len(accuracies))
			sumAccuracy+=(sum(accuracies)/(len(accuracies)+1))
		
		print 'Mean Absolute Error'
		print float(sumAccuracy)/lenCount
		f.write("%d %f\n" %(no,sumAccuracy/lenCount))
		no=no+50
