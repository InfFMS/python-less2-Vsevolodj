count = 0
a = 0
N = int(input())
for i in range(2,N):
    for j in range(2,i+1):
        if i%j==0: count +=1
        if count>1:
            a = j
            break

    print(a)


