import timeit

def insertionSort(arr): 
  
    # percorre o array 'arr'
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return arr
vetor = []
for i in range(1,10):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)
inicio = timeit.default_timer()
vetor = insertionSort(vetor)
fim = timeit.default_timer()
print(vetor)
print('tempo de ordenação: %f ms' %(fim-inicio))