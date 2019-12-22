from pprint import pprint

class orbital_body(object):
    def __init__(self, name):
        self.name = name
        self.primary = None
        self.satellites = []
        self._orbits_to_com = None
        self._path_to_com = None

    def __str__(self):
        if self.primary:
            return f"{self.primary.name}){self.name}"
        else:
            return self.name

    def __repr__(self):
        return self.__str__()

    def add_satellite(self, satellite):
        self.satellites.append(satellite)
        satellite.primary = self

    def get_orbits_to_com(self):
        if not self._orbits_to_com:

            if self.primary:
                self._orbits_to_com = self.primary.get_orbits_to_com() + 1
            else:
                self._orbits_to_com = 0

        return self._orbits_to_com

    def get_path_to_com(self):
        if not self._path_to_com:

            if self.primary:
                self._path_to_com = self.primary.get_path_to_com() | set([self.name])
            else:
                self._path_to_com = set([self.name])
        
        return self._path_to_com

def build_storage():
    input_file = open("day6.input")
    storage = {}
    for line in input_file:
        primary, satellite = line.strip().split(")")
        for body_name in primary, satellite:
            if body_name not in storage:
                storage[body_name] = orbital_body(body_name)

        storage[primary].add_satellite(storage[satellite])

    return storage

def part1():
    storage = build_storage()

    orbit_count = 0
    for body in storage.values():
        orbit_count += body.get_orbits_to_com()

    return orbit_count

def part2():
    storage = build_storage()
    you_path = storage["YOU"].get_path_to_com()
    san_path = storage["SAN"].get_path_to_com()

    return len(you_path ^ san_path) - 2

def main():
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")

if __name__ == "__main__":
    main()
