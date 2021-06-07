count = int(input())
line = input()
counter = int('0')
for i in range(0, len(line)-1) :
    if(line[i] == line[i+1]) :
        counter += 1
print(counter)
