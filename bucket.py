def bv(node,count):
    l = 2*node+1
    r = 2*node+2
    if l < len(A):
        count = bv(l, count-1 if count else 0)
    if ret[count] == -1:
        ret[count] = A[node]
    if r < len(A):
        bv(r, count+1)
    return count+1

A = [20,2,3,1,4,5,6]
ret = [-1]*(len(A)+1)
bv(0,0)
print(ret[:ret.index(-1)])
