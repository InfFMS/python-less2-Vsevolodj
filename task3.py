number = int(input("Введите возраст:"))
if number > 120 :
    print("Неверный возраст")
elif number == 11 or number == 12 or number == 13 or number == 14 or number == 15:
    print(number, "лет")
elif (number%10)==1:
    print(number, "год")
elif (number%10)<5 and (number%10)!=0 :
    print(number, "года")
elif (number%10)==0 or (number//10)<10  :
    print(number, "лет")