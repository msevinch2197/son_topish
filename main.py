import random

def guess_number():
    print("🎮 Son topish o‘yiniga xush kelibsiz!")
    print("Men 1 dan 100 gacha son o‘yladim.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("👉 Taxminingni kiriting: "))
            attempts += 1

            if guess < number:
                print("📉 Juda kichik!")
            elif guess > number:
                print("📈 Juda katta!")
            else:
                print(f"🎉 To‘g‘ri topding! {attempts} ta urinishda!")
                break

        except ValueError:
            print("❌ Iltimos, son kiriting!")

if __name__ == "__main__":
    guess_number()
