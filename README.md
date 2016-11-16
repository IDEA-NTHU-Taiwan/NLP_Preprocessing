#NLP Preprocessing

This package include several preprocessing method for text analysis

## Structure of the repository

**/module** contains the preprocessing class
**/tests** contains the test for each class

## Run the tests

```
./Makefile
```

## Add a dependency

All the dependencies are in *requirements.txt*

## Add a preprocessing class

1. Write the test in *test/test_<CLASS_NAME>.py*

2. Create a file *module/FILE_NAME*

3. Add the the class in *module/__init__.py*

```python
from .FILE_NAME import CLASS_NAME
```
