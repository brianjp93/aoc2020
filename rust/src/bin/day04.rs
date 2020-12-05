use std::fs;
use regex::Regex;
use std::collections::HashMap;


fn main() {
    let data = fs::read_to_string("./inputs/day4").unwrap();
    let groups = data.split("\n\n")
        .map(|x| {x.trim()})
        .collect::<Vec<&str>>();

    let passports = groups.into_iter().map(|x| {parse_passport(x)}).collect::<Vec<HashMap<String, String>>>();
    let mut count1 = 0;
    let mut count2 = 0;
    for passport in passports {
        if is_valid1(&passport) {
            count1 += 1;
        }
        if is_valid2(&passport) {
            count2 += 1;
        }
    }
    println!("Part 1: {:?}", count1);
    println!("Part 2: {:?}", count2);
}

fn parse_passport(data: &str) -> HashMap<String, String> {
    let mut map: HashMap<String, String> = HashMap::new();
    for line in data.split("\n") {
        for item in line.split(" ").into_iter().collect::<Vec<&str>>() {
            let item: Vec<&str> = item.split(":").collect();
            map.insert(item[0].to_string(), item[1].to_string());
        }
    }
    map
}

fn is_valid1(passport: &HashMap<String, String>) -> bool {
    if passport.len() == 8 {
        return true
    }
    passport.len() == 7 && passport.get("cid") == None
}

fn is_valid2(passport: &HashMap<String, String>) -> bool {
    [
        is_valid1(&passport),
        validate_hcl(&passport),
        validate_hgt(&passport),
        validate_ecl(&passport),
        validate_date(&passport, "byr".to_string(), 1920, 2002),
        validate_date(&passport, "iyr".to_string(), 2010, 2020),
        validate_date(&passport, "eyr".to_string(), 2020, 2030),
        validate_pid(&passport),
    ].iter().all(|x| *x)
}

fn validate_pid(passport: &HashMap<String, String>) -> bool {
    let re = Regex::new(r"^[0-9]{9}$").unwrap();
    let val = passport.get("pid");
    if val != None {
        let val = val.unwrap();
        return re.is_match(val)
    }
    false
}

fn validate_hcl(passport: &HashMap<String, String>) -> bool {
    let val = passport.get("hcl");
    if val != None {
        let val = val.unwrap();
        let re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
        return re.is_match(&val)
    }
    false
}

fn validate_hgt(passport: &HashMap<String, String>) -> bool {
    let re = Regex::new(r"^([0-9]+)(in|cm)$").unwrap();
    let val = passport.get("hgt");
    if val != None {
        let val = val.unwrap();
        let caps = re.captures(val);
        if caps.iter().len() > 0 {
            let caps = caps.unwrap();
            let height = caps.get(1).unwrap().as_str().parse::<usize>().unwrap();
            let height_type = caps.get(2).unwrap().as_str();
            if height_type == "in" {
                return (59..77).contains(&height)
            }
            else if height_type == "cm" {
                return (150..194).contains(&height)
            }
        }
    }
    false
}

fn validate_ecl(passport: &HashMap<String, String>) -> bool {
    let val = passport.get("ecl");
    if val != None {
        let val = val.unwrap();
        return ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&val.as_str())
    }
    false
}

fn validate_date(passport: &HashMap<String, String>, field: String, start: usize, end: usize) -> bool {
    let val = passport.get(&field);
    if val != None {
        let val = val.unwrap().parse::<usize>().unwrap();
        return (start..end+1).contains(&val)
    }
    false
}
