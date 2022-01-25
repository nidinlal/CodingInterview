class Sort:

    def merge(self, A, B):
        Ai, An = 0, len(A)
        Bi, Bn = 0, len(B)
        ret = []
        while Ai < An and Bi < Bn:
            if A[Ai] <= B[Bi]:
                ret.append(A[Ai])
                Ai += 1
            else:
                ret.append(B[Bi])
                Bi += 1
        if Ai == An:
            ret += B[Bi:]
        else:
            ret += A[Ai:]
        return ret

    def mergeSort(self, array):
        if len(array) <= 1:
            return array
        mi = len(array)//2
        A = self.mergeSort(array[:mi])
        B = self.mergeSort(array[mi:])
        return self.merge(A,B)

    def quickSort(self,array):
        if len(array) <= 1:
            return array
        pi = 0
        lArr = []
        rArr= []
        for i in range(1,len(array)):
            if array[i] <= array[pi]:
                lArr.append(array[i])
            else:
                rArr.append(array[i])
        return self.quickSort(lArr)+[array[pi]]+self.quickSort(rArr)

Array = [2,6,1,9,5,8,5,2,5,4,9,0,-1,-3,4]

sort = Sort()
print(Array,sorted(Array))
print(sort.mergeSort(Array))
print(sort.quickSort([2,6,1,3,4]))
print(sort.quickSort(Array))
