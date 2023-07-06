# The Book
My notes and code from [The Rust Programming Language](https://doc.rust-lang.org/book/).

<!-- MarkdownTOC levels="1,2" -->

- [1. Getting Started](#1-getting-started)
- [2. Guessing Game](#2-guessing-game)
- [3. Common Programming Concepts](#3-common-programming-concepts)
- [Appendix B: Operators and Symbols](#appendix-b-operators-and-symbols)
- [Appendix E - Editions](#appendix-e---editions)
- [Appendix G - How Rust is Made](#appendix-g---how-rust-is-made)
- [History](#history)

<!-- /MarkdownTOC -->
## [1. Getting Started](https://doc.rust-lang.org/book/ch01-00-getting-started.html)
- `main()` always executed first.
- `cargo new`: Create new project.
- `cargo build`: Build project.
- `cargo run`: Build and run project.
- `cargo check`: Check that code compiles, but don't emit binary.
- `cargo update`: Update to latest acceptable versions of crates specified in `cargo.toml`.
- Code: [`hello`](./src/hello.rs)


## [2. Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)
- Variables immutable by default.
- References also immutable by default.
- `match` expression made up of _arms_. Arms consist of a _pattern_ to match + code to run for that arm.
- `Result` type is an enum with two _variants_: `Ok` and `Err`.
- `"str".trim()` to trim whitespace off a string.
- `"str".parse()` to convert strings to another type.
- Code: [`guess`](./src/guess.rs)


## [3. Common Programming Concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)
### [3.1 Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- Constants (`const`): always immutable, type must be annotated, declarable in any scope, must be constant expression.
- Shadowing: allows a few transformations on a variable, then variable becomes immutable.
    + Makes it possible to change type of value bound to variable.
- Code: [`variables`](./src/variables.rs)


### [3.2 Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- Scalar type: represents a single value. Four primary scalar types: ints, floats, bools, and chars.
- Compound type: group multiple values together. Two primitive compound types: tuples and arrays.
- Integers:
    * Signed (`i8/16/32/64/128`; range -2<sup>n-1</sup> to 2<sup>n-1</sup> - 1) or unsigned (`u8/16/32/64/128`; range 0 to 2<sup>n</sup> - 1).
    * Signed numbers stored using two's complement representation.
    * Overflows: panic in debug builds, two's complement-wrap in release builds.
    * Default is `i32`.
    * Examples:

| Number literals  | Example       |
|------------------|:-------------:|
| Decimal          | `98_222`      |
| Hex              | `0xff`        |
| Octal            | `0o77`        |
| Binary           | `0b1111_0000` |
| Byte (`u8` only) | `b'A'`        |
| Suffixed         | `57u8`        |


- Floats:
    * `f32` and `f64`, both signed. `f32` is single-precision, `f64` is double-precision. Default is `f64`.
    * Declare implicitly with dot: `let x = 2.0;`.
- Operations:
    * Standard `+`, `-`, `*`, `/`, `%`. On ints, `/` does integer division.
- Booleans: `bool`. `true` and `false`.
- Characters: `char`. Use single quotes: `let c = 'z';`.
- Tuples
    * Collection of values of possibly different types. Length is fixed.
    * Ex: `let tup: (i32, f64, u8) = (500, 6.4, 1);`
    * Destructuring: `let (x, y, z) = tup;`
    * Direct access: `let x = tup.0;`
    * Empty tuple written `()` and called _unit_.
- Arrays:
    * Collection of values of same type. Length is fixed.
    * Data allocated on stack rather than heap.
    * Use when you know the number of elements won't change (e.g. months of the year).
    * Ex: `let a = [1, 2, 3, 4, 5];`
    * Ex with type: `let a: [i32; 5] = [1, 2, 3, 4, 5];`
    * Ex homogenous: `let a = [3; 5];` (array containing five threes)
    * Direct access: `let first = a[0];`
    * OOB access results in panic at runtime.


### [3.3 Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)



## Appendix B: Operators and Symbols
Table B-1: Operators

| Operator | Example | Explanation | Overloadable? |
|----------|---------|-------------|---------------|
| `!` | `ident!(...)`, `ident!{...}`, `ident![...]` | Macro expansion | |
| `!` | `!expr` | Bitwise or logical complement | `Not` |
| `!=` | `expr != expr` | Nonequality comparison | `PartialEq` |
| `%` | `expr % expr` | Arithmetic remainder | `Rem` |
| `%=` | `var %= expr` | Arithmetic remainder and assignment | `RemAssign` |
| `&` | `&expr`, `&mut expr` | Borrow | |
| `&` | `&type`, `&mut type`, `&'a type`, `&'a mut type` | Borrowed pointer type | |
| `&` | `expr & expr` | Bitwise AND | `BitAnd` |
| `&=` | `var &= expr` | Bitwise AND and assignment | `BitAndAssign` |
| `&&` | `expr && expr` | Short-circuiting logical AND | |
| `*` | `expr * expr` | Arithmetic multiplication | `Mul` |
| `*=` | `var *= expr` | Arithmetic multiplication and assignment | `MulAssign` |
| `*` | `*expr` | Dereference | `Deref` |
| `*` | `*const type`, `*mut type` | Raw pointer | |
| `+` | `trait + trait`, `'a + trait` | Compound type constraint | |
| `+` | `expr + expr` | Arithmetic addition | `Add` |
| `+=` | `var += expr` | Arithmetic addition and assignment | `AddAssign` |
| `,` | `expr, expr` | Argument and element separator | |
| `-` | `- expr` | Arithmetic negation | `Neg` |
| `-` | `expr - expr` | Arithmetic subtraction | `Sub` |
| `-=` | `var -= expr` | Arithmetic subtraction and assignment | `SubAssign` |
| `->` | `fn(...) -> type`, <code>&vert;...&vert; -> type</code> | Function and closure return type | |
| `.` | `expr.ident` | Member access | |
| `..` | `..`, `expr..`, `..expr`, `expr..expr` | Right-exclusive range literal | `PartialOrd` |
| `..=` | `..=expr`, `expr..=expr` | Right-inclusive range literal | `PartialOrd` |
| `..` | `..expr` | Struct literal update syntax | |
| `..` | `variant(x, ..)`, `struct_type { x, .. }` | "And the rest" pattern binding | |
| `...` | `expr...expr` | (Deprecated, use `..=` instead) In a pattern: inclusive range pattern | |
| `/` | `expr / expr` | Arithmetic division | `Div` |
| `/=` | `var /= expr` | Arithmetic division and assignment | `DivAssign` |
| `:` | `pat: type`, `ident: type` | Constraints | |
| `:` | `ident: expr` | Struct field initializer | |
| `:` | `'a: loop {...}` | Loop label | |
| `;` | `expr;` | Statement and item terminator | |
| `;` | `[...; len]` | Part of fixed-size array syntax | |
| `<<` | `expr << expr` | Left-shift | `Shl` |
| `<<=` | `var <<= expr` | Left-shift and assignment | `ShlAssign` |
| `<` | `expr < expr` | Less than comparison | `PartialOrd` |
| `<=` | `expr <= expr` | Less than or equal to comparison | `PartialOrd` |
| `=` | `var = expr`, `ident = type` | Assignment/equivalence | |
| `==` | `expr == expr` | Equality comparison | `PartialEq` |
| `=>` | `pat => expr` | Part of match arm syntax | |
| `>` | `expr > expr` | Greater than comparison | `PartialOrd` |
| `>=` | `expr >= expr` | Greater than or equal to comparison | `PartialOrd` |
| `>>` | `expr >> expr` | Right-shift | `Shr` |
| `>>=` | `var >>= expr` | Right-shift and assignment | `ShrAssign` |
| `@` | `ident @ pat` | Pattern binding | |
| `^` | `expr ^ expr` | Bitwise exclusive OR | `BitXor` |
| `^=` | `var ^= expr` | Bitwise exclusive OR and assignment | `BitXorAssign` |
| <code>&vert;</code> | <code>pat &vert; pat</code> | Pattern alternatives | |
| <code>&vert;</code> | <code>expr &vert; expr</code> | Bitwise OR | `BitOr` |
| <code>&vert;=</code> | <code>var &vert;= expr</code> | Bitwise OR and assignment | `BitOrAssign` |
| <code>&vert;&vert;</code> | <code>expr &vert;&vert; expr</code> | Short-circuiting logical OR | |
| `?` | `expr?` | Error propagation | |


Table B-2: Stand-Alone Syntax

| Symbol | Explanation |
|--------|-------------|
| `'ident` | Named lifetime or loop label |
| `...u8`, `...i32`, `...f64`, `...usize`, etc. | Numeric literal of specific type |
| `"..."` | String literal |
| `r"..."`, `r#"..."#`, `r##"..."##`, etc. | Raw string literal, escape characters not processed |
| `b"..."` | Byte string literal; constructs an array of bytes instead of a string |
| `br"..."`, `br#"..."#`, `br##"..."##`, etc. | Raw byte string literal, combination of raw and byte string literal |
| `'...'` | Character literal |
| `b'...'` | ASCII byte literal |
| <code>&vert;...&vert; expr</code> | Closure |
| `!` | Always empty bottom type for diverging functions |
| `_` | "Ignored" pattern binding; also used to make integer literals readable |


Table B-3: Path-Related Syntax

| Symbol | Explanation |
|--------|-------------|
| `ident::ident` | Namespace path |
| `::path` | Path relative to the crate root (i.e., an explicitly absolute path) |
| `self::path` | Path relative to the current module (i.e., an explicitly relative path).
| `super::path` | Path relative to the parent of the current module |
| `type::ident`, `<type as trait>::ident` | Associated constants, functions, and types |
| `<type>::...` | Associated item for a type that cannot be directly named (e.g., `<&T>::...`, `<[T]>::...`, etc.) |
| `trait::method(...)` | Disambiguating a method call by naming the trait that defines it |
| `type::method(...)` | Disambiguating a method call by naming the type for which it’s defined |
| `<type as trait>::method(...)` | Disambiguating a method call by naming the trait and type |


Table B-4: Generics

| Symbol | Explanation |
|--------|-------------|
| `path<...>` | Specifies parameters to generic type in a type (e.g., `Vec<u8>`) |
| `path::<...>`, `method::<...>` | Specifies parameters to generic type, function, or method in an expression; often referred to as turbofish (e.g., `"42".parse::<i32>()`) |
| `fn ident<...> ...` | Define generic function |
| `struct ident<...> ...` | Define generic structure |
| `enum ident<...> ...` | Define generic enumeration |
| `impl<...> ...` | Define generic implementation |
| `for<...> type` | Higher-ranked lifetime bounds |
| `type<ident=type>` | A generic type where one or more associated types have specific assignments (e.g., `Iterator<Item=T>`) |


Table B-5: Trait Bound Constraints

| Symbol | Explanation |
|--------|-------------|
| `T: U` | Generic parameter `T` constrained to types that implement `U` |
| `T: 'a` | Generic type `T` must outlive lifetime `'a` (meaning the type cannot transitively contain any references with lifetimes shorter than `'a`) |
| `T: 'static` | Generic type `T` contains no borrowed references other than `'static` ones |
| `'b: 'a` | Generic lifetime `'b` must outlive lifetime `'a` |
| `T: ?Sized` | Allow generic type parameter to be a dynamically sized type |
| `'a + trait`, `trait + trait` | Compound type constraint |


Table B-6: Macros and Attributes

| Symbol | Explanation |
|--------|-------------|
| `#[meta]` | Outer attribute |
| `#![meta]` | Inner attribute |
| `$ident` | Macro substitution |
| `$ident:kind` | Macro capture |
| `$(…)…` | Macro repetition |
| `ident!(...)`, `ident!{...}`, `ident![...]` | Macro invocation |


Table B-7: Comments

| Symbol | Explanation |
|--------|-------------|
| `//` | Line comment |
| `//!` | Inner line doc comment |
| `///` | Outer line doc comment |
| `/*...*/` | Block comment |
| `/*!...*/` | Inner block doc comment |
| `/**...*/` | Outer block doc comment |


Table B-8: Tuples

| Symbol | Explanation |
|--------|-------------|
| `()` | Empty tuple (aka unit), both literal and type |
| `(expr)` | Parenthesized expression |
| `(expr,)` | Single-element tuple expression |
| `(type,)` | Single-element tuple type |
| `(expr, ...)` | Tuple expression |
| `(type, ...)` | Tuple type |
| `expr(expr, ...)` | Function call expression; also used to initialize tuple `struct`s and tuple `enum` variants |
| `expr.0`, `expr.1`, etc. | Tuple indexing |


Table B-9: Curly Brackets

| Context      | Explanation      |
|--------------|------------------|
| `{...}`      | Block expression |
| `Type {...}` | `struct` literal |


Table B-10: Square Brackets

| Context | Explanation |
|---------|-------------|
| `[...]` | Array literal |
| `[expr; len]` | Array literal containing `len` copies of `expr` |
| `[type; len]` | Array type containing `len` instances of `type` |
| `expr[expr]` | Collection indexing. Overloadable (`Index`, `IndexMut`) |
| `expr[..]`, `expr[a..]`, `expr[..b]`, `expr[a..b]` | Collection indexing pretending to be collection slicing, using `Range`, `RangeFrom`, `RangeTo`, or `RangeFull` as the "index" |


## [Appendix E - Editions](https://doc.rust-lang.org/book/appendix-05-editions.html)
- New Rust edition released every two or three years.
- Each edition collects features from previous six-week release cycles into meaningful package.


## [Appendix G - How Rust is Made](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html)
- Developed on train schedule with three release channels/branches: nightly/`master`, beta/`beta`, and stable/`stable`.
    * All dev done on `master`, and new release created every night.
    * `beta` branches from `master` to create a beta release every six weeks.
    * Regressions found in `beta` fixed on `master` and backported to `beta`.
    * `stable` branches from `beta` six weeks after that beta was created to create a stable release.
- Unstable features protected behind feature flags and only usable in nightly releases.
- Stability without stagnation.


## History
- `2023/07/05` Tombstone read indefinitely (器用貧乏 / Rust curiosity sated). ☠️
- `2022/12/16` Read Appendices E/G + chapters 1-2.
- `2022/12/21` Read Appendix A + chapter 3.1.
- `2022/12/26` Read chapter 3.2 and Appendix B.
