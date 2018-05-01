import sys

def comb(A,n,k,p,lo):
    if p == len(A):
        print(A)
        return
    else:
        for i in range(p,len(A)):
            A[i], lo = lo, A[i]
        comb(A,n,k,p+1,lo+1)
        comb(A,n,k,p,lo+1)

if __name__ == "__main__":
    d = len(sys.argv)>3
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    A = []
    for i in range(k):
        A.append(0)
    if d: print("n:",n,"k:",k)
    comb(A,n,k,0,0)