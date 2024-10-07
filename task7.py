count = 0
N = int(input())
for i in range(2,N):
    for j in range(2,i):
        if i%j==0: count +=1
        if count>1:break
    print(i)

