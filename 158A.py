at = input().split(" ")
n = int(at[0])
k = int(at[1])
a = list(map(int,input().split(" ")))
rank = int(k)
lastElem = int('-1')
check = 'true';
a.sort(reverse = True)
index = int('0')
for i in a :
    if(check == 'true') :
        if(int(i) == int('0')) :
            check = 'false'
            rank = int(index)
        if(lastElem == -1):
            lastElem = int(i)
        if(index >= k):
            if(int(i) == int(lastElem)) :
                rank=int(rank) + 1
            else :
                check = 'false'
        else :
            lastElem = int(i)
        index+=1
print(rank)
