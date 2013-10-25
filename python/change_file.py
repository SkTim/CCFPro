#copyright: LHY
#edit it to establish knowledge lib

for i in range(33):
    ofn = str(i+1)+str(i+1)+'.txt'
    nfn = str(i+1)+'.txt'
    a = open(ofn,'r')
    b = open(nfn,'w')
    ind = a.readlines()
    for i in ind:
	b.write(i.decode('gb2312').encode('utf-8'))



