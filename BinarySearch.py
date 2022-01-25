
class BinarySearch:

#    def __init__(self, A = []):
#        self.arr = A

    def bs(self, val, array):
        li, ri = 0, len(array)
        mi = (li+ri)//2
        if not array: # or ri < li:
            return -1
        if array[mi] == val:
            return mi
        elif array[mi] > val:
            return self.bs(val, array[:mi])
        else:
            ret = self.bs(val, array[mi+1:])
            return mi +1 + ret if ret != -1 else -1

    def insertionSort(self, val, array, li, ri):
        if ri < li:
            return array[:ri+1]+[val]+array[ri+1:]
        mi = (li+ri)//2
        if array[mi] == val:
            return array[:mi+1]+[val]+array[mi+1:]
        elif array[mi] > val:
            return self.bsAdd(val, array, li, mi-1)
        else:
            return self.bsAdd(val, array, mi+1, ri)

BS = BinarySearch()
A = [1,2,3,4,6,8]
print(A)
for i in range(A[-1]+2):
    print(i,BS.bs(i,A))

print(5,BS.insertionSort(5,A,0,len(A)-1))
print(-1,BS.insertionSort(-1,A,0,len(A)-1))
print(11,BS.insertionSort(11,A,0,len(A)-1))
print(3,BS.insertionSort(3,A,0,len(A)-1))
print(1,BS.insertionSort(1,A,0,len(A)-1))
