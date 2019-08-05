def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
arr = [] 
for num in range(10):
    arr.append(int(input('Digite um numero\n')))

insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 