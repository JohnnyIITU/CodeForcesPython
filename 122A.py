goodNumbers = []
goodNum = [int('4') , int('7')]
for i in goodNum : 
    goodNumbers.append(i)
    for j in goodNum :
        sec = int(str(i)+str(j))
        for k in goodNum :
            thr = int(str(i)+str(j)+str(k))
            goodNumbers.append(thr)
        goodNumbers.append(sec)
checkNum = int(input())
isGoodNumber = int('0')
for i in goodNumbers :
    if(checkNum % i == 0 ) :
        isGoodNumber = int('1')
if(isGoodNumber == int('1')) :
    print("YES")
else :
    print("NO")
