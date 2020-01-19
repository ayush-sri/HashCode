#implement the function for pizza 
def fun(inp):
	limit,variety=map(int,inp[0].rstrip('\n').split())
	inp_pizza=list(map(int,inp[1].split()))
	assert inp_pizza.__len__()==variety,'The variety of pizza cannot exceed the input variety'
	dic=dict()
	j=inp_pizza.__len__()-1
	while(j>=0):
		lis=[]
		i=j
		while(i>=0):
			if (inp_pizza[i]+sum(lis))<=limit:
				lis.append(inp_pizza[i])
			i-=1
		dic[sum(lis)]=lis[::-1]
		j-=1
	return dic,[inp_pizza.index(i) for i in dic[max(dic.keys())]].__len__(),[inp_pizza.index(i) for i in dic[max(dic.keys())]]


