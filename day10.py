import math
import numpy as np


INPUT_FILE = "day10.input"


def get_bearing(vector):
    # We want the clockwise angle from vertical. Map the axes to fit this
    # Positive X should be straigt up (currently negative Y) and positive Y should be
    # straight right (currently positive X)

    x = -vector[1]
    y = vector[0]

    # Now we can think about normal angle calculation
    if x == 0:
        angle = math.pi / 2 if y > 0 else -math.pi / 2
    else:
        angle = math.atan(y / x)

    # We now have an angle in the range [-pi/2, pi/2]
    # Consider the left hand side too

    if x < 0:
        angle += math.pi

    # Force positive angles
    if angle < 0:
        angle += 2 * math.pi

    return angle


def get_distance(vector):
    return np.linalg.norm(vector)


class asteroid(object):
    def __init__(self, x, y):
        self.can_see = {}
        self.pos = np.array([x, y], dtype=np.int8)

    def look_at(self, other):
        direction = other.pos - self.pos
        bearing = get_bearing(direction)
        distance = get_distance(direction)
        if bearing not in self.can_see:
            self.can_see[bearing] = [(distance, other)]
        else:
            self.can_see[bearing].append((distance, other))

    def get_destruction_order(self):
        asteroid_list = []
        for direction, asteroids in self.can_see.items():
            asteroids = sorted(asteroids)
            asteroids = [
                (direction + i * 2 * math.pi, asteroid)
                for i, (_, asteroid) in enumerate(asteroids)
            ]
            asteroid_list.extend(asteroids)

        return [asteroid for _, asteroid in sorted(asteroid_list)]


class System(object):
    def __init__(self):
        self.asteroids = get_asteroids()
        self._best_base = None

    def best_base(self):
        if self._best_base is not None:
            return self._best_base

        best_base = None
        for potential_base in self.asteroids:
            for asteroid in filter(lambda x: x != potential_base, self.asteroids):
                potential_base.look_at(asteroid)

            if best_base is None or len(potential_base.can_see) > len(
                best_base.can_see
            ):
                best_base = potential_base

        self._best_base = best_base
        return best_base

    def get_destruction_order(self):
        return self.best_base().get_destruction_order()


def get_asteroids():
    input_file = open(INPUT_FILE)
    asteroids = []
    station = None
    for y, line in enumerate(input_file):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append(asteroid(x, y))
            elif char == "X":
                station = asteroid(x, y)

    if station:
        asteroids = station, asteroids
    return asteroids


def part1(system):
    return len(system.best_base().can_see)


def part2(system):
    destruction_order = system.get_destruction_order()
    twohundredth = destruction_order[199]
    return f"x: {twohundredth.pos[0]}, y: {twohundredth.pos[1]}"


def main():
    system = System()
    print(f"one: {part1(system)}")
    print(f"two: {part2(system)}")


if __name__ == "__main__":
    main()
