fn main() {
    // Variables and mutability
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}\n");

    // Constants
    const THREE_HOURS_IN_SECONDS: u32 = 3 * 3600;
    println!("{THREE_HOURS_IN_SECONDS}\n");

    // Shadowing
    let x = 5;
    let x = x + 1;
    {
        let x = x * 2;
        println!("inner scope: {x}");
    }
    println!("outer scope: {x}\n");

    let spaces = "   ";
    let spaces = spaces.len();
    println!("n_spaces: {spaces}");
}
