A = []
n = int(input("Enter the number of students:-"))
for i in range(n):
    A.append(float(input("enter the percentage of students")))
print("Before sorting")
print(A)
def partition(start,end):
 
    pivot = A[end]
    pindex = start
    for i in range(start,end):
        if A[i] < pivot:
            A[i] , A[pindex] = A[pindex] , A[i]
            pindex = pindex + 1
            
    A[pindex] , A[end] = A[end] , A[pindex]
  
    return pindex
        
 
def quicksort(start,end):
    
    if start < end :
        pindex = partition(start,end)
        quicksort(start, pindex - 1)
        quicksort(pindex + 1, end)
    
quicksort(0,n-1)
print("After sorting")
print(A)
