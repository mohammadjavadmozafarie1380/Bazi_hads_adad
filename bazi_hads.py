
import random

while True:
    number = random.randint(1, 10)

    print("بازی حدس عدد")
    print("شما 5 بار فرصت حدس دارید")

    for i in range(5):
        guess = int(input("عدد مورد نظر را وارد کنید: "))

        if guess == number:
            print("آفرین! درست حدس زدی")
            break
        else:
            print("اشتباه است!")

    if guess != number:
        print("فرصت های شما تمام شد")
        print("عدد درست:", number)

    while True:
        again = input("بازی دوباره؟ (بله/خیر): ")

        if again == "بله":
            break

        else:
            print("لطفاً درست وارد کنید! فقط بله یا خیر")
