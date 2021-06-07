goodNumbers = ['4', '7']
number = input()
count = int('0')
for i in number :
    if(i in goodNumbers) :
        count+=1
if(count == int('4') or count == int('7')) :
    print("YES")
else :
    print("NO")
