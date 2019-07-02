import sys
import system_handler as sysHandle


def clean_string(sinput):
	soutput = sinput
	opening_special_characters = ('"', "'", '—')
	if soutput.startswith(opening_special_characters):
			soutput = soutput[1:]

	ending_special_characters = ('"', "'",  '-', '—')
	if soutput.endswith(ending_special_characters):
		soutput =  soutput[:-1]
	
	return soutput

def get_right_side(input_string):
	opening_special_characters = ('(', '[', '{', '“', '‘')
	result = input_string	
	for substr in opening_special_characters:
		if substr in result:
			temp = result.split(substr)
			result = temp[1]
	return result

def get_left_side(input_string):
	ending_special_characters = ("'s'",'/',']', '}', ')', '.', '’', '”', '…', ':', ';',',', '?', '!')
	result = input_string	
	for substr in ending_special_characters:
		if substr in result:
			temp = result.split(substr)
			result = temp[0]
	return result

def without_numbers(str):
    return not any(ch.isdigit() for ch in str)



def cleanWordList(inputlist):
	result = inputlist
	result = list(map(get_right_side, result))
	result = list(map(get_left_side, result))
	result = list(map(clean_string, result))
	result = list(filter(without_numbers, result))
	result = list( dict.fromkeys(result))
	result.sort()
	return result

def filter_list(list1):

	list2 = list(filter(lambda s: s.islower(), list1))
	list3 =  [item for item in list1 if item not in list2]
	return(list2, list3)



def processText(pathIn, dirOut):
	pathOut = sysHandle.getRawPath(pathIn, dirOut)
	#print('pathOut', pathOut)
	#output_path = getNormalPath(path1, path2)
	#STEP 1: read data file and split to get words
	words = sysHandle.getWordFromTextFile(pathIn)

	#STEP 2: trim left, right, remove overlappings and sort
	wordList = cleanWordList(words)

	#STEP 3: remove items found in exclusion list, remove empty string
	exclusion = sysHandle.openExclusionList()
	cleanList = [w for w in wordList if w.lower() not in exclusion]
	cleanList = [w for w in cleanList if w]

	#print(cleanList)
	sysHandle.writeListToFile(cleanList, pathOut)
	sysHandle.openDir(dirOut)
	sys.exit()
