INPUT_FILE = "day12.input"
STEPS = 1000


class Moon(object):
    def __init__(self, start_pos):
        self.dims = len(start_pos)
        self.pos = start_pos
        self.vel = [0] * self.dims

    def update_velocity(self, other):
        if self == other:
            return

        for dim in range(self.dims):
            if self.pos[dim] < other.pos[dim]:
                self.vel[dim] += 1
            elif self.pos[dim] > other.pos[dim]:
                self.vel[dim] -= 1

    def update_pos(self):
        for dim in range(self.dims):
            self.pos[dim] += self.vel[dim]

    def get_energy(self):
        return sum(map(abs, self.pos)) * sum(map(abs, self.vel))


class System(object):
    def __init__(self, moons):
        self.moons = moons

    def time_step(self):
        for moon in self.moons:
            for other in self.moons:
                moon.update_velocity(other)

        for moon in self.moons:
            moon.update_pos()

    def total_energy(self):
        energy = 0
        for moon in self.moons:
            energy += moon.get_energy()
        return energy


def build_system():
    input_file = open(INPUT_FILE)
    moons = []
    for line in input_file:
        line = line.strip()
        line = line.strip("<>")
        pos = [int(part.split("=")[1]) for part in line.split(",")]
        moons.append(Moon(pos))

    return System(moons)


def solve():
    system = build_system()
    for _ in range(STEPS):
        system.time_step()

    return system.total_energy()


def main():
    print(f"one: {solve()}")


if __name__ == "__main__":
    main()
