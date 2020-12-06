use std::fs;
use std::collections::HashSet;


fn main() {
    let data = fs::read_to_string("./inputs/day6").unwrap();
    let data = data.trim().split("\n\n")
        .map(|x| {x.trim()})
        .collect::<Vec<&str>>();

    let mut inters: Vec<HashSet<char>> = Vec::new();
    let mut unions: Vec<HashSet<char>> = Vec::new();
    for group in data {
        let people: Vec<&str> = group.split("\n").collect();
        let mut groupsets: Vec<HashSet<char>> = Vec::new();
        for person in people {
            groupsets.push(person.chars().collect::<HashSet<char>>());
        }
        let first = groupsets[0].clone();
        let inter = groupsets.clone().iter().fold(first.clone(), |x, y| {
            x.intersection(&y).cloned().collect()
        });
        let union = groupsets.iter().fold(first, |x, y| {
            x.union(&y).cloned().collect()
        });
        inters.push(inter);
        unions.push(union);
    }
    println!("Part 1: {:?}", unions.iter().map(|x| { x.len() }).sum::<usize>());
    println!("Part 2: {:?}", inters.iter().map(|x| { x.len() }).sum::<usize>());
}
