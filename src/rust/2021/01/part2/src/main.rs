
use std::str;

fn main() {
    let input = str::from_utf8(include_bytes!("../../input.txt")).unwrap();

    let i32_inp = input
    .lines()
    .map(|line| {
        line.parse::<i32>()
            .expect("")
    })
    .collect::<Vec<_>>();
    let sum: i32 = i32_inp.windows(2)
    
    println!("The result is: {:?}", sum)
}
