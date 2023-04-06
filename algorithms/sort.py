A = [1,5,3,45,34,32]

lenA = len(A)
for i in range(lenA):
 for j in range((lenA-1)):
  if A[i] > A[j]:
     tmp=A[i]
     A [i] = A[j]
     A[j]=tmp
print(A)

def quicksort(X):
    if len(X) <= 1:
        return X
    middle = X[(len(X)//2)]
    
    
    left, equal, right = [], [], []

    for num in X:
        if num < middle:
            left.append(num)
        elif num == middle:
            equal.append(num)
        else:
            right.append(num)

    return quicksort(left) + equal + quicksort(right)


B = quicksort([1,5,3,45,34,32])
print(B)