import random

def matematik_oyunu():
    skor = 0

    while True:
        sayi1 = random.randint(1, 20)
        sayi2 = random.randint(1, 20)
        operator = random.choice(['+', '-'])

        if operator == '+':
            correct_answer = sayi1 + sayi2
        elif operator == '-':
            correct_answer = sayi1 - sayi2

        question = f"Soru: {sayi1} {operator} {sayi2}? "
        user_answer = input(question)

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Geçersiz bir giriş yaptınız. Lütfen sayı girin.")
            continue

        if user_answer == correct_answer:
            print("Doğru cevap!")
            skor += 1
            devam_et = input("Devam etmek istiyor musunuz? (Evet/Hayır): ")
            if devam_et.lower() == "hayır":
                break
        else:
            print("Yanlış cevap!")

    print(f"Oyun bitti! Toplam doğru cevap sayınız: {skor}")

    print(f"Skorunuz: {skor}")

matematik_oyunu()
