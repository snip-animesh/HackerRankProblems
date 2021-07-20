def phi(n):
    res,i,o=n,2,n
    lst,nums_lst=[],[]
    while(i*i<=n):
        if n%i==0:
            res//=i
            res*=(i-1)
            lst.append(i)
            nums_lst.append(o//i)
            while(n%i==0):
                n//=i
        i+=1
    if n>1:
        res//=n
        res*=(n-1)
        lst.append(n)
        nums_lst.append(o//n)
    return res,lst,nums_lst
def power(base,power,mod):
    res = 1
    while (power > 0):
        if power % 2 == 0:
            base = ((base)%mod)*((base)%mod)
            power //= 2
        else:
            res = ((res)%mod)*((base)%mod)
            power -= 1
    return res


n=int(input())
res,lst,nums_lst=phi(n-1)
# print(res,lst,nums_lst)
for i in range(2,n):
    for j in nums_lst:
        if power(i,j,n)%n==1:
            break
    else:
        print(i,res)
        break

        
