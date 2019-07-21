import os, sys
import system_handler as sysHandle
from mysql_data import getWordList


def convertList(rawList):
	arr = rawList.split('\n')
	return arr


def filterList(rawList, dictList):

	listClear = [item for item in rawList if item.lower() in dictList]
	listTrash =  [item for item in rawList if item not in listClear]
	return(listClear, listTrash)

def splitDictByCase(list1):

	list2 = list(filter(lambda s: s.islower(), list1))
	list3 =  [item for item in list1 if item not in list2]
	return(list2, list3)	

def processText(inFile, outDir, dictDir, trashDir, logDir, recycleDir):
	#print ('logDir:', logDir, 'recyle Dir:', recycleDir)

	
	#print ('recycleList:', recycleList)

	initialString = "Dictionary_Check_Log_"
	pathLog = sysHandle.getDatedFilePath(initialString, logDir)
	logData = []
	dateStamp = sysHandle.getDateStamp()
	message = "Starting to directionary-check at " + dateStamp
	logData.append(message)
	print(message)

	
	pathOutClean = sysHandle.getRawPath(inFile, outDir)
	pathOutTrash = sysHandle.getRawPath(inFile, trashDir)
	#print ('path clean:', pathOutClean, 'path trash:', pathOutTrash)
	rawList = convertList(sysHandle.readTextFile(inFile))
	dicList = sysHandle.loadDictionaries(dictDir)

	#split clean and trash based on dictionary
	listClean, listTrash = filterList(rawList, dicList)

	#split into lower case and upper case parts
	lowerClean, upperClean = splitDictByCase(listClean)

	#get a list of words from mysql database	
	lowerDic, upperDic = splitDictByCase(getWordList())	

	#logging activity
	dateStamp = sysHandle.getDateStamp()
	message = "Loading dictionary completed at " + dateStamp
	logData.append(message)
	print(message)	


	newUpperClean = [item for item in upperClean if item.lower() not in lowerDic]

	newClean = newUpperClean + lowerClean

	#logging activity
	dateStamp = sysHandle.getDateStamp()
	message = "Completed dictionary checking at " + dateStamp
	logData.append(message)
	print(message)	

	recycleList = sysHandle.loadDictionaries(recycleDir)
	newListTrash = [item for item in listTrash if item not in recycleList]

	sysHandle.writeListToFile(newClean, pathOutClean)
	sysHandle.writeListToFile(newListTrash, pathOutTrash)

	#logging activity
	dateStamp = sysHandle.getDateStamp()
	message = "Finished directionary checking at " + dateStamp
	logData.append(message)
	print(message)
	sysHandle.writeListToFile(logData, pathLog)

	sysHandle.openDir(outDir)
	sys.exit()

