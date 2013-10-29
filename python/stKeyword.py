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

#	print 'j = ',j

	li = indata[j].split(' ')
	for k in range(len(li)):
	    if li[k] != '\r\n' and li[k] != ' ':
		if li[k] in keywords:

		    regressionLib[keywords.index(li[k])] += 1

#		    if(len(regressionLib) > 1):
#		    	t_a = regressionLib[keywords.index(li[k])]
#	                t_b = li[k]

#		        del regressionLib[keywords.index(li[k])]
#		        del keywords[keywords.index(li[k])]

 #  		        if t_a >= regressionLib[0]:
#		    	    regressionLib.insert(0,t_a)
#			    keywords.insert(0,t_b)

#			elif t_a <= regressionLib[-1]:
#			    regressionLib.append(t_a)
#			    keywords.append(t_b)

#			elif t_a < regressionLib[0] and t_a > regressionLib[-1]:
#			    for l in range(1,len(regressionLib) - 1):
#				if t_a >= regressionLib[l]:
#				    regressionLib.insert(l,t_a)
#				    keywords.insert(l,t_b)

		if not li[k] in keywords:
		    keywords.append(li[k])
		    regressionLib.append(1)

    for j in range(len(keywords)):
	ofHandle.write(keywords[j] + ' ' + str(regressionLib[j]) + '\n')
    
    print i

    ifHandle.close()
    ofHandle.close()

