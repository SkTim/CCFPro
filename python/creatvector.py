routeR = "../data/regression_lib/"
routeD = "../data/wordVector"

dictionary = []
vectorList = []
outHandle = open(routeD,'w')

for i in range(33):
    infile = routeR + str(i + 1) + ".sorted"
    inHandle = open(infile,'r')
    inList = inHandle.readlines()
    for j in range(len(inList)):
	t_dataList = inList[j].split('\n')
	dataList = t_dataList[0].split(' ')

	if len(dataList) != 2:
	    continue
	word = dataList[0]
	weight = dataList[1]
        if word in dictionary:
	    vectorList[dictionary.index(word)][i] = weight
	if not word in dictionary:
	    dictionary.append(word)
	    vector = []
	    for k in range(33):
		vector.append(0)
	    vector[i] = weight
	    vectorList.append(vector)

    print i + 1
    inHandle.close()

print "word number = ",len(vectorList)

for i in range(len(vectorList)):

    print i
    outHandle.write(dictionary[i] + ' ')
    for j in range(len(vectorList[i])):
	outHandle.write(str(vectorList[i][j]) + ' ')
    outHandle.write('\n')

outHandle.close()
	

	

