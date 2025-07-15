age = int(input("შეიყვანე შენი ასაკი: "))

if age < 18:
    years_left = 18 - age
    print("შენ 18 წლის გახდები", years_left, "წელიწადში.")
else:
    print("შენ უკვე 18 წლის ხარ ან მეტის!")
