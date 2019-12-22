from int_comp import int_comp

INPUT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0]

def day2_1():
    code = INPUT
    result = int_comp(code)
    print(result)

def day2_2():
    for noun in range(100):
        for verb in range(100):
            code = INPUT.copy()
            code[1] = noun
            code[2] = verb
            result = int_comp(code)

            if result == 19690720:
                print(f"noun: {noun}, verb: {verb}")
