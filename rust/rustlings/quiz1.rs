// quiz1.rs
// This is a quiz for the following sections:
// - Variables
// - Functions
// - If

// Mary is buying apples. The price of an apple is calculated as follows:
// - An apple costs 2 rustbucks.
// - If Mary buys more than 40 apples, each apple only costs 1 rustbuck!
// Write a function that calculates the price of an order of apples given
// the quantity bought. No hints this time!

// Put your function here!
fn calc_apple_price(quantity: u32) -> u32 {
    let price_per = if quantity > 40 {1} else {2};
    let total = quantity * price_per;
    return total;
}

// Don't modify this function!
#[test]
fn verify_test() {
    let price1 = calc_apple_price(35);
    let price2 = calc_apple_price(40);
    let price3 = calc_apple_price(41);
    let price4 = calc_apple_price(65);

    assert_eq!(70, price1);
    assert_eq!(80, price2);
    assert_eq!(41, price3);
    assert_eq!(65, price4);
}
