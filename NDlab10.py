from colorama import Fore, Back, Style
from colorama import init
import math

init()
a = int(input("Санды енгіз!\n"))
if a == 1:
    print("Қалалар ойыны")
    print(Style.BRIGHT)  # цвет в терминале

    k_s_j = [
        ("Алматы Қазақстанның астанасы ма?", "жоқ"),
        ("Ақтау Қазақстанның батысында орналасқан", "иә"),
        ("Талдықорған Алматы облысында орналақан", "жоқ")
    ]
    print(Back.RESET)
    answers_counter = [0, 0]
    print(Fore.BLUE)
    for q, a in k_s_j:
        print(q, '[иә/жоқ]' + Style.BRIGHT)
        answer = input().strip().lower()
        if answer == a:
            print("Дұрыс жауап\n")
            answers_counter[0] += 1
            answers_counter[1] += 1
        else:
            print("Қате жауап\n")
            answers_counter[0] += 1
    print(Style.RESET_ALL)
    print("\nЖауап берілді: {}, Дұрыс жауаптар: {}".format(answers_counter[0], answers_counter[1]))
    input()
elif a == 2:
    print("Сандар ойыны")
    print(Style.BRIGHT)

    s_s_j = [
        ("3 тің 5 дәрежесі ", math.pow(3, 5)),
        ("2 нің факториалы ! ", math.factorial(2)),
        ("log10(100) нешеге тең?", math.log10(100)),
        ("Түбір астында 122 нешеге тең?", int(math.sqrt(122))),
        ("Тангенс 180 нешеге тең?", int(math.tan(180)))
    ]
    print(Back.RESET)
    answers_counter = [0, 0]
    print(Fore.GREEN)
    for q, a in s_s_j:
        print(q + Style.BRIGHT)
        answer = int(input().strip().lower())
        if answer == a:
            print("Дұрыс жауап\n")
            answers_counter[0] += 1
            answers_counter[1] += 1
        else:
            print("Қате жауап\n")
            answers_counter[0] += 1
    print(Style.RESET_ALL)
    print("\nЖауап берілді: {}, Дұрыс жауаптар: {}".format(answers_counter[0], answers_counter[1]))
    input()
elif a == 3:
    print("Жолдар ойыны")
    print(Style.BRIGHT)

    s_s_j = [
        ("NoteBook.swapcase() - нені шығарады", "NoteBook".swapcase()),
        ("PyTHoN.capitalize() - нені шығарады", "PyTHoN".capitalize()),
        ("Java.zfill(6) - нені шығарады", "Java".zfill(6))
    ]
    print(Back.RESET)
    answers_counter = [0, 0]
    print(Fore.CYAN)
    for q, a in s_s_j:
        print(q + Style.BRIGHT)
        answer = input()
        if answer == a:
            print("Дұрыс жауап\n")
            answers_counter[0] += 1
            answers_counter[1] += 1
        else:
            print("Қате жауап\n")
            answers_counter[0] += 1
    print(Style.RESET_ALL)
    print("\nЖауап берілді: {}, Дұрыс жауаптар: {}".format(answers_counter[0], answers_counter[1]))
    input()
