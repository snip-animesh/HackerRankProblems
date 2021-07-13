
def matpow(mat1,mat2,r1,c2,r2):
    mat1 = mat1
    mat2 = mat2
    result = []
    r1=r1
    c2=c2
    r2=r2

    for r_1 in range(r1):
        sum = []
        for c_2 in range(c2):
            s = 0
            for r_2 in range(r2):
                s = (mat1[r_1][r_2] * mat2[r_2][c_2] + s)%1000000007
            sum.append(s)
        result.append(sum)
    return result

def matmul(A,n):
    magic=[[0,1],[1,1]]
    i=[[1,0],[0,1]]
    while(n>0):
        if n%2==0:
            magic=matpow(magic,magic,2,2,2)
            n//=2
        else:
            n-=1
            i=matpow(magic,i,2,2,2)
    return matpow(A,i,1,2,2)


for _ in range(int(input())):
    a,b,n=map(int,input().split())
    res=[[a,b]]
    result=matmul(res,n-1)
    print(result[0][1])
