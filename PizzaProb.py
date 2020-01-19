def hash(inp):
    limit,variety=map(int,inp[0].rstrip('\n').split())
    inp_pizza=list(map(int,inp[1].rstrip('\n').split()))
    #print(limit) 
    assert inp_pizza.__len__() == variety, 'The variety of pizza cannot exceed the input variety'
    dic = dict()
    j = inp_pizza.__len__()-1
    while(j>=0):
        lis = []
        i = j
        while(i>=0):
            if (inp_pizza[i]+sum(lis)) <= limit:
                lis.append(inp_pizza[i])
            i-=1
        dic[sum(lis)] = lis[::-1]
        j-=1
    return [inp_pizza.index(i) for i in dic[max(dic.keys())]].__len__(), [inp_pizza.index(i) for i in dic[max(dic.keys())]]

if __name__=='__main__':
    name=input()
    try:
        with open(name,'r') as file:
            inp = file.readlines()
            l,ind=hash(inp)
            #print(sum(d[max(d.keys())]))
            #print(max(d.keys())) 
            #return the dic from the hash function and then read it in a vraible named d in line no 22
            with open(file.name.split('\\')[::-1][0][0]+'_out.in', 'w') as file2:
                file2.writelines([str(l), '\n', ' '.join(list(map(str, ind)))])
    except FileNotFoundError as e:
        raise FileNotFoundError('File is not present')
    
        
        
        
        
            
        
        
        
        
        
        
    
