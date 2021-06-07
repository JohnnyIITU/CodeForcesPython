count = int(input())
mins = []
for i in range(0, count) :
    line = list(map(int, input().split(" ")))
    n =line[0]
    k =line[1]
    d =line[2]
    min = d
    days = list(map(int ,input().split(" " )))
    for j in range(0, n - d+1) :
        if(len(set(list(days[j:j+d]))) < min) :
            min = len(set(list(days[j:j+d])))
    mins.append(min)
for i in mins :
    print(i)
