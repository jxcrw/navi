# Python Testing with Pytest
My notes and scratch code from [Python Testing with Pytest](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition).

<!-- MarkdownTOC levels="1,2" -->

- [0 Preface](#0-preface)
- [1 Getting Started](#1-getting-started)
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
- Can specify test files, test dirs, specific tests.

### Test Outcomes
| Outcome | Symbol | Notes                                  | Decorator                                        |
|:-------:|:------:|:---------------------------------------|:-------------------------------------------------|
| PASSED  |   .    | Test ran successfully.                 | –                                                |
| FAILED  |   F    | Test failed.                           | –                                                |
| SKIPPED |   s    | Test was skipped.                      | `@pytest.mark.skip()`<br>`@pytest.mark.skipif()` |
|  XFAIL  |   x    | Test was supposed to fail, and it did. | `@pytest.mark.xfail()`                           |
|  XPASS  |   X    | Test was supposed to fail, but passed. | `@pytest.mark.xfail()`                           |
|  ERROR  |   E    | Error occurred in fixture or hook.     | –                                                |



## History
- `2023/08/06` Read pp x-#.