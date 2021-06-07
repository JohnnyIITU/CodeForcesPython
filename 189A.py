import sys
n,a,b,c = list(map(int, input().split(" ")))
cuts = [a,b,c]
cuts.sort()
max_cuts = dict()
for i in range(n+int(1)) :
    max_cuts[i] = int('-999999999')
max_cuts[0] = int(0)
max_cuts[cuts[0]] = int(1)
max_cuts[cuts[1]] = int(1)
max_cuts[cuts[2]] = int(1)
for i in range(int(1),n+int(1)) :
    for j in range(int(3)) :
        if(cuts[j] > i) :
            break
        max_cuts[i] = max(max_cuts[i-cuts[j]] + int(1), max_cuts[i])
print(max_cuts[n])
