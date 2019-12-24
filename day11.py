from int_comp import Computer, BUFFERED
from queue import Empty
from pprint import pprint


INPUT_FILE = "day11.input"
LEFT = 0
RIGHT = 1
BLACK = 0
WHITE = 1


class Robot(object):
    def __init__(self, computer):
        self.computer = computer
        self.pos = [0, 0]
        self.dir = [0, 1]

    def turn(self, direction):
        if direction == RIGHT:
            self.dir[0], self.dir[1] = -self.dir[1], self.dir[0]
        else:
            self.dir[0], self.dir[1] = self.dir[1], -self.dir[0]

        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]

    def send(self, value):
        self.computer.put_input(value)

    def receive(self):
        try:
            return self.computer.get_output(), self.computer.get_output()
        except Empty:
            return None

    def start(self, initial_colour=BLACK):
        painted = {(0, 0): initial_colour}
        self.send(initial_colour)
        self.computer.start()
        result = self.receive()
        while result is not None:
            colour, direction = result
            painted[tuple(self.pos)] = colour
            self.turn(direction)
            try:
                self.send(painted[tuple(self.pos)])
            except KeyError:
                self.send(BLACK)

            result = self.receive()

        return painted


def get_robot():
    input_file = open(INPUT_FILE)
    code = map(int, input_file.readline().strip().split(","))
    return Robot(Computer(code, io_type=BUFFERED))


def part1():
    robot = get_robot()
    painted = robot.start()

    return len(painted)

def part2():
    robot = get_robot()
    painted = robot.start(WHITE)

    minx = 0
    maxx = 0
    miny = 0
    maxy = 0

    for pannel in painted:
        minx, maxx = min(minx, pannel[0]), max(maxx, pannel[0])
        miny, maxy = min(miny, pannel[1]), max(maxy, pannel[1])

    image = [["."] * (maxx - minx + 1) for _ in range(maxy - miny + 1)]

    for pos, colour in painted.items():
        if colour == WHITE:
            image[pos[1] - miny][pos[0] - minx] = "#"

    return image


def main():
    print(f"one: {part1()}")
    print("two:")
    pprint(["".join(row) for row in part2()])


if __name__ == "__main__":
    main()
