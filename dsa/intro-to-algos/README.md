# Intro to Algos
My notes and scratch code from the venerable [Introduction to Algorithms (CLRS)](http://mitpress.mit.edu/algorithms).

Anything reusable gets rolled into my [`enigmata`](https://github.com/jxcrw/enigmata/tree/main/tools/dsa) repo for use in LeetCode / Advent of Code.


## 1 The Role of Algorithms in Computing
### 1.1 Algorithms
- Algorithm: a well-defined computational procedure that takes some value(s) as input and produces some value(s) as output in finite time.
- Problem instance: the input needed to compute a solution to a problem.
- Correct algorithm: algorithm that halts (finishes in finite time) and outputs a correct solution for every problem instance.
- Data structure: a way to store and organize data to facilitate access to and modification of that data.
- NP-complete problem: problem for which no solution algorithm that runs in reasonable time is known.
- If an efficient algorithm exists for any one NP-complete problem, then efficient algorithms exist for all of them.
- Online algorithm: algorithm that receives its input over time rather than having all input present at start.

### 1.2 Algorithms as a technology
- Insertion sort vs merge sort:
    * Insertion sort time complexity = O(c<sub>1</sub>n<sup>2</sup>), merge sort complexity = O(c<sub>2</sub>n log n).
    * Wrt c<sub>1</sub> and c<sub>2</sub>, c<sub>1</sub> is usually less than c<sub>2</sub>.
    * For small input sizes, insertion sort is usually faster. For large input sizes, merge sort is faster.


## History
- 2023/01/20: Read pp 9-12.
- 2023/01/19: Read pp 3-8.
- 2023/01/18: Read pp xiii-xx.
