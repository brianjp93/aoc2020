use std::fs;
use std::collections::HashSet;


fn main() {
    let data = fs::read_to_string("./inputs/day5").unwrap();
    let data = data.trim().split("\n")
        .map(|x| {x.trim()})
        .collect::<Vec<&str>>();
    let seat_ids = data.into_iter().map(|word| {
        let [row, col] = find_seat(word.to_string());
        return row * 8 + col
    }).collect::<Vec<usize>>();
    let max_id = seat_ids.iter().max().unwrap();
    let my_seat = find_my_seat(&seat_ids);

    println!("Part 1: {:?}", max_id);
    println!("Part 2: {:?}", my_seat);
}

fn find_my_seat(seat_ids: &Vec<usize>) -> usize {
    let seat_id_set: HashSet<usize> = seat_ids.clone().into_iter().collect();
    for x in &seat_id_set {
        if !seat_id_set.contains(&(x + 1)) && seat_id_set.contains(&(x + 2)) {
            return x + 1
        }
    }
    0
}

fn find_seat(word: String) -> [usize; 2] {
    let part1 = &word[..7];
    let part2 = &word[7..];

    let mut start = 1;
    let mut end = 128;
    for ch in part1.chars() {
        let size = end - start + 1;
        if ch == 'F' {
            end -= (size / 2) as usize;
        }
        else if ch == 'B' {
            start += (size / 2) as usize
        }
    }
    let row = start - 1;

    let mut start = 1;
    let mut end = 8;
    for ch in part2.chars() {
        let size = end - start + 1;
        if ch == 'L' {
            end -= (size / 2) as usize;
        }
        else if ch == 'R' {
            start += (size / 2) as usize
        }
    }
    let col = start - 1;
    [row, col]
}
