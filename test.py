wordList = ['A', 'B']
exclusionList = ['a']


cleanList = [w for w in wordList if w.lower() not in exclusionList]

print(cleanList)