power = int(input("Введите число:"))
s = 2
s = str(s)
for i in range(2,power+1):
    a = 2**i
    a = str(a)
    s = s +" "+a

print(s)
