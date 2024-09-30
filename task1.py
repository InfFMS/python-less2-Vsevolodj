# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

number = int(input("Введите номер урока:"))
if number>13:
    print("Уроки закончились. Пора домой")
else:
    print("Начало:", (8 * 60 + 30 - 10 + 55 * (number-1)+10) // 60, ":", (8 * 60 + 30 - 10 + 55 * (number-1)+10) % 60)
    print("Конец:", (8*60+30-10+55*number)//60, ":", (8*60+30-10+55*number)%60)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
