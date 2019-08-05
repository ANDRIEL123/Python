from random import randint
import timeit

def insertionSort(alist):

   for i in range(1, len(alist)):

       # element to be compared
       current = alist[i]

       # comparing the current element with the sorted portion and swapping
       while i > 0 and alist[i-1] > current:
           alist[i] = alist[i-1]
           i = i-1
           alist[i] = current

       # print(alist)

   return alist

arr = []

for i in range(1000):
    arr.append(int(randint(0, 1000)))

inicio = timeit.default_timer()
insertionSort(arr)
fim = timeit.default_timer()

print(arr)
print('\n\nArray ordenado\n\n')
print(arr)
print('tempo de ordenação: %f ms' %(fim-inicio))
