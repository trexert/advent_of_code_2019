def day1_1():
    mass = input()
    total_fuel = 0
    while mass != "":
        mass = int(mass)
        total_fuel += mass // 3 - 2
        mass = input()

    print(f"total fuel requred: {total_fuel}")

def day1_2():
    mass = input()
    total_fuel = 0
    while mass != "":
        mass = int(mass)
        fuel_to_add = mass // 3 - 2
        while fuel_to_add > 0:
            total_fuel += fuel_to_add
            fuel_to_add = fuel_to_add // 3 - 2
        mass = input()

    print(f"total fuel requred: {total_fuel}")
