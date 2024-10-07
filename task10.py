c1=int(input())
r1=int(input())
c2=int(input())
r2=int(input())
if (c1>8 or c1<1 or r2>8 or r2<1):
    print("Неверно")
elif (r1-c1-r2+c2==0 or r1+c1-r2-c2==0 or r1==r2 or c1==c2) and (r1!=r2 or c1!=c2):
    print("YES")
else:
    print("NO")
