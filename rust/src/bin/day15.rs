use std::collections::HashMap;

type N = i128;
type NList = Vec<i128>;

fn main() {
    let d: NList = vec![17, 1, 3, 16, 19, 0];
    let init_length = d.len() as usize;

    for n in &[2020, 30000000] {
        let dc = d.clone();
        let mut history: HashMap<N, NList> = HashMap::with_capacity(*n);
        let mut i = 0 as usize;
        let mut speak: N = -1;
        while &i < n {
            if i < init_length {
                speak = dc[i];
            }
            else if let Some(x) = history.get_mut(&speak) {
                if x.len() > 1 {
                    speak = x[x.len()-1] - x[x.len()-2];
                }
                else {
                    speak = 0;
                }
            }
            else {
                speak = 0;
            }

            if let Some(x) = history.get_mut(&speak) {
                x.push((i + 1) as N);
                if x.len() > 2 {
                    x.drain(0..1);
                }
            }
            else {
                history.insert(speak, vec![(i+1) as N]);
            }
            i += 1;
        }
        println!("{:?}", speak)
    }
}
