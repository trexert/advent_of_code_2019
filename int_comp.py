from queue import Queue

# IO Types
HUMAN = "human"
BUFFERED = "buffered"

# Modes
POS = 0
IMM = 1

# Operators
ADD = 1
MUL = 2
RIN = 3
OUT = 4
JIT = 5
JIF = 6
SLT = 7
EQU = 8
HALT = 99

BINARITH = [ADD, MUL]
IO = [RIN, OUT]
FLOW = [JIT, JIF]
COMPARISON = [SLT, EQU]


class OpError(Exception):
    pass


class ModeError(Exception):
    pass


class Computer(object):
    def __init__(self, code, io_type=HUMAN):
        assert io_type in [HUMAN, BUFFERED]
        self._io_type = io_type
        self.prov_code = code.copy()
        self.reset()

    def reset(self):
        self.code = self.prov_code.copy()
        self.oppos = 0
        if self._io_type == BUFFERED:
            self.input_queue = Queue()
            self.output_queue = Queue()

    def run(self):
        while True:
            mode_code, operator = self._get_op()

            if operator == HALT:
                break

            elif operator in BINARITH or operator in COMPARISON:
                args, resloc = self._get_args(mode_code, 2)

                if operator == ADD:
                    self.code[resloc] = args[0] + args[1]
                elif operator == MUL:
                    self.code[resloc] = args[0] * args[1]
                elif operator == SLT:
                    self.code[resloc] = 1 if args[0] < args[1] else 0
                elif operator == EQU:
                    self.code[resloc] = 1 if args[0] == args[1] else 0

                self.oppos += 4

            elif operator in IO:
                if operator == RIN:
                    _, resloc = self._get_args(mode_code, 0)
                    self.code[resloc] = self._get_input()
                elif operator == OUT:
                    args, _ = self._get_args(mode_code, 1)
                    self._set_output(args[0])

                self.oppos += 2

            elif operator in FLOW:
                args, _ = self._get_args(mode_code, 2)

                if (operator == JIT and args[0] != 0) or (
                    operator == JIF and args[0] == 0
                ):
                    self.oppos = args[1]
                else:
                    self.oppos += 3

            else:
                raise OpError([mode_code, operator, self.code, self.oppos])

        return self.code[0]

    def put_input(self, value):
        self.input_queue.put(value)

    def get_output(self, timeout=5):
        return self.output_queue.get(timeout=timeout)

    def _get_args(self, mode_code, arg_count):
        arg_pos = self.oppos
        args = list()
        for _ in range(arg_count):
            arg_pos += 1
            mode_code, mode = divmod(mode_code, 10)
            if mode == POS:
                args.append(self.code[self.code[arg_pos]])
            elif mode == IMM:
                args.append(self.code[arg_pos])
            else:
                raise ModeError()

        resloc = self.code[self.oppos + arg_count + 1]

        return args, resloc

    def _get_op(self):
        opcode = self.code[self.oppos]
        return divmod(opcode, 100)

    def _get_input(self):
        if self._io_type == HUMAN:
            result = int(input("Provide input to the int computer: "))
        else:
            result = self.input_queue.get(timeout=5)

        return result

    def _set_output(self, value):
        if self._io_type == HUMAN:
            print(f"int computer output: {value}")
        else:
            self.output_queue.put(value)


def int_comp(prov_code):
    return Computer(prov_code).run()
