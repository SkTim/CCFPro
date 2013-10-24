inHandle = open('../data/keyword_class.txt','r')
outHandle = open('../data/originData','w')

inData = inHandle.readlines()

for line in inData:
    if line[-2] != '-':
	outHandle.write(line)

inHandle.close()
outHandle.close()
