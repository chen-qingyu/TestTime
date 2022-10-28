fn main() {
    const N: f64 = 1.0E7;
    let mut x: f64 = 0.0;
    let mut y: f64;
    let mut hits: f64 = 0.0;
    while x * x < N {
        y = 0.0;
        while y * y < N {
            if x * x + y * y < N {
                hits += 1.0;
            }
            y += 1.0;
        }
        x += 1.0;
    }
    println!("{}", (hits / N) * 4.0);
}
