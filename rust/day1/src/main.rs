use std::fs::File;
use std::io::Read;

fn main() {
    part1();
    part2();
}

fn compute() -> Vec<i32> {
    let mut file = File::open("input.txt").unwrap();
    let mut s = String::new();
    file.read_to_string(&mut s).unwrap();
    let vec: Vec<&str> = s.split("\n\n").collect();
    let mut elves: Vec<i32> = vec.iter()
        .map(|item| item.split("\n")
             .filter(|x| !x.is_empty())
             .map(|x| x.parse::<i32>().unwrap()).sum::<i32>()
        )
        .collect();
    elves.sort_by(|a, b| b.cmp(a));
    elves
}

fn part1() {
    let elves = compute();
    println!("{:?}", elves[0]);
}

fn part2() {
    let elves = compute();
    println!("{:?}", &elves[0..3].iter().sum::<i32>());
}
