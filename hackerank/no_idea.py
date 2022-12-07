
if __name__== '__main__':


    outFile = open("no_idea.out",'w')
    inFile =  open("no_idea.txt",'r',newline='\n',encoding='utf8')
    happiness=0     
    
    lNM=inFile.readline().split()
    n = int(lNM[0])
    m = int(lNM[1])


    N=inFile.readline().split()
    A=inFile.readline().split()
    B= inFile.readline().split()
    lN = [int(x) for x in N]
    lA = set([int(x) for x in A])
    lB = set([int(x) for x in B])  
    
    for x in lN:
        if x in lA :
            happiness+=1          
        if x in lB:
            happiness-=1  
    print(happiness)


        