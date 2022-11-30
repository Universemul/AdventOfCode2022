use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> io::Result<Vec<String>>
where P: AsRef<Path> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines().map(|line| line.unwrap().to_string()).collect())
}

pub fn read_ints(filename: &str) -> Vec<i32> {
    let lines = read_lines(filename).unwrap(); 
    lines.iter().map(|line| line.parse::<i32>().unwrap()).collect()
}

pub fn get_args() -> Vec<String> {
    env::args().collect()
}
