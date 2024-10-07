N = int(input())
for i in range(2,N):
    g = 0
    for t in range(1,i):
        if i % t == 0:
            g = g+1
    if g == 1:
        print(i)
