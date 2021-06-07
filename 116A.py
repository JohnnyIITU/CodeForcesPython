count = int(input())
operations = []
max = int('0')
current = int('0')
for i in range(0, count) :
    operations.append(input())
    places = operations[i].split(" ")
    current -= int(places[0])
    if(max < current) :
        max = current
    current += int(places[1])
    if(max < current) :
        max = current
print(max)
