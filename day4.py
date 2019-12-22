def try_password(number, allow_large_groups):
    number, last_digit = divmod(number, 10)
    in_large_group = False
    found_potential_pair = False
    found_pair = False
    last_one_matched = False
    while number > 0:
        number, temp = divmod(number, 10)

        if temp > last_digit:
            return False

        if temp == last_digit:
            if allow_large_groups:
                found_pair = True
            else:
                if found_potential_pair or in_large_group:
                    in_large_group = True
                    found_potential_pair = False
                else:
                    found_potential_pair = True

        else:
            found_pair |= found_potential_pair
            found_potential_pair = False
            in_large_group = False

        last_digit = temp

    return found_pair or found_potential_pair

def solve(allow_large_groups):
    count = 0
    for x in range(134564, 585160):
        if try_password(x, allow_large_groups):
            count += 1
    return count

def problem1():
    return solve(True)

def problem2():
    return solve(False)

def main():
    print(problem1())
    print(problem2())

if __name__ == "__main__":
    main()