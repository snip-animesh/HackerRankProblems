def pf(n):
    i,res,m=2,n,10**9+7
    while(i*i<=n):
        if n%i==0:
            res//=i
            res*=(i-1)
            while(n%i==0):
                n//=i

        i+=1
    if n>=2:
        res//=n
        res*=(n-1)
    return (res//2)%m


n=int(input())
if n<3:
    print(n-1)
else:
    m=10**9+7
    x=n%m
    y=pf(n)
    print(int((x*y)%m))
