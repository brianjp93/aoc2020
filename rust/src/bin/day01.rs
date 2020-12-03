use std::fs;
use std::collections::HashSet;

fn main() {
    let data: HashSet<usize> = fs::read_to_string("./inputs/day1")
        .unwrap()
        .split("\n").collect::<Vec<&str>>().into_iter()
        .filter(|x| {x != &""})
        .map(|x| {x.parse::<usize>().unwrap()})
        .collect::<Vec<usize>>()
        .into_iter().collect();
    let out = find_group(&data, 2020, 2);
    println!("{:?}", out.iter().fold(1, |x, y| { x*y }));
    let out = find_group(&data, 2020, 3);
    println!("{:?}", out.iter().fold(1, |x, y| { x*y }));
}

fn find_group(data: &HashSet<usize>, n: isize, count: usize) -> Vec<usize> {
    if n < 0 { return vec![] }
    for i in data.into_iter() {
        if count <= 2 {
            if n - *i as isize > 0 && data.contains(&(n as usize - i)) {
                return vec![*i, n as usize - i]
            }
        }
        else {
            let mut new_data = data.clone();
            new_data.remove(i);
            let mut possible = find_group(&new_data, n - *i as isize, count-1);
            if possible.len() > 0 {
                possible.push(*i);
                return possible
            }
        }
    }
    return vec![]
}
