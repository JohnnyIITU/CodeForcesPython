input()
gameRes = input()
aCount = int('0')
for i in gameRes :
    if(i == 'A') :
        aCount+=1
bCount = len(gameRes) - aCount
if(aCount == bCount) :
    print("Friendship")
elif(aCount > bCount) :
    print("Anton")
else :
    print("Danik")
