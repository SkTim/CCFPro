#copyright: LHY
#static the weight of each keyword

for i in range(33):
    
    regressionLib = []
    keywords = []


    sourceFile = "../data/keyword_lib/" + str(i + 1) + ".txt"
    destinationFile = "../data/regression_lib/" + str(i + 1)
    ifHandle = open(sourceFile,'r')
    ofHandle = open(destinationFile,'w')

    indata = ifHandle.readlines()

    for j in range(len(indata)):
	li = indata[j].split(' ')
	for k in range(len(li)):
	    if li[k] != '\r\n' and li[k] != ' ':
		if li[k] in keywords:
		    regressionLib[keywords.index(li[k])] += 1
		if not li[k] in keywords:
		    keywords.append(li[k])
		    regressionLib.append(1)
		    #regressLib[keywords.index(li[k])] = 1
    
    print i
    for j in range(len(keywords)):
	ofHandle.write(keywords[j] + ' ' + str(regressionLib[j]) + '\n')

    ifHandle.close()
    ofHandle.close()

