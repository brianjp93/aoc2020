use std::fs;
use regex::Regex;

fn main() {
    let data = fs::read_to_string("./inputs/day2").unwrap();
    let data = data.split("\n").collect::<Vec<&str>>().into_iter()
        .filter(|x| {x != &""})
        .collect::<Vec<&str>>();
    let counts = get_counts(data);
    println!("Part 1: {:?}", &counts[0]);
    println!("Part 2: {:?}", &counts[1]);
}

fn get_counts(data: Vec<&str>) -> [usize; 2] {
    let re = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    let mut count1 = 0 as usize;
    let mut count2 = 0 as usize;
    for row in data {
        let caps = re.captures(row).unwrap();
        let low = caps[1].parse::<usize>().unwrap();
        let high = caps[2].parse::<usize>().unwrap();
        let letter = &caps[3];
        let word = &caps[4];

        let count = word.matches(letter).count();
        if low <= count && count <= high {
            count1 += 1
        }
        if [&word[low-1..low], &word[high-1..high]].join("").matches(letter).count() == 1 {
            count2 += 1
        }
    }
    return [count1, count2]
}
