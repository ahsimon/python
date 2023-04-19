
sortOrder=1
items= [["item1","1","1134"]
        ,["item2","8","90274"]
        ,["item3","4","33"]]

pageNumber=1
pageSize=2

sortedList =sorted(items, key=lambda x: x[1])
   
if sortOrder ==0: 
    sortedList.reverse()

pages = (len(items)/pageSize)
if (pages- int(pages)) > 0:
    pages +=1    

index0= pageSize * pageNumber
index1= index0 + pageSize
pageList=sortedList[index0:index1]
itemsList = [x[0] for x in pageList]

print(itemsList)


