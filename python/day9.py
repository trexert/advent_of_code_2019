from int_comp import int_comp


INPUT_FILE = "day9.input"


def solve():
    input_file = open(INPUT_FILE)
    code = map(int, input_file.readline().strip().split(","))
    return int_comp(code)


def main():
    solve()


if __name__ == "__main__":
    main()
