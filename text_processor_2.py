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

def processText(inFile, outDir, dictDir, trashDir):
	#print ('input file:', inFile, 'output Dir:', outDir)
	#print ('dictionary:', dictDir, 'trash Dir:', trashDir)
	
	pathOutClean = sysHandle.getRawPath(inFile, outDir)
	pathOutTrash = sysHandle.getRawPath(inFile, trashDir)
	#print ('path clean:', pathOutClean, 'path trash:', pathOutTrash)
	rawList = convertList(sysHandle.readTextFile(inFile))
	dicList = sysHandle.loadDictionaries(dictDir)
	
	#split clean and trash based on dictionary
	listClean, listTrash = filterList(rawList, dicList)

	#get a list of words from mysql database
	
	lowerDic, upperDic = splitDictByCase(getWordList())
	#print(lowerDic)

	lowerClean, upperClean = splitDictByCase(listClean)

	newUpperClean = [item for item in upperClean if item.lower() not in lowerDic]

	newClean = newUpperClean + lowerClean

	sysHandle.writeListToFile(newClean, pathOutClean)
	sysHandle.writeListToFile(listTrash, pathOutTrash)

	sysHandle.openDir(outDir)
	sys.exit()

