# Python

## Overview

Python software is distributed as a series of *libraries* that are called within your code to perform certain tasks.
There are many different collections, or *distributions* of Python software.
Generally you install a specific distribution of Python and then add additional libraries as you need them. There are also several different *versions* of Python.
Support for Python 2 ended in 2020, so you should use Python>=3!
It is import to note that some libraries only work with specific versions of Python.

```{note}
If you open a terminal on your computer, chances are if you type 'python' you will find it is already installed! But it is best-practice to create separate environments or 'virtual environments' to not interfere with existing installations. You can use {term}`conda` for this.
```

## Installing a specific Python version

We will be using Python 3 during the week.
You can create environments with different versions of Python using the following commands:

``` bash
conda create --name py39 python=3.9
```

To use Python 3.9:

``` bash
conda activate py39
```

To check if you have the correct version activated

```bash
which python
python --version
```

If you are already familiar with Python 2.7, you can take a look at the syntax differences [here](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html), but the main point to remember is to put the print statements in parentheses:
```python
print('Hello World!')
```