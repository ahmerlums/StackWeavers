import os
import sys



if os.path.exists(str(sys.argv[1])): #Checking for Valid Path
	dirList = os.listdir(str(sys.argv[1]))
	print dirList

	topicsDictionary = {} 
	for i in dirList:
		temp = i.split('-') #To match Format
		
		if len(temp) == 3:

			print i
			

             #Separation based on format
			courseName = temp[0][:-1]
			topic = temp[1][1:-1]
			lecture = temp[2][1:] 

			#This would be unique
			key = courseName + " - " + topic

			#Maintaining a dictionary of number of files in each topic. Need to increment everytime when new Lecture is found.
			if key in topicsDictionary.keys():
				temp = 'downloads/'+courseName+'/'+ str(topicsDictionary[key])+ " - " +topic
				topicsDictionary[key] = topicsDictionary[key] + 1

			else:
				temp = 'downloads/'+courseName+'/ 1 - ' +topic
				topicsDictionary[key] = 1

			
			

			
			if not os.path.exists(temp):
				os.makedirs(temp)

				#Renaming the Directory as now a new File has been added. So the Count goes up.
			os.rename(temp,'downloads/'+courseName+'/'+ str(topicsDictionary[key])+ " - " +topic)	

			#Moving the File to its folder
			source = 'downloads/'+i
			dest = 'downloads/'+courseName+'/'+ str(topicsDictionary[key])+ " - " +topic+ '/' +lecture

			
			os.rename(source,dest)