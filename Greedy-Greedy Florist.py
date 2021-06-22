n,k=map(int,input().split())
lst=sorted([int(x) for x in input().split()])
lst.reverse()
sum=sum(lst[:k])
del lst[:k]
lst.reverse()
if lst!=[]:
    for i in range(1,len(lst)+1):
        for j in range(k):
            x=lst.pop()
            sum=(x*(1+i))+sum

            if lst==[]:
                break
        else:
            continue
        break
print(sum)
