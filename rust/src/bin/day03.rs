use std::fs;

const TREE: &str = "#";

fn main() {
    let data = fs::read_to_string("./inputs/day3").unwrap();
    let data = data.split("\n").filter(|x| {x != &""}).collect::<Vec<&str>>();
    let slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];
    let counts: Vec<usize> = slopes
        .iter()
        .map(|item| {count_trees(&data, item[0], item[1])})
        .collect();
    println!("Part 1: {}", &counts[1]);
    println!("Part 2: {:?}", counts.into_iter().fold(1, |x, y| {x * y}));
}

fn count_trees(data: &Vec<&str>, dx: usize, dy: usize) -> usize {
    let max_x: usize = data[0].len();
    let max_y: usize = data.len();
    let mut count = 0;
    let mut x = 0;
    let mut y = 0;
    while y < max_y {
        if data[y].chars().nth(x % max_x).unwrap().to_string() == TREE {
            count += 1;
        }
        x += dx;
        y += dy;
    }
    return count;
}


