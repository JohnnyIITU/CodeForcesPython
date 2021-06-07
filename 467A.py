rooms = []
count = int('0')
for i in range(0, int(input())) :
    rooms.append(list(map(int, input().split(" "))))
for i in range(0, len(rooms)) :
    if(rooms[i][1] - rooms[i][0] > 1) :
        count+=1
print(count)
