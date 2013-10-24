inHandle = open('../data/keyword_class.txt','r')
inData = inHandle.readlines()
outHandle = []

for i in range(33):
    a = open('../data/class/' + str(i + 1),'w')
    outHandle.append(a)

for line in inData:
    if line[-2] != '-':
	if line[-3] == ' ':
	    t_list = line.split('\t')
	    _s = t_list[0]
	    outHandle[int(line[-2]) - 1].write(_s + '\n')
	if line[-3] != ' ':
	    t_list = line.split('\t')
	    _s = t_list[0]
	    outHandle[int(line[-3] + line[-2]) - 1].write(_s + '\n')

for i in range(33):
    outHandle[i].close()

inHandle.close()
#outHandle.close()
