# программа, которая получает номер месяца и выводит соответствующее ему время года или сообщение об ошибке.

months = ["Времена года", "Зима", "Весна", "Лето", "Осень" ]

number = int(input("Введите номер месяца:"))
if number > 12 :
    print("Неверный номер месяца")
elif number<3 or number==12:
    print(months[1])
elif number<6:
    print(months[2])
elif number<9:
    print(months[3])
elif number<12:
    print(months[4])



