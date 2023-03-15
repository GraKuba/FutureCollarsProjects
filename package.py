# Napisz program do obsługi ładowarki paczek. Każda paczka może maksymalnie 
# zmieścić 20 kg towaru. 
# Do paczki dodawane są elementy. Każdy z nich może ważyć od 1 do 10 kg. 
# Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg, 
# paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów), 
# a bieżący element powinien zostać dodany do nowej paczki.
# Wszystkie elementy powinny zostać wysłane.
# Program powinien pobierać maksymalną liczbę elementów do wysyłki. Jeśli podano element o wadze 0, 
# program powinien zakończyć działanie, tak jakby maksymalna liczba paczek została osiągnięta.
# Na koniec działania program powinien wyświetlić w podsumowaniu:

# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów (brak optymalnego pakowania). 
# Liczba paczek * 20 - liczba kilogramów wysłanych
# Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
# Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, 
# lub mniej niż 1 kg i nie był dokładnie równy 0.

current_package = 0
kgs_sent = 0
packages_sent = 0
wasted_kgs = 0
highest_waste = 0
highest_waste_nr = 0
i = 0

while True:
    print('Package weight')
    package = int(input())
    i += 1
    if 0 < package < 11:
        if (current_package + package) > 20:
            print('Package has been sent')
            kgs_sent += current_package
            wasted_kgs += (20 - kgs_sent)
            if (highest_waste < wasted_kgs):
                highest_waste = wasted_kgs
                highest_waste_nr = i
            packages_sent += 1
            current_package = package 
        elif (current_package + package) == 20:
            print('Package has been sent')
            kgs_sent += 20
            packages_sent += 1
            current_package = 0
        else:
            current_package += package 
    elif package == 0:
        if current_package != 0:
            print('Package has been sent')
            kgs_sent += current_package
            packages_sent += 1
            break
        else:
            break
    else:
        print("Input different package weight.")
        pass
    print(f"Current package is: {current_package}")

print(f'Kgs sent: {kgs_sent}')
print(f'Packages sent {packages_sent}')
print(f'Wasted kgs: {wasted_kgs}')
print(f'Highest waste - package nr. {highest_waste_nr}: {highest_waste}')
