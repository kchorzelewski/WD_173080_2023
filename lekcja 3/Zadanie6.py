def guess_the_number():
    a = random.randint(1,10)
    shots = 0
    points = 0
    while(shots<5):
        shots+=1
        x = eval(input("Zgadnij liczbę: "))
        if x == a:
            print(f"Wylosowana liczba to {a}, zdobywasz 10 punktów")
            points += 10
        else:
            print(f"Wylosowana liczba to {a}. Tracisz punkt")
            if points:
                points-=1
        a = random.randint(1, 10)
    print(f"Koniec gry. Twoja punktacja to {points} punktów")
guess_the_number()
