# Description

Minimal Python unit-test setup.

## Test framework

You can either choose the built-in
[unittest](https://docs.python.org/3/library/unittest.html) 
or the more flexible [PyTest](https://docs.pytest.org).

If using PyTest, you need to install it first (see below at "Dependencies").

You will find unit-test files written for each framework. Choose the one that
works for you; feel free to delete the other one.

## Dependencies

Install dependencies with:

```
pip install -r requirements.txt
```

## Running tests

It is strongly recommended that you use a Python IDE like 
([PyCharm](https://www.jetbrains.com/pycharm/) 
to run the tests.

If you are using PyTest, you can also run them from the
command-line with:

```
pytest
```

Alternatively, for unittest it is:

```
python -m unittest
```