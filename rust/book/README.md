# The Book
My notes and code from [The Rust Programming Language](https://doc.rust-lang.org/book/).


### [1. Getting Started](https://doc.rust-lang.org/book/ch01-00-getting-started.html)
- `main()` always executed first.
- `cargo new`: Create new project.
- `cargo build`: Build project.
- `cargo run`: Build and run project.
- `cargo check`: Check that code compiles, but don't emit binary.
- `cargo update`: Update to latest acceptable versions of crates specified in `cargo.toml`.
- Code: [`hello_world`](./src/hello_world.rs), [`hello_cargo`](./src/hello_cargo.rs)


### [2. Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)
- Variables immutable by default.
- References also immutable by default.
- `match` expression made up of _arms_. Arms consist of a _pattern_ to match + code to run for that arm.
- `Result` type is an enum with two _variants_: `Ok` and `Err`.
- `"str".trim()` to trim whitespace off a string.
- `"str".parse()` to convert strings to another type.
- Code: [`guess`](./src/guess.rs)


### [3. Common Programming Concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)
#### [3.1 Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- Constants (`const`): always immutable, type must be annotated, declarable in any scope, must be constant expression.
- Shadowing: allows a few transformations on a variable, then variable becomes immutable.
    + Makes it possible to change type of value bound to variable.
- Code: [`variables`](./src/variables.rs)

#### [3.2 Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html)



### [Appendix E - Editions](https://doc.rust-lang.org/book/appendix-05-editions.html)
- New Rust edition released every two or three years.
- Each edition collects features from previous six-week release cycles into meaningful package.


### [Appendix G - How Rust is Made](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html)
- Developed on train schedule with three release channels/branches: nightly/`master`, beta/`beta`, and stable/`stable`.
    * All dev done on `master`, and new release created every night.
    * `beta` branches from `master` to create a beta release every six weeks.
    * Regressions found in `beta` fixed on `master` and backported to `beta`.
    * `stable` branches from `beta` six weeks after that beta was created to create a stable release.
- Unstable features protected behind feature flags and only usable in nightly releases.
- Stability without stagnation.


## History
- 2022/12/16: Read Appendices E/G + chapters 1-2.
- 2022/12/21: Read Appendix A + chapter 3.1.
