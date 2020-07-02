from int_comp import Computer, BUFFERED

from itertools import permutations

INPUT_FILE_NAME = "day7.input"


class AmpCircuit(object):
    def __init__(self, code):
        self.amps = []
        for _ in range(5):
            self.amps.append(Computer(code, io_type=BUFFERED))
        self.reset_amps()

    def reset_amps(self):
        for amp in self.amps:
            amp.reset()
        for i, amp in enumerate(self.amps):
            amp.input_queue = self.amps[i - 1].output_queue

    def run(self):
        for amp in self.amps:
            amp.start()
        for amp in self.amps:
            amp.join()

    def set_phases(self, phase_list):
        assert len(phase_list) == 5
        for phase, amp in zip(phase_list, self.amps):
            amp.put_input(phase)

    def set_input(self, value):
        self.amps[0].put_input(value)

    def get_output(self):
        return self.amps[4].get_output()


def setup_circuit():
    input_file = open(INPUT_FILE_NAME)
    code = list(map(int, input_file.readline().strip().split(",")))
    return AmpCircuit(code)


def solve(part):
    circuit = setup_circuit()
    current_max = 0
    if part == 1:
        phase_lists = permutations([0, 1, 2, 3, 4])
    else:
        phase_lists = permutations([5, 6, 7, 8, 9])

    for phase_list in phase_lists:
        circuit.reset_amps()
        circuit.set_phases(phase_list)
        circuit.set_input(0)
        circuit.run()
        current_max = max(current_max, circuit.get_output())

    return current_max


def main():
    print(f"problem1: {solve(1)}")
    print(f"problem2: {solve(2)}")


if __name__ == "__main__":
    main()
