# Python Testing with Pytest
My notes and scratch code from [Python Testing with Pytest](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition).

<!-- MarkdownTOC levels="1,2" -->

- [0 Preface](#0-preface)
- [1 Getting Started](#1-getting-started)
- [2 Writing Test Functions](#2-writing-test-functions)
- [History](#history)

<!-- /MarkdownTOC -->



## 0 Preface
### Why pytest?
- Simplicity: tests are super easy to write (and read!).
- Almost zero cognitive overhead (just assert!).
- Runs tests written for unittest/nose.
- Integrates with CI/CD + automation tools.
- Extendable with custom + third-party plugins.
- Large, active [open-source dev community](https://github.com/pytest-dev/pytest).



## 1 Getting Started
### Running Pytest
- Test functions should start with `test`.
- Test classes should start with `Test`.
- Test files should start with `test_` or end with `_test`.
- Can specify test dirs, files, classes, functions, patterns, etc.

### Test Outcomes
| Outcome | Symbol | Notes                                  | Decorator                                        |
|:-------:|:------:|:---------------------------------------|:-------------------------------------------------|
| PASSED  |   .    | Test ran successfully.                 | –                                                |
| FAILED  |   F    | Test failed.                           | –                                                |
| SKIPPED |   s    | Test was skipped.                      | `@pytest.mark.skip()`<br>`@pytest.mark.skipif()` |
|  XFAIL  |   x    | Test was supposed to fail, and it did. | `@pytest.mark.xfail()`                           |
|  XPASS  |   X    | Test was supposed to fail, but passed. | `@pytest.mark.xfail()`                           |
|  ERROR  |   E    | Error occurred in fixture or hook.     | –                                                |



## 2 Writing Test Functions
### Failing with pytest.fail() and Exceptions
- A test fails if there is any uncaught exception. This can happen when:
    + `assert` statement fails (raises `AssertionError`).
    + Code explicitly calls `pytest.fail()`.
    + Any other exception is raised.
- Main drawback of `pytest.fail()` is no pytest assert rewriting.
- Main use case of `pytest.fail()` is for assertion helper functions.

### Structuring Test Functions
- Common pattern: arrange-act-assert/given-when-then.
- Anti-pattern: arrange-act-assert-act-assert... .
    + Doesn't focus on testing a single behavior.
    + Hard to determine original intent in future.



## History
- `2023/08/06` Read pp x-30.
