nabidka = ["Velikonoční beránek", "Vajíčka", "Pomlázky", "Čokoláda", "Kinder vajíčka"]
kosik = []

print("Vítejte v aplikace Koledník")

while True:
    print("-------------------------------------")
    print("Ahoj koledníku, co bys rád do košíku?")
    print("-------------------------------------")
    print("Zde máme na výběr")

    # Výpis dat z listu do terminálu s číslování
    for i in range(len(nabidka)):
        print(f"    {i+1}. {nabidka[i]}")

    volba = input("Zadejte vaší volbu koledy: ")

    if volba == nabidka[0]:
        kosik.append(nabidka[0])
        nabidka.pop(0)
    elif volba == nabidka[1]:
        kosik.append(nabidka[1])
        nabidka.pop(1)
    elif volba == nabidka[2]:
        kosik.append(nabidka[2])
        nabidka.pop(2)
    elif volba == nabidka[3]:
        kosik.append(nabidka[3])
        nabidka.pop(3)
    elif volba == nabidka[4]:
        kosik.append(nabidka[4])
        nabidka.pop(4)
    else:
        print("Tohle v nabídce nemáme :(")

    print("------------------------------------")
    print("Obsah vašeho košíku")
    
    #výpis obsahu košíku
    for i in range(len(nabidka)):
        print(f"    {i+1}. {nabidka[i]}")