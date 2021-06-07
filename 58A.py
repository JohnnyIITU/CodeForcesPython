s = input().lower()
hFinded = int('0')
eFinded = int('0')
l1Finded = int('0')
l2Finded = int('0')
oFinded = int('0')
finded = int('0')
for i in s :
    if(hFinded == int('0')) :
        if(i == 'h') :
            hFinded = int('1')
    else : 
        if(eFinded == int('0')) :
            if(i == 'e') :
                eFinded = int('1')
        else :
            if(l1Finded == int('0')) :
                if(i == 'l') :
                    l1Finded = int('1')
            else :
                if(l2Finded == int('0')) :
                    if(i == 'l') :
                        l2Finded = int('1')
                else :
                    if(i == 'o') :
                        oFinded = int('1')
                        finded = int('1')
if(finded == int('1')) :
    print("YES")
else :
    print("NO")
