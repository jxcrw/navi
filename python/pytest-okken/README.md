# Python Testing with Pytest
My notes and scratch code from [Python Testing with Pytest](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition).

<!-- MarkdownTOC levels="1,2" -->

- [0 Preface](#0-preface)
- [1 Getting Started](#1-getting-started)
- [2 Writing Test Functions](#2-writing-test-functions)
- [3 Fixtures](#3-fixtures)
- [4 Builtin Fixtures](#4-builtin-fixtures)
- [5 Parameterization](#5-parameterization)
- [6 Markers](#6-markers)
- [7 Strategy](#7-strategy)
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



## 3 Fixtures
- Functions that run before/after tests, get system/data into known state.
- Strong fixturing support in pytest.

### Fixture Scope
- `@pytest.fixture(scope="<SCOPE>")`
- Scopes: `function`, `class`, `module`, `package`, `session`
- Use a `conftest.py` file to share fixtures among multiple test files.
- Use `pytest --fixtures` to see where fixtures are defined.
- Use `pytest --fixtures-per-test` to see what fixtures are used by each test.
- Can scaffold fixtures to ensure tests don't rely on run order ("test isolation" → golden rule!).
- Can use multiple fixtures per test.

### Advanced Fixture Scoping
- Can define custom scope function with logic and pass it by name as a fixture scope to achieve dynamic scoping.
    + But seems like more complicated than it's worth for many basic use cases.
- `@pytest.fixture(autouse=True)` for fixtures that always run without being explicitly called.



## 4 Builtin Fixtures
- `tmp_path` creates temp directory (function scope).
- `tmp_path_factory` can create multiple temp directories (session scope).
- `capsys` to capture output written to stdout and stderr.
- `monkeypatch` to dynamically modify class or module at test runtime.
- Many more that you don't need to worry about unless you actually have a use case for them.



## 5 Parameterization
- Way to use a single test function to test many test cases.
- Test function parameterization: `@pytest.mark.parametrize("param_name", ["param_val1", "param_val2", ...])`
- Fixture parameterization: `@pytest.fixture(params=["param_val1", "param_val2", ...])`
- Same test, different data ⇒ lean towards function parameterization.
- Same test, different start state ⇒ lean towards fixture parameterization.



## 6 Markers
- Used to indicate that a test is special in some way, or as tags/labels.

| Built-in Marker                 | Description                                             |
|:--------------------------------|:--------------------------------------------------------|
| `@pytest.mark.skip()`           | Skips a test, with an optional reason.                  |
| `@pytest.mark.skipif()`         | Skips test if any of the conditions are True.           |
| `@pytest.mark.xfail()`          | Indicates that a test is expected to fail.              |
| `@pytest.mark.parametrize()`    | Test function parameterization.                         |
| `@pytest.mark.usefixtures()`    | Indicates that a test needs all the specified fixtures. |
| `@pytest.mark.filterwarnings()` | Adds a warning filter to the given test.                |

### Custom Markers
- `@pytest.mark.<custom_marker>` + add to `pytest.ini`.
- Can be used at test, file, or class level.
- Third-party package [Faker](https://faker.readthedocs.io/en/master/) provides `faker` fixture to generate fake data.



## 7 Strategy
- Totally architecture-dependent. User-visible features usually a good place to start.
- Consider: security, performance, loading, input validation, etc.
- Test by application layer (UI/API/DB/etc.).
    + Here, UI/DB are thin to isolate dependencies, and so that testing API gives more bang for buck.
- Test by:
    + Recent - new features/fixes/refactors/etc.
    + Core - things that must work for product to be useful.
    + Risk - perhaps like third-party code .
    + Problematic - things that frequently break or get bug reports.
    + Expertise - features/algos only understood by a few people.
- Brainstorming test cases:
    + Happy path
    + Interesting input sets
    + Interesting starting states
    + Interesting ending states
    + Possible error states
- Write explicit strategy and list cases before writing test code.
- Document bugfixes with tests.
- Test enough to sleep soundly at night.



## History
- `2023/08/07` Read pp 96-111. `test-strategy`
- `2023/08/07` Read pp 73-95. `markers`
- `2023/08/07` Read pp 61-72. `parameterization`
- `2023/08/07` Read pp 49-60. `builtin-fixtures`
- `2023/08/07` Read pp 31-48. `fixtures`
- `2023/08/06` Read pp x-30. `intro` `install` `test-functions`
