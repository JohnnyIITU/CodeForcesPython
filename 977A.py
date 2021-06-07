n,k = map(int,input().split())
while(k>0) :
    if(n%int(10) == int(0)) :
        n = int(n/10)
        k-=int(1)
    else :
        n -= int(1)
        k-=int(1)
print(n)
