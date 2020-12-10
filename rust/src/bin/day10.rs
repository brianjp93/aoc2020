use std::fs;
use std::collections::HashMap;

type GenNum = i64;
type Data = Vec<GenNum>;

fn main() {
    let d = fs::read_to_string("./inputs/day10").unwrap();
    let mut d: Data = d.trim().split("\n")
        .filter(|x| x != &"")
        .map(|x| { x.trim().parse::<GenNum>().unwrap() })
        .collect();
    d.sort();
    d.insert(0, 0);
    d.push(d[d.len()-1] + 3);
    let mut diffs: HashMap<GenNum, GenNum> = HashMap::new();
    for (i, n) in d[..d.len()-1].iter().enumerate() {
        let diff = d[i+1] - n;
        if let Some(x) = diffs.get_mut(&diff) {
            *x += 1;
        }
        else {
            diffs.insert(diff, 1);
        }
    }
    println!("Part 1: {:?}", diffs.get(&(1 as GenNum)).unwrap() * diffs.get(&(3 as GenNum)).unwrap());
    println!("Part 2: {:?}", c(&d));
}


fn c(d: &Data) -> GenNum {
    let mut cache: Data = d.iter().map(|_| 0 as GenNum).collect();
    cache[0] = 1;
    for (i, n) in d.iter().enumerate() {
        for x in 1..4 {
            if i >= x && n - d[i-x] <= 3 {
                cache[i] += cache[i-x];
            }
        }
    }
    *cache.last().unwrap()
}
