excepts = ['H', 'Q', '9']
printed = int('0')
for i in input() :
    if(i in excepts) :
        printed = int('1')
if(printed == int('1')) :
    print("YES")
else :
    print("NO")
