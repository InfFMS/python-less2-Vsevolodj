number = int(input("Введите возраст:"))
if number > 120 :
    print("Неверный возраст")
elif (number%10)==1:
    print(number, "год")
elif (number%10)<5 and (number%10)!=0 :
    print(number, "года")
elif (number%10)==0 or (number//10)<10  :
    print(number, "лет")