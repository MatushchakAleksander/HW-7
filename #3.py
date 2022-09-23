import random

b = random.randint(1, 11)
counter = 0
a = ()
while counter != 3 and a != b:
    counter = counter + 1
    a = int(input("Попытка # " + str(counter) + ": "))

    if a > b:
        print("Бери меньше")

    elif a < b:
        print("Бери больше!")

    else:
        print("Ты угадал!")
