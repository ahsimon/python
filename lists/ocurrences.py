N= input()
lenght = len(N)
counter=0
result=[]
char=N[0]
for x in range(lenght): 
    if N[x] == char:
       counter+=1
    if N[x] !=char:
        result.append([counter,int(char)])
        counter=1  
    if x == (lenght -1):
       result.append([counter,int(N[x])])              
    char=N[x]    
print(*[(k[0], k[1]) for k in result])