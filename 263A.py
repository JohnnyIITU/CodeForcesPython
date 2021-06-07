row1 = list(map(int, input().split(" ")))
row2 = list(map(int, input().split(" ")))
row3 = list(map(int, input().split(" ")))
row4 = list(map(int, input().split(" ")))
row5 = list(map(int, input().split(" ")))
col = int('0')
row = int('0')
if(1 in row1) :
    col = int('1')
    row = row1.index(1)
if(1 in row2) :
    col = int('2')
    row = row2.index(1)
if(1 in row3) :
    col = int('3')
    row = row3.index(1)
if(1 in row4) :
    col = int('4')
    row = row4.index(1)
if(1 in row5) :
    col = int('5')
    row = row5.index(1)
row += 1
print(abs(3-row)+abs(3-col))
