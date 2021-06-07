#LOWER 65-90
#UPPER 97-122
string = input()
lowers = int('0')
uppers = int('0')
for i in string :
    if(ord(i) > 96) :
        lowers+=1
    else :
        uppers+=1
if(lowers >= uppers) :
    print(string.lower())
else :
    print(string.upper())
