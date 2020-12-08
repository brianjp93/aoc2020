use std::fs;
use std::collections::HashMap;
use regex::Regex;
use cached::proc_macro::cached;
use cached::SizedCache;

fn main() {
    let left_regex: regex::Regex = Regex::new(r"(\w+ \w+) bags contain").unwrap();
    let right_regex: regex::Regex = Regex::new(r"(\d+) (\w+ \w+)").unwrap();
    let data = fs::read_to_string("./inputs/day7").unwrap();
    let data: Vec<String> = data.trim().split("\n")
        .map(|x| { x.trim().to_string() })
        .collect();

    let mut hash: HashMap<String, Vec<(String, i32)>> = HashMap::new();
    for line in &data {
        let bag = left_regex.captures(&line).unwrap();
        let right = right_regex.find_iter(&line);
        let mut d: Vec<(String, i32)> = Vec::new();
        for mat in right.into_iter() {
            let right = right_regex.captures(mat.as_str()).unwrap();
            d.push((
                right.get(2).unwrap().as_str().to_string(),
                right.get(1).unwrap().as_str().parse::<i32>().unwrap(),
            ));
        }
        hash.insert(bag.get(1).unwrap().as_str().to_string(), d);
    }
    let count: i32 = hash.keys().map(|bag| {
        if check_bag(&bag, &"shiny gold".to_string(), &hash) {
            1
        }
        else {
            0
        }
    }).sum();
    println!("{:?}", count);
    println!("{:?}", count_bags(&"shiny gold".to_string(), 0, &hash));
}

#[cached(
    type="SizedCache<String, bool>",
    create="{ SizedCache::with_size(1000) }",
    convert = r#"{ format!("{}{}", bag, bagtype) }"#
)]
fn check_bag(bag: &String, bagtype: &String, bags: &HashMap<String, Vec<(String, i32)>>) -> bool {
    for inner in bags.get(bag).unwrap() {
        if &inner.0 == bagtype || check_bag(&inner.0, bagtype, bags) {
            return true
        }
    }
    return false
}

fn count_bags(bag: &String, start: i32, bags: &HashMap<String, Vec<(String, i32)>>) -> i32 {
    return start + bags.get(bag).unwrap().into_iter().map(|inner| {
        inner.1 * count_bags(&inner.0, 1, bags)
    }).sum::<i32>()
}
