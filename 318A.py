line = list(map(int, input().split(" ")))
count = line[0]
index = line[1]
if(count % 2 == int('0')) :
    if(count / 2 > index) :
        print(index*int('2')-int('1'))
    else :
        print( index*int('2')-int('1')
else :
    if(int(count / 2)  + 1 < index) :
        print(int(count / int('2'))*int('2'))
    else : 
        print(int('2')*(index-int('1')) + int('1'))
