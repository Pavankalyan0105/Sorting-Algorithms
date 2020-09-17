def mergeSort(arr):
    if(len(arr) == 1):
        return arr
    mid = len(arr)//2
    left , right = arr[:mid] , arr[mid:]
    mergeSort(left)
    mergeSort(right)
    result = merge(left , right , arr)
    return result
    
    
    
def merge(left , right , arr):
    nL = len(left)
    nR = len(right)
    i,j,k=0,0,0
    while(i<nL and j<nR):
        if(left[i] < right[j]):
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while(i<nL): 
        arr[k] = left[i]
        i+=1
        k+=1
        
    while(j<nL): 
        arr[k] = right[j]
        j+=1
        k+=1
    return arr
    

list=[]
list = [int(i) for i in input().split()]
print(mergeSort(list))
