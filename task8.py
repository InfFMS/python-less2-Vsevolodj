c1=int(input())
r1=int(input())
c2=int(input())
r2=int(input())
if (r1>8 or r1<1 or r2>8 or r2<1):
    print("Неверно")
elif (abs(c1-c2)==2 and abs(r1-r2)==1) or (abs(c1-c2)==1 and abs(r1-r2)==2):
    print("YES")
else:
    print("NO")
