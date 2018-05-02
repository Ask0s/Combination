import sys

def comb(A,n,k,p,lo):
    if p >= k or lo >= n:
        print(A)
    else:
        # for i in range(p,k):
        A[p] = lo
        comb(A,n,k,p+1,lo+1)
        A[p] = lo
        comb(A,n,k,p,lo+1)

if __name__ == "__main__":
    d = len(sys.argv)>3
    n = int(5)
    k = int(3)
    A = []
    for i in range(k):
        A.append(0)
    if d: print("n:",n,"k:",k)
    comb(A,n,k,0,0)