import random

def multipli_game():
    wrong = 0
    good = 0
    for i in range(10):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        x = eval(input(f"Pytanie {i+1}: {a} x {b} = "))
        if x == a*b:
            print("Poprawna odpowiedź!")
            good += 1
        else:
            print(f"Błędna odpowiedź, poprawną odpowiedzia jest {a*b}")
            wrong += 1
    print(f"Błędne odpowiedzi: {wrong}")
    print(f"Poprawne odpowiedzi: {good}")
multipli_game()
