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
