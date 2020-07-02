use std::fs;

const INPUT_FILE: &str = "../../inputs/day1.input";

fn main() {
    println!("part1: {:?}", part1());
    println!("part2: {:?}", part2());
}

fn part1() -> i32 {
    let input_string: String = fs::read_to_string(INPUT_FILE).unwrap();
    input_string.split_whitespace().map(|str_val: &str| str_val.parse::<i32>().unwrap())
        .map(fuel_calc)
        .sum()
}

fn part2() -> i32 {
    let input_string: String = fs::read_to_string(INPUT_FILE).unwrap();
    input_string.split_whitespace().map(|str_val: &str| str_val.parse::<i32>().unwrap())
        .map(adv_fuel_calc)
        .sum()
}

fn fuel_calc(part_mass: i32) -> i32 {
    part_mass / 3 - 2
}

fn adv_fuel_calc(part_mass: i32) -> i32 {
    let mut result = 0;

    let mut added_fuel = fuel_calc(part_mass);
    while added_fuel > 0 {
        result += added_fuel;
        added_fuel = fuel_calc(added_fuel);
    }

    result
}
