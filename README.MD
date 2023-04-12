
# Learn Python with Unit Tests

This is a little example for learning Python using unit tests.

## Usage

As you study the language, add little examples as tests.

This enables you to look up the syntax quickly later.

By keeping the tests running, you can be certain that the examples are correct.

Tests are especially useful if you tryout behaviour of the language that is
not immediately clear to you. Try out the behaviour and assert the results with
unit tests assertions. This way, you can even look up the output/results without
having to run the code again and frequently needing to check the output.

## Running the Tests

### Single Files

```bash
    python3 <file-name>
```

Unit tests are called because of this boilerplate in the files, if you add
a file be sure to include it:

```python
if __name__ == '__main__':
    unittest.main()

```

## Run all Files

run all tests with:

```python
    python3 -m unittest *.py
```

To ensure that all your examples are correct.

## Run in PyCharm

To run all tests in PyCharm, the run configuration 
needs to be modified to include all *.py files in 
test discovery by adding `-p *.py` as additional parameter.
See [Test Discovery](https://docs.python.org/3/library/unittest.html#unittest-test-discovery)

# Unit Tests in Python

https://docs.python.org/3/library/unittest.html

# Sources for Python

* [Python Documentation](https://docs.python.org/3/)
* [Sedgewick, Wayne, Dondero: Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/home/)

# Things to explore

## Control Structures
* Conditional Statement (if/else)
* Loops
* functions and methods

## Data Structures
* Lists, Set, Map, Queue, Stack, (Heap)

## Object Oriented Programming
* class definition
* instance creation
* method lookup

## What is the Type model?

* static or dynamic?
* strict or loose?

## How to interact with the language / Structure of a Program

* main method
* interpreter