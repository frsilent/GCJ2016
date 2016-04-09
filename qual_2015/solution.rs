#[allow(unused_variables)]

use std::error::Error;
use std::env;
use std::io::prelude::*;
use std::fs::File;
use std::io::BufReader;
use std::path::Path;

fn main() {
    let file_name = std::env::args().nth(1).unwrap();
    let path = Path::new(&file_name);

    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("Unable to open {}: {}", display, Error::description(&why)),
        Ok(file) => file,
    };

    let mut reader = BufReader::new(file);
    let mut buffer = String::new();

    reader.read_line(&mut buffer);
    let test_cases = &buffer;
    println!("{}", test_cases);

    // reader.read_line(&mut buffer);
    // println!("{}", buffer);

    // for line in file.lines() {
    //     let l = line.unwrap();
    //     println!("{}", l);
    // }


    // let mut file = File::open(&file_name).unwrap();
    // let mut file = fs::File::open(file_name);

    // file.read_to_end(&mut file_buffer).unwrap();

    // let file_buffer = file_buffer;

    println!("{}", file_name);
}