# Complete DSA Python
My notes and scratch code from the [The Complete Data Structures and Algorithms Course in Python](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/).

Anything reusable gets rolled into my [`pazuru/tools/dsa`](https://github.com/jxcrw/pazuru/tree/main/tools/dsa) repo for use in LeetCode / Advent of Code.

**Contents**
<!-- MarkdownTOC levels="1,2" -->

- [1: Introduction](#1-introduction)
- [2-4: Recursion](#2-4-recursion)
- [5-6: Big O Notation](#5-6-big-o-notation)
- [7: Arrays](#7-arrays)
- [8: Python Lists](#8-python-lists)
- [12: Dictionaries](#12-dictionaries)
- [13: Tuples](#13-tuples)
- [14: Linked Lists](#14-linked-lists)
- [19: Stacks](#19-stacks)
- [20: Queues](#20-queues)
- [22: Tree/Binary Tree](#22-treebinary-tree)

<!-- /MarkdownTOC -->
<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 1: Introduction
- Data structures are just ways of organizing data to make access to that data easier/faster/more efficient.
- An algorithm is just a set of steps for accomplishing some task. Examples:
    + Compression algorithms for audio and video data: AAC, MP3, JPEG, H.265 (all stuff you've heard of before).
    + Graph algorithms for stuff like Google Maps
- Companies only tend to focus on DSA during interviews because it's the best way they know of to evaluate candidate's problem solving skills and software engineering fundamentals in a limited time.

### Types of Data Structures
- Primitive: Pre-defined in programming language (integer, float, character, string, boolean)
- Non-primitive: User-defined, combine two or more primitives
    + Linear: Data items arranged in memory in a linear, sequential manner
        * Static: Associated memory locations fixed at compile time (array, etc.)
        * Dynamic: Associated memory locations change (linked list, static, queue, etc.)
    + Non-linear: Data item connected to other items, non-sequential in memory (tree, graph, etc.)

### Types of Algorithms
- Simple recursive algorithms
    + Calls itself
- Divide and conquer algorithms
    + Divide problem into smaller subproblems of the same type, solve subproblems recursively
    + Combine solutions to subproblems into solution to original problem
    + Examples: Quick sort and merge sort
- Dynamic programming algorithms
    + Worked based on memoization (remember past results and use them to find new results)
    + Generally used for optimization problems
- Greedy algorithms
    + Works in phases, at each phase we do the best we can without considering future consequences
    + Hope that choosing local optimum solution at each step, we will end up at global optimum solution
    + Also used for optimization problems
- Brute force algorithms
    + Simply try all possibilities until satisfactory solution is found
- Randomized algorithms
    + Use random number at least once during computation to make a decision
    + Examples: Quick sort algorithm

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 2-4: Recursion
- A way of solving a problem by having a function call itself. Properties:
    + Performing the same operation multiple times with different inputs
    + In every step we try smaller inputs to make the problem smaller
    + Base condition needed to stop recursion, otherwise infinite loop occurs
- System uses LIFO stack memory to remember/manage calls to recursive functions
- All recursive algorithms can be implemented
- Recursive algorithms can be very inefficient in memory space
- Recursion versus iteration:

|                  | Recursion | Iteration | Notes                                                                         |
|:-----------------|:----------|:----------|:------------------------------------------------------------------------------|
| Space efficient? | No        | Yes       | Iteration doesn't require stack memory                                        |
| Time efficient?  | No        | Yes       | Recursion incurs time overhead for push/pop operations on stack memory        |
| Easy to code?    | Yes       | No        | Recursion easier when we know problem can be divided into smaller subproblems |

- When to use recursion:
    + When problem can be broken into similar subproblems
    + When we are fine with extra time and space overhead
    + Need quick working solution more than efficient solution (recursion can be slow)
    + Relatively small inputs
    + Traversing pre-ordered trees
    + When using memoization to reduce time complexity
- When to avoid recursion:
    + Memory-constrained environments (mobile devices)
    + Time-critical applications (airbag deployment system)
    + Large inputs

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 5-6: Big O Notation
- Big O: Complexity ≤ worst case
- Big Ω: Complexity ≥ best case
- Big Θ: Worst case < complexity < best case
- O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

### Time Complexity
- How long algorithm takes to run
```python
array = [1, 2, 3, 4, 5]

# O(1): Constant time complexity
element = array[n] # Direct lookup

# O(n): Linear time complexity
for element in array:
    print(element) # Visiting every element in array once

# O(log n): Logarithmic time complexity
for i in range(0, len(array), 3):
    print(array[i]) # Only visiting some of the elements
# Binary search of sorted array is another example of logarithmic complexity

# O(n^2): Quadratic time complexity
for x in array:
    for y in array:
        print(x, y) # Visiting each element in array for each element in array

# O(2^n): Exponential time complexity
def fibonacci(n):
    assert n >= 0 and isinstance(n, int), 'n must be a non-negative integer!'
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Two recursive calls per call
```

### Space Complexity
- How much memory is needed to run algorithm
    + Array of size n ⇒ O(n)
    + Array of size n\*n ⇒ O(n^2)

```python
# O(n) space complexity
def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)

# O(1) space complexity
def pair_sum_sequence(n):
    sum = 0
    for i in range(0, n + 1):
        sum = sum + pair_sum(i, i + 1)
    return sum

def pair_sum(a, b):
    return a + b
```

### Drop Constants and Non-Dominant Terms
- As n → ∞, constants/non-dominant terms don't really matter
- O(2n)        → O(n)
- O(n^2 + n)   → O(n^2)
- O(n + log n) → O(n)
- O(2\*2^n + 1000n^100) → O(2^n)

#### Example
```python
def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0] # O(1)
    for index in range(1,len(sampleArray)): # O(n)
        if sampleArray[index] > biggestNumber: # O(1)
            biggestNumber = sampleArray[index] # O(1)
    print(biggestNumber) # O(1)

# O(1) + O(n) + O(1) + O(1) + O(1) ⇒ O(n)

```

#### Recursive Examples
```python
def findMaxNumRec(sampleArray, n): # M(n)
    if n == 1: # O(1)
       return sampleArray[0] # O(1)
    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1)) # M(n - 1)

# M(n) = O(1) + M(n - 1)
# M(1) = O(1)
# M(n - 1) = O(1) + M((n - 1) - 1)
# M(n - 2) = O(1) + M((n - 2) - 1)

# M(n) = 1 + 1 + M((n - 1) - 1)
# = 2 + M(n - 2)
# = 2 + 1 + M((n - 2) - 1)
# = 3 + M(n - 3)
# ...
# = a + M(n - a), substitute a = n - 1
# = n - 1 + M(n - n - 1)
# = n - 1 + 1
# = n
```

```python
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)

# O(2^n) = O(branches^depth)
```

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 7: Arrays
### What is an array?
- Stores data of the same type (traditionally)
- Elements located contiguously in memory (makes access efficient)
- Each element has unique index or key
- Size is predefined and cannot be modified

### Types of Arrays
- One-dimensional or multi-dimensional
- Think of 3D array as 2D array with a depth dimension as well
    + (First index is depth)

### Arrays in Memory
- Elements located sequentially in memory
- 2D and 3D arrays stored in memory as 1D array

### Array Operations
- Python uses list instead of traditional arrays
- But does have traditional arrays ([docs](https://docs.python.org/3/library/array.html))
    ```python
    from array import *
    my_array = array(typecode, [initializers]) #
    ```
- 1D array complexity
    | Operation          |          Time Complexity           | Space Complexity |
    |:-------------------|:----------------------------------:|:----------------:|
    | Creation           |                O(1)                |       O(n)       |
    | Insertion          | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |
    | Accessing          |                O(1)                |       O(1)       |
    | Traversal          |                O(n)                |       O(1)       |
    | Searching (linear) |                O(n)                |       O(1)       |
    | Deletion           | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |

- 2D array complexity
    | Operation            |           Time Complexity           | Space Complexity |
    |:---------------------|:-----------------------------------:|:----------------:|
    | Creation             |                O(1)                 |      O(mn)       |
    | Insertion of col/row | O(1) (end)<br>O(mn) (anywhere else) |       O(1)       |
    | Accessing            |                O(1)                 |       O(1)       |
    | Traversal            |                O(mn)                |       O(1)       |
    | Searching (linear)   |                O(mn)                |       O(1)       |
    | Deletion             | O(1) (end)<br>O(mn) (anywhere else) |       O(1)       |

### When to Use/Avoid
- When to use
    + To store multiple variables of same data type
    + When can leverage direct random access to elements
- When to avoid
    + When want to store multiple variables of different data types
    + Reserves specific amount of memory to store content
    + When array size could grow uncontrolably and thrash memory

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 8: Python Lists
- List: Data structure that holds an ordered collection of items
- Can contain items of different types

### Lists versus Arrays
- Both mutable.
- Both can be indexed and iterated.
- Both can be sliced.
- Arrays optimized for arithmetic operations.
- Lists can contain elements of different data types.
- Complexity
    | Operation          |          Time Complexity           | Space Complexity |
    |:-------------------|:----------------------------------:|:----------------:|
    | Creation           |                O(1)                |       O(n)       |
    | Insertion          | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |
    | Accessing          |                O(1)                |       O(1)       |
    | Traversal          |                O(n)                |       O(1)       |
    | Searching (linear) |                O(n)                |       O(1)       |
    | Deletion           | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |

(Same as 1D arrays)

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 12: Dictionaries
- Collection which is unordered (sort of), mutable, and indexed.
- Also known as associative array.
- If element added to dictionary causes a collision, it's added to the associated index as a linked list.
- Dictionary versus List
    |             Dictionary              |                 List                 |
    |:-----------------------------------:|:------------------------------------:|
    |              Unordered              |               Ordered                |
    |           Access via keys           |           Access via index           |
    |    Collection of key-value pairs    |        Collection of elements        |
    | Preferred when you have unique keys | Preferred when you have ordered data |
    |        No duplicate elements        |      Allows duplicate elements       |
- Complexity
    | Operation          |     Time Complexity      | Space Complexity |
    |:-------------------|:------------------------:|:----------------:|
    | Creation           |        O(len(d))         |       O(n)       |
    | Insertion          | O(1)<br>O(n) (amortized) |       O(1)       |
    | Accessing          |           O(1)           |       O(1)       |
    | Traversal          |           O(n)           |       O(1)       |
    | Searching (linear) |           O(n)           |       O(1)       |
    | Deletion           |           O(1)           |       O(1)       |

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 13: Tuples
- **Immutable** sequence of Python objects.
- Comparable and hashable (has value that remains same during its lifetime).
- Parentheses are standard but not required (`my_tuple = (1, 2)` rather than `my_tuple = 1, 2`).
- Stored in contiguous locations in memory.
- Main difference versus lists is mutability.
- Tuples generally used for heterogenous data, lists for homogenous data.
- Iterating through a tuple is faster than iterating through a list.
- Tuples can be used as keys in dictionaries.

- Complexity
    | Operation          | Time Complexity | Space Complexity |
    |:-------------------|:---------------:|:----------------:|
    | Creation           |      O(1)       |       O(n)       |
    | Accessing          |      O(1)       |       O(1)       |
    | Traversal          |      O(n)       |       O(1)       |
    | Searching (linear) |      O(n)       |       O(1)       |

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 14: Linked Lists
- Collection of independent nodes that may contain any type of data, where each node has a reference (link) to the next node.
- Very similar to a train (has head and tail, cars joined by links)
- Starts with head, which just has reference to next node.
- Each node consists of the value of the node and a reference to the next node.
- The reference/link is the memory location of the target node.
- Ends with tail that points to last node.
- Not stored contiguously in memory.
- Versus arrays:
    + Each element of linked list is an independent object
    + Variable size - size of linked list is not predefined
    + Insertion and removal operations in linked list are very efficient
    + Random access - accessing an element is very efficient in arrays (indexed), in linked list always need to iterate all sequentially
- Types:
    + Singly linked list - each element is simply a node plus a reference to the next node
    + Circular singly linked list - same as singly linked list except last node stores a reference to the first node
    + Doubly linked list - each node stores reference to previous node and next node
    + Circular doubly linked list - same as doubly linked list except first/last node have references to each other

- Complexity
    | Operation              | Time Complexity | Space Complexity |
    |:-----------------------|:---------------:|:----------------:|
    | Creation               |      O(1)       |       O(1)       |
    | Insertion              |      O(n)       |       O(1)       |
    | Searching (linear)     |      O(n)       |       O(1)       |
    | Traversal              |      O(n)       |       O(1)       |
    | Deletion (node)        |      O(n)       |       O(1)       |
    | Deletion (linked list) |      O(1)       |       O(1)       |

- Time complexity (versus array) (Note: some of these don't seem right but were what was presented)
    | Operation                   |  Array   | Linked List |
    |:----------------------------|:--------:|:-----------:|
    | Creation                    |   O(1)   |    O(1)     |
    | Insertion (first position)  |   O(1)   |    O(1)     |
    | Insertion (last position)   |   O(1)   |    O(1)     |
    | Insertion (nth position)    |   O(1)   |    O(n)     |
    | Searching (linear) unsorted |   O(n)   |    O(n)     |
    | Searching (linear) sorted   | O(log n) |    O(n)     |
    | Traversal                   |   O(n)   |    O(n)     |
    | Deletion (first position)   |   O(1)   |    O(1)     |
    | Deletion (last position)    |   O(1)   |  O(n)/O(1)  |
    | Deletion (nth position)     |   O(1)   |    O(n)     |
    | Deletion (self)             |   O(1)   |  O(n)/O(1)  |
    | Access nth element          |   O(1)   |    O(n)     |

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 19: Stacks
- Stores items in a last-in/first-out (LIFO) manner. Like a pile of dinner plates.
- Implementing with list versus linked list:
    + List: Easy to implement, but speed problem when large due to contiguous memory allocation.
    + Linked list: Harder to implement, but faster when large due to non-contiguous memory allocation.
- Good when LIFO functionality is required, or to reduce chance of data corruption.
- Bad when random access is required.

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 20: Queues
- Stores items in a first-in/first-out (FIFO) manner.
    + New items added to end. Old items popped from beginning.
- `collections.deque` - implemented as doubly-linked list.
- `queue` - multi-producer, multi-consumer queues.
    + Useful in threaded programming to exchange info safely between multiple threads.
    + Has FIFO, LIFO, and priority queues.
- `multiprocessing.Queue` - shared job queue implementation that allows queue items to be processed in parallel by multiple concurrent workers. Meant for sharing data between processes.

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## 22: Tree/Binary Tree
- Non-linear data structure with hierarchical relationships between elements.
- Each node has two components: data and references to children.
- Facilitates quicker and easier access to data vs linear DSes like arrays, LLs, stacks, queues.
- Convenient for naturally hierarchical data like folder structure, HTML/XML data, etc.
- Binary search tree performs fast search/insert/delete on sorted data.
- Self-balancing trees like AVL and red black trees guarantee O(log n) for search.
- Root: the top node that doesn't have a parent.
- Edge: link between a parent and a child.
- Leaf: node that has no children.
- Siblings: children of same parent.
- Ancestors: parent, grandparent, n-grandparent of a node.
- Depth: length of path from root to given node.
- Height: length of path from given node to the deepest node on its side.
- Tree depth: depth of root node (0).
- Tree height: height of root node.

### Binary Tree
- Each node has at most two children (left and right).
- Family of DSes (binary search tree, heap tree, AVL, red black tree, syntax tree).
- Full binary tree: each node has zero or two children.
- Perfect binary tree: all non-leaf nodes have two children at the same depth + all leaf nodes in same level.
- Complete binary tree: all levels filled except last level, which has nodes as left as possible.
- Balanced binary tree: all leaf nodes have same depth from root.
- Preorder traversal: root → left → right. DFS. Last visited is rightmost node of rightmost subtree.
- Inorder traversal: left → root → right. DFS. Last visited is rightmost node of rightmost subtree.
- Postorder traversal: left → right → root. DFS. Last visited is root node of overall tree.
- Levelorder traversal: level by level. BFS. Last visited is rightmost node of lowest level.
