"""
We know from fermat's theorem that , a^(p-1) = 1(mod p) .Here = holds for equivalent sign .

Our equation is a=x^2 (mod p)

So , any number x^(p-1) must to be equal 1(mod p) isn't it?

                Now , a^(p-1) = (x^2)^(p-1) ; from given equation 

                it makes u sense that if we put (p-1)/2 for (p-1) then 

                a^ (p-1)/2  =  (x^2)^((p-1) /2) =  x^(p-1) = 1(mod p)

      So, from here we can see that if x will be  in the from of x^2 then  (x^2)^((p-1) /2)  
      tends to  x^(p-1)  which is equal to 1(mod p) but .Here one important criteria is a^ (p-1)/2 
      should be obvious 1 also . As , X is not given . a^(p-1)/2 should be 1 to make x^2 form under modulo(p) """

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


for _ in range(int(input())):
    A,M=map(int,input().split())
    if A==0:
        print("YES")
    else:
        res=power(A,(M-1)//2,M)%M
        if res ==1:
            print("YES")
        else:
            print("NO")
