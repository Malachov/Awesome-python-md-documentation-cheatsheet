# Awesome-python-md-documentation

This is python user documentation created in markdown so it can be visualized in IDE. How it can look is on this printscreen.

![Printscreen of documentation use](https://raw.githubusercontent.com/Malachov/Awesome-python-md-documentation-cheatsheet/master/printscreen.png)

Feel free to colab...

It's also in jupyter notebook ipynb version. Markdown is good for finding correct syntax and for efficiency, notebook is good, when you want to learn something a play with code. It's derived from original md with notedown, so modify markdown. To convert type in cmd opened in folder (or in some other shell):

To recreate jupyter notebook just open create_jupyter.cmd (in windows)

Or if you don't have windows, type this to terminal !!:

    # ! pip install notedown
    # ! notedown input.ipynb --to markdown --strip > output.md

Note 1: Some cells are commented, because can slow notebook, make errors or save files. If there is an !!! exclamation mark !!! after comment, it means, that it's code for your shell (e.g. cmd). If you remove comment, run cell from notebook, code in shell will be executed. Longer comments are assigned to variable so it's not printed to console. Just remove variable, uncomment and enjoy...

Note 2: Jupyter need some libraries for particular tasks. Install it when reach the error, or if you don't want to install them manually, use chapter 1 Requirements - bulk libraries install, and install all of them from [My requirements](https://github.com/Malachov/My-python-requirements)

Note 3: Content is not working in jupyter, so delete it. Use nbextensions and extension table of content. If you have no nbextensions, than use:

    # !  pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install 

    # I recommend Table Of contents, Variable inspector, ExecuteTime, Code Prettify and Autopep8. Just restart jupyter and choose from tab nbextensions.

# Content

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Awesome-python-md-documentation](#awesome-python-md-documentation)
- [Content](#content)
- [General](#general)
  - [Show installed libraries](#show-installed-libraries)
  - [Virtual env](#virtual-env)
  - [Requirements - bulk libraries install](#requirements-bulk-libraries-install)
- [Comments](#comments)
  - [Documentation - docstrings](#documentation-docstrings)
    - [reStructured text](#restructured-text)
    - [docBlockR](#docblockr)
  - [Multi line code](#multi-line-code)
    - [Show where python is installed](#show-where-python-is-installed)
- [Logical conditions](#logical-conditions)
  - [Not](#not)
  - [Greater than, lower than](#greater-than-lower-than)
  - [And, or](#and-or)
  - [None](#none)
- [Variables](#variables)
  - [Declaration of more variables at once](#declaration-of-more-variables-at-once)
    - [Swap variables values](#swap-variables-values)
    - [Bulk create variables](#bulk-create-variables)
    - [Check if variable exist](#check-if-variable-exist)
  - [Import variables from other modules](#import-variables-from-other-modules)
    - [Find name of variable, list or dictionary](#find-name-of-variable-list-or-dictionary)
- [DATA TYPES](#data-types)
    - [Type of variable as condition](#type-of-variable-as-condition)
    - [If exist](#if-exist)
  - [String](#string)
    - [Format](#format)
    - [Newest and fastest format- f'strings'](#newest-and-fastest-format-fstrings)
    - [String to code](#string-to-code)
    - [Join - concatenate](#join-concatenate)
- [List](#list)
- [Deque](#deque)
  - [Tuple](#tuple)
- [Dictionary](#dictionary)
- [Set](#set)
- [Dataframe](#dataframe)
- [Numpy Array](#numpy-array)
- [Iterator](#iterator)
- [LOOPZ](#loopz)
  - [IF](#if)
    - [If variable exist](#if-variable-exist)
    - [Ternary operator - If in argument](#ternary-operator-if-in-argument)
  - [FOR](#for)
    - [Return indexes and elements](#return-indexes-and-elements)
  - [Generate list of elements from u1 to u5](#generate-list-of-elements-from-u1-to-u5)
  - [Generate values with strings](#generate-values-with-strings)
    - [For in list comprehension](#for-in-list-comprehension)
    - [Generate list with for cycle and if](#generate-list-with-for-cycle-and-if)
    - [Generate list with more parameters](#generate-list-with-more-parameters)
    - [Nested lists](#nested-lists)
  - [WHILE](#while)
- [Functions](#functions)
    - [Jump out of function - return](#jump-out-of-function-return)
    - [Default parameter](#default-parameter)
    - [Unknown number of parameters - *args, **kwargs](#unknown-number-of-parameters-args-kwargs)
    - [Global variables](#global-variables)
- [Functions are objects](#functions-are-objects)
    - [Function in list generator](#function-in-list-generator)
  - [Functions map(), filter(), reduce()](#functions-map-filter-reduce)
    - [Reduce - Input sequention into function](#reduce-input-sequention-into-function)
- [Generators](#generators)
- [Dekorators](#dekorators)
- [Module](#module)
- [Classes](#classes)
    - [Create object](#create-object)
    - [Call class method](#call-class-method)
    - [Change atribute of class](#change-atribute-of-class)
    - [Call static method](#call-static-method)
    - [Magic methods](#magic-methods)
- [FILE I/O](#file-io)
    - [Import fuction from other file](#import-fuction-from-other-file)
    - [Find script's adress](#find-scripts-adress)
    - [Import variables from file in the same folder](#import-variables-from-file-in-the-same-folder)
    - [If file or dir exists](#if-file-or-dir-exists)
    - [Create module from folder](#create-module-from-folder)
    - [Show all files in folder](#show-all-files-in-folder)
    - [Filter for one type data](#filter-for-one-type-data)
    - [Load all files with certain suffix](#load-all-files-with-certain-suffix)
  - [Work with files](#work-with-files)
    - [Import txt](#import-txt)
  - [Pickling](#pickling)
- [Paths](#paths)
  - [Pathlib - new and correct way](#pathlib-new-and-correct-way)
- [Try -- Except](#try-except)
  - [Try for all errors and print it](#try-for-all-errors-and-print-it)
  - [Raise exception](#raise-exception)
  - [Assert - Require something or error](#assert-require-something-or-error)
- [Warnings](#warnings)
- [Regular expressions](#regular-expressions)
- [Built in functions](#built-in-functions)
    - [Print](#print)
    - [Range](#range)
    - [Reverse range](#reverse-range)
    - [\__name__ - If file is runned from inside or is imported](#__name__-if-file-is-runned-from-inside-or-is-imported)
- [Date and time](#date-and-time)
- [Plots, graphs](#plots-graphs)
  - [Plotly](#plotly)
  - [Matplotlib](#matplotlib)
  - [Table](#table)
  - [Symbolic functions](#symbolic-functions)
- [Libraries](#libraries)
  - [If pip cannot be installed by SSL errorr](#if-pip-cannot-be-installed-by-ssl-errorr)
- [Jupyter](#jupyter)
  - [Autoreload](#autoreload)
  - [Link](#link)
  - [Image](#image)
  - [Youtube](#youtube)
  - [Show all images from folder](#show-all-images-from-folder)
- [Requests - API - GET, POST](#requests-api-get-post)
- [Images, pictures](#images-pictures)
- [Mahematics, statistics, linear algebra](#mahematics-statistics-linear-algebra)
- [Machine learning](#machine-learning)
- [Signal processing and controll](#signal-processing-and-controll)
- [Miscellaneous](#miscellaneous)
  - [Measure time](#measure-time)
  - [Show bytcode](#show-bytcode)
- [Performance](#performance)
    - [Type hinting](#type-hinting)
  - [Numba](#numba)
  - [Dask](#dask)
    - [Dask formats](#dask-formats)
  - [Force to empty memory](#force-to-empty-memory)
  - [Max execution time python](#max-execution-time-python)
  - [Profiling](#profiling)
- [Whole sections](#whole-sections)
  - [Encoding JSON with Python](#encoding-json-with-python)
- [Pypi export / create own library](#pypi-export-create-own-library)
- [Github](#github)

<!-- /code_chunk_output -->


# General

## Show installed libraries

    # !  pip list

    # Show outdated libraries

    # !  pip list --outdated

## Virtual env

    # !  pip install virtualenv
    # !  virtualenv daniel  # Vytvoří novou virtuálku
    # !  C:\VSCODE\Diplomka\pokus\Scripts\activate.bat  # Activate virtual env

## Requirements - bulk libraries install

    # !  pip install -r /path/to/requirements.txt

    # Create requirements

    # !  pipreqs --encoding=utf8 C:\VSCODE\Diplomka

    # Deprecated

    # !  (pip freeze > requirements.txt)

# Comments

    # One line comment

    ## Multiline comment
    """ Víceřádkové komentáře používají tři uvozovky nebo apostrofy
    a jsou často využívány jako dokumentační komentáře k metodám
    """

## Documentation - docstrings
Posible modes - DocBlockR, ReST, Numpy, Google

### reStructured text

```markdown
restr = ''' # remove the variable - it's just for jupyter
Section Header
==============

Subsection Header
-----------------

- A bullet list item

- A sub item

1) An enumerated list item

.. image:: /path/to/image.jpg

A sentence with links to `Wikipedia`_

.. _Wikipedia: https://www.wikipedia.org/

+------------------------+------------+----------+
| Header row, column 1   | Header 2   | Header 3 |
+========================+============+==========+
| body row 1, column 1   | column 2   | column 3 |
+------------------------+------------+----------+
| body row 2             | Cells may span        |
+------------------------+-----------------------+

Literal - no linebreaks etc.

::

some literal text.


Python code in docstrings

.. code:: python

print("A literal block directive explicitly marked as python code")
'''
```

### docBlockR

```python
"""Function to find optimal parameters of function
======
Output:
------
    Optimized parameters {dict}

Arguments:
------
    model {func} -- Function to be optimized (eg: ridgeregression)
    kwargs {dict} -- Initial arguments (eg: {"alpha": 0.1, "n_steps_in": 10})
    kwargs_limits {dict} -- Bounds of arguments (eg: {"alpha": [0.1, 1], "n_steps_in":[2, 30]})
    data {list, array, dataframe col} -- Data on which function is optimized (eg: data1)
    fragments {int} -- Number of optimized intervals (default: 10)
    predicts {int} -- Number of predicted values (default: 7)
"""
```

## Multi line code

    poi = { "1": 3,
            "2": 4, 
            "6": 8 }

    # or use brackets or \\

    a = (   1 + 2
            + 3 + 4 )

    a = 1 + 2 \
        + 3 + 

    f = range(  1 + 2
            + '3' - '4')  # Function example

### Show where python is installed

    # ! where python

# Logical conditions
## Not

    not True # => False
    'a' is not 1
    'a' != 1

## Greater than, lower than
\>=

## And, or

    0 and 2 # => 0
    -5 or 0 # => -5
    0 == False # => True
    if 2 > 1 and 5 > 6:
        pass

    # Logical conditions can be combined

    1 < 2 < 3 # => True

## None

    # None is object (NULL, nil, ...)

    None  # => None

    # So don't use "==" for comparison. Rather use "is"

    None is None # => True

    # None, 0, and empty string/list/dictionary is False, everything else True

    bool(0) # => False
    bool("") # => False
    bool([]) # => False
    bool({}) # => False

# Variables

    y = int(2.8)

    x = 1
    x += 1 # Zkrácený zápis x = x + 1. Pozor, žádné x++ neexisuje

    # Int divided by int

    3 / 2  # = 1.5
    3 // 2  # = 1

## Declaration of more variables at once

    a = b = c = 1

    a,b,c = 1,2,"john"

### Swap variables values

    e = 2; d = 4
    e, d = d, e # d is now 5, e is now 4

### Bulk create variables

    name = ['mike', 'john', 'steve']  
    age = [20, 32, 19]

    for x,y in zip(name, age):
        globals()[x] = y  # mike = 20 ...

    uname = ['u{}'.format(n) for n in range(7)] # [u1, u2, u3...]

### Check if variable exist

    if 'myVar' in locals():
        pass

## Import variables from other modules
Creat config.py

There for example

    x = 1

In main then use

config.x = 2 ....

### Find name of variable, list or dictionary

    var = 3
    my_var_name = [k for k,v in globals().items() if v == var][0]

# DATA TYPES

    a = type(var)  # Return type

### Type hinting

    def sentence_has_animal(sentence: str) -> bool:
        return "animal" in sentence
    sentence_has_animal("Donald had a farm without animals")

### Type of variable as condition

    if isinstance(var, str):  # Check if it's string (or int etc...)
        pass

    # More types at once

    import numpy as np  
    y = np.array([1])
    isinstance(y, (np.ndarray, np.generic))  # pd.DataFrame For dataframe

    if a is list: # Zjistí, zda jde přímo o string
        pass

    # Also work if object is includes in class

### If exist

    if callable(a):
        pass

## String

    # Strings " or ' and can contain UTF8 symbols

    a = "This is string."
    a = 'This is also string.'

    # In python 3

    print('strings are now utf-8 \u03BCnico\u0394é!')  # strings are now utf-8 μnicoΔé!

    # Strings can use + but don't use

    a = "Hello " + "world!" # => "Hello world!"

    # Can be concatenated without '+'

    a = "Hello " "world!" # => "Hello world!"

    # String is list of symbols

    a = "This is list"[0] # => 'T'

### Format

    # Old

    a = '%s  %s' % ('one', 'two')

    # Newer

    a = '{} {}'.format('one', 'two')

    # Format can be used multiple times

    a = "{0} {1} stříkaček stříkalo přes {0} {1} střech".format("tři sta třicet tři", "stříbrných")

    # You can use named arguments

    a = "{jmeno} si dal {jidlo}".format(jmeno="Franta", jidlo="guláš") # => "Franta si dal guláš"

### Newest and fastest format- f'strings'

    name = 'Peter'
    f"Hello, {name}. You are {2 * 17}. Also functions {name.lower()}."

    # You can use raw strings (no escape characters, but still format)
    a = 15
    print(fr'Escape is here:\n but still {a}')  # Escape is here:\n but still 15

If you use """ no escape symbols will be used
Also can use dictionaries, but "" is necesarry
Dont use # in f strings

### String to code

    mycode = 'x = 1'
    exec(mycode)

    # or
    x = eval("2+2") # number ze stringu

### Join - concatenate

    words = ["this", 'is', 'a', 'list', 'of', "strings"]
    ' '.join(words)  #returns "This is a list of strings"

## List

    empty_list = []
    lst = [1, 2, 3, 4]
    lst.append(1)  # lst is now [1, 2, 3, 4, 1]
    lst.insert(1, 2)  # insert 2 on index 1
    lst.pop()  # Remove last value
    lst.remove(2)  # Remove first 2 in list
    del lst[1]  # Delete first element
    del lst[-2:]  # Range delete - from the last one
    b = [1,2]
    c = lst + b  # Serializes
    lst.extend(b)  # Serializes

    # If lst a = lst b and we change one of them, the other also change therefor

    lista = [1, 2, 3]
    listb = lista.copy()
    listb[2] = 5
    print(lista)  # [1, 2, 5]

    ### Access members

    lst = [1, 2, 3, 4]
    lst[0]  # => 1
    lst[-1]  # => 3

    ### Slices

    lst[1:3]  # => [2, 4]
    lst[2:]  # => [4, 3]
    lst[:3] # => [1, 2, 4]

    # Every second member

    lst[::2] # =>[1, 4]

    ### Minimum

    youngest = min(lst)

    ### Find maximum and it's index

    m = max(lst)
    [i for i, j in enumerate(a) if j == m] # pro a = [1,2,0]  # 1

    ### Sum

    suma = sum(lst)

    ### If member exist

    1 in lst # => True

    ### Length of list

    len(lst) # => 6

    ### Every value just once

    t =  [1,  2,  3,  1,  2,  5,  6,  7,  8]
    lst = list(set(t))  # [1,  2,  3,  5,  6,  7,  8]

    ### Reverse

    rev = lst[::-1] # => [3, 4, 2, 1]

    # Or

    rev = t.reverse()

    ### Iterate in reverse order

    for i in reversed(lst):
        pass

    ### Check if list is empty or not

    a = 6
    if a:
        pass

    if not a:
        pass

    ### Create list from 0 to 10

    l = range(10) #  [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]

    ### Create list - List comprehension

    [x*5 for x in range(5)] #[0, 5, 10, 15, 20]
    [x for x in range(5) if x%2 == 0] #[0, 2, 4]
    [a if a else  2  for a in  [0,1,0,3]]

    # List comprehension from more entities

    list_1 = [1, 2, 3]
    list_2 = [2, 3, 4]
    [(i, j) for i, j in zip(list_1, list_2)] # [(1, 'a'), (2, 'b'...]

    ### Zip lists

    zip(list_1, list_2) # {(a1, b1), (a2, b2)}

    ### Logical condition on lists

    j2 = [i for i in list_1 if i >=  5]

    ### One value more times

    listOfStr = ['Hi'] * 3 # ['Hi', 'Hi', 'Hi']

    ### Multiple list

    my_list =  [1,  2,  3,  4,  5]
    my_new_list =  [i *  5  for i in my_list]

    ### Find index

    my_list.index(3)

    ### Nested lists

    t = [[1,2], [3,4]]
    print(t[1][1])  # 4

    ### Every first member of nested lists

    L = [[[0,1,2],[3,4,5],[6,7,8]],  [[0,1,2],[3,4,5],[6,7,8]],  [[0,1,2],[3,4,5],[6,7,8]]]
    R = [[x[0]  for x in sl ]  for sl in L ]  # [[0, 3, 6], [0, 3, 6], [0, 3, 6]]

    # Or

    lst = [[1,2,3],[11,12,13],[21,22,23]]
    a = list(zip(*lst))[0]  # [1, 11, 21]

    ### Add first with first, second with second

    [a + b for a, b in zip(list_1, list_2)]

    ### List of functions

    def func1():return 1
    def func2():return 2
    def func3():return 3
    fl = [func1,func2,func3]
    [f() for f in fl] # [1, 2, 3]

    ### How many times members in list

    import collections
    print( collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))

## Deque

You can iterate from both sides

    import collections
    de = collections.deque([1, 2, 3])
    de.append(0)  # Add x to the right side of the deque.
    de.appendleft(6)  # Add x to the left side of the deque.
    de.count(2)  # Count the number of deque elements equal to x.
    lst = [1, 2, 3]
    de.extend(lst)  # Extend the right side of the deque by appending elem   ents from the iterable argument.
    de.pop()  # Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
    de.popleft()  # Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
    de.remove(2)  # Remove the first occurrence of value. If not found, raises a ValueError.
    de.reverse()  # Reverse the elements of the deque in-place and then return None.
    de.rotate(1)  # Rotate the deque n steps to the right. If n is negative, rotate to the left.
    de.clear()  # Remove all elements from the deque leaving it with length 0.


## Tuple

Tuple is like list but imutable  !!! [] i can change - () i cannot change !!!

    tuple = (1, 2, 3)
    tuple[0]  # => 1
    # tuple[0] = 3  # Raise TypeError

    a, = 5  # (5)
## Dictionary

    empty_dic = {}
    dic = {"jedna": 1, "dva": 2, "tři": 3}
    dic_variable = {key:value for (key,value) in dic.items()}

    ### Add value

    dic['čtyři'] = 4  # If key is already there it's updated

    ### Create dictionary from two lists

    name = ['mike', 'john', 'steve']  
    age = [20, 32, 19]
    dic=dict(zip(name, age))

    ### Miscelanious

    thisdict = {'b':1, 'c':2, 'd':3}
    del thisdict['b']  # delete list
    'e' in thisdict  # returns False
    thisdict.items()  # returns [('a', 1), ('c', 'eggs')]

    # All keys

    dic.keys()

    # You need list sometimes not iterables

    list(dic.keys())

    ### Last key in dictionary

    max(dic)

    ### For cycle for all keys

    for s in dic:
        print(s)

    ### Maximum value and its index

    stats = {'a':1000, 'b':3000, 'c': 100}
    maxname = max(stats, key=stats.get)
    maxvalue = stats[maxname]

    ### Values

    list(dic.values()) # => [3, 2, 1]
    "jedna" in dic # => True if value is in dictionary
    dic.get("čtyři") # => None - don't raise error if key not in dic
    dic.setdefault("pět", 5) # dic["pět"] default 5

    ### Find key from value

    list(stats.keys())[list(stats.values()).index(100)]

    ### For cycle for dictionaries

    for k in stats: # Iteruje přes všechny klíče
        print(k)

    for k, v in stats.items(): # Iteruje řes všechny klíče a hodnoty
        print(k,v)

    ### Join two dictionaries

    c = {**dic, **stats}

    ### Enumerate in dictionaries

    for i, (j, k) in enumerate(dic.items()):
        pass

    ### Dictionary as arguments into function

    def rep(*nonamed, **named):
        return nonamed, named

    t = (47,11)
    d = {'x':'extract','y':'yes'}
    rep(*t, **d) # It's the same as f(47, 11, x=extract, y=yes)

    ### Nested dictionaries - for examples name of functions and it's parameters

    def rep2(*inp, **inp2):
        return rep

    models = {"AR (Autoregression)": rep, "Linear neural unit": rep2}
    modelsparameters = {"AR (Autoregression)": {"predicts":  2}, "Linear neural unit": {"predicts": 4}}
    modelscomplet = zip(models.keys(), models.values(),  modelsparameters.values())
    modelsresults = []

    for i, j, k in modelscomplet:
        modelsresults.append({i: j(1, **k)})

    ### Nested dictionaries - Find minimum

    top = 1000000
    for key, value in modelsparameters.items():
        for inkey, invalue in value.items():
            if invalue < top:
                best_model_name = key
                best_data = inkey
                top = invalue

    ### Dictionary comprehension

    {x: x**2 for x in range(1, 5)} # => {1: 1, 2: 4, 3: 9, 4: 16}
    {pismeno for pismeno in "abeceda"} # => {"d", "a", "c", "e", "b"}

## Set

It is not oredered and every value is just once!

    empty_set = set()
    sett = {1, 1, 2, 2, 3, 4}  # {1, 2, 3, 4}
    sett.add(5)  # {1, 2, 3, 4, 5}
    jina_set = {3, 4, 5, 6}

    # Intersect of 2 sets

    sett & jina_set # => {3, 4, 5}

    # Union

    sett | jina_set # => {1, 2, 3, 4, 5, 6}

    # Exception

    {1, 2, 3, 4} - {2, 3, 5} # => {1, 4}

    # If member exist

    2 in sett # => True
    9 in sett # => False

## Dataframe

Panda library is necessary
If there is a parameter inplace=True, then changes are made on original, otherwise change is only made for new variable assign

    ### Import from csv

    impt = '''
    import pandas as pd
    data = pd.read_csv(
        "data/files/complex_data_example.tsv",
        sep='\t',  # Tab-separated value file.
        quotechar="'",  # single quote allowed as quote character
        dtype={"salary": int},  # Parse the salary column as an integer
        usecols=['name', 'birth_date'].  # Only columns
        parse_dates=['birth_date'],  # Intepret the birth_date column as a date
        skiprows=10,  # Skip the first 10 rows of the file
        na_values=['.', '??']  # Take any '.' or '??' values as NA
    )
    '''

    ### Save into CSV

    # df.to_csv('newcsv.csv') # bez názvů , header=False

    ### Create

    import pandas as pd
    # one column dataframe

    s2 = pd.Series([1,2,3,4])

    # dataframe

    s2 = pd.DataFrame([1,2,3,4])

    # from list

    data = [['tom', 10, 1], ['nick', 15, 2], ['juli', 14, 3]]
    df = pd.DataFrame(data, columns = ['name', 'age', 'index'])

    # from dictionary

    dict = {'a': 1, 'b': 2}
    newdatf = pd.DataFrame.from_dict(dict, orient='index')

    # from array

    array = np.array([[1, 2], [2, 3], [3, 4]])
    #df2 = pd.DataFrame(data=array[1:,1:], index=range(len(data)), columns=data[0,1:])

    ### Access column

    df['name']

    ### Subset of columns - Access members

    # With name

    df1 = df[['name','age']]

    # with index

    df2 = df.iloc[:,0:1]  #   # All rows, first and second column

    df3 = df.iloc[0]  # First row

    ### Column to new dataframe

    a = df.pop('index')

    ### Return name of column from index

    a = df.columns[0]  # Columns return name of column

    ### Find index from column name

    a = df.columns.get_loc("age")

    ### Logical conditions

    df_new = df.loc[df['name'] == 'juli']

    ### Concat 2 columns

    df['name_and_age'] = df['name'] + str(df['age'])

    ### Make index from colmn

    df.set_index('name', inplace=True)
    df.reset_index(level=None, drop=False, inplace=False)

    ### Convert into array

    df['age'].values
    b=df1.iloc[:,1:].values  # every column separately

    ### Convert into list

    lst = df['age'].values.tolist()

    ### Miscelaneous

    df.index  # RangeIndex(start=0, stop=x....)
    df.dtypes  # age  int ...

    ### Lenght of dataframe

    length = len(df.index)

    ### Date and time and datetime, range

    # Datetime from values

    year = 2020; month = 3; day = 14; hour = 4
    start = pd.Timestamp(year=year, month=month, day=day, hour=hour)

    # Range

    df['EventStart'] = pd.date_range(start=start, periods=length, freq='H')

    # Convert from datetime to time, the same to datetime

    df['EventStart_time'] = df['EventStart'].dt.time

    ### Set index

    df.set_index('EventStart', drop=True, inplace=True)
    df.index = pd.to_datetime(df.index)

    ### Resample datetime dataframe

    df_res = df.resample('M').sum() # Méně řádků na výstupu

    ### Copy of dataframe

    # !!! If you use variables., change in one is also changed in the others, so if you want independent dataframes, use copy() !!!

    df2 = df.copy()


    ### Join 2 dataframes

    #### Concat
    # possible parameters - axis, join, ignore_index, sort, keys, levels

    df = pd.DataFrame([['a', 1], ['b', 2], ['c', 3]], columns=['letter', 'number'])
        #         letter  number
        #    0      a       1
        #    1      b       2
        #    2      c       3

    df2 = pd.DataFrame([['c', 1], ['d', 2], ['e', 3]], columns=['letter', 'number2'])

        #        letter  number
        #    0      c       1
        #    1      d       2
        #    2      e       3

    # Add rows

    df_rows = pd.concat([df, df2])

        #        letter  number  number2
        #    0      a     1.0      NaN
        #    1      b     2.0      NaN
        #    2      c     3.0      NaN
        #    0      c     NaN      1.0
        #    1      d     NaN      2.0
        #    2      e     NaN      3.0

        # join='inner' means only columns that are in both dfs

    # Add columns

    df_columns = pd.concat([df, df2], axis=1)

        #        letter  number letter  number
        #    0      a       1      c       1
        #    1      b       2      d       2
        #    2      c       3      e       3

    # or you can use

    df4 = df.append(df2)
        #         letter  number  number2
        #    0      a     1.0      NaN
        #    1      b     2.0      NaN
        #    2      c     3.0      NaN
        #    0      c     NaN      1.0
        #    1      d     NaN      2.0
        #    2      e     NaN      3.0

    ### Merge
    # Add database parameters like left join, outer join

    result = pd.merge(df, df2, on='letter', how='left')

        #        letter  number  number2
        #    0      a       1      NaN
        #    1      b       2      NaN
        #    2      c       3      1.0

    ### Group by

    gpd = df4.groupby('letter').agg({'number': np.mean, 'number2': np.size})

        #        number  number2
        #  letter		
        #    a	   1.0	   1.0
        #    b	   2.0	   1.0
        #    c	   3.0	   2.0   # c only once, not twice
        #    d	   NaN	   1.0
        #    e	   NaN	   1.0

    #### Get all from one group

    gpd = df4.groupby('letter')
    c = gpd.get_group('c')

        #        letter  number  number2
        #    2      c     3.0      NaN
        #    0      c     NaN      1.0

    ### Mean, standard deviation

    mean = df['number'].mean()
    std = df['number'].std()

    ### Rolling (moving) average and standard deviation

    rolling_mean = df['number'].rolling(10).mean()
    rolling_std = df['number'].rolling(10).std()

    ### Remove outliers

    df_removed_outliers = df[ (df['number'] < 2 * std) ]

    ### Transpose - Rows into columns

    df = df.T

## Numpy Array

    ## Create

    ar = np.array([[1,2,3], [4, 5, 6]])
    a = ar[1, 2]  # 5 - Access array
    a = np.append(a, 3)  # Add element to the end
    a = np.insert(a,1,[11,12])  # Into a on index 1 insert [11,12], next parameter can be axis
    np.roll(a,2) # Posune array o 2 doprava
    wo = np.array([1,2,3]) # Shape (3,)
    wo = np.array([[1,2,3,4,5]]) # Shape (1,5)
    wo = np.array([[1],[2],[3],[4],[5]]) # Shape (5,1)
    shape = np.shape(a) # `(n,m) Number of rows, columns etc.
    ar.shape[0]  # How many rows`
 

    ## Convert

    a = np.array([1, 2, 3])
    my_list = ar.tolist()  # Convert on list
    one_dim_list = np.array(ar).reshape(-1).tolist()  # Convert to one-dimensional list
    a_scal = a[0].item()  # from np.int convert on int

    ### Convert to other dtype

    b = a.astype(int)  # convert on np.int


    ### Slicing

    a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

       #    [[1 2 3]
       #     [3 4 5]
       #     [4 5 6]] 

    # Only column - not retain shape

    b = a[:, 1]  # [2 4 5]

    # Columns with same shape

    b = a[:, 1:2]  #   [[2]
                   #    [4]
                   #    [5]]

    # Only rows

    b = a[1, :]

    ### Join matrixes

    np.vstack([a,a])

        #   [[1, 2, 3],
        #    [3, 4, 5],
        #    [4, 5, 6],
        #    [1, 2, 3],
        #    [3, 4, 5],
        #    [4, 5, 6]])

    np.hstack([a,a])

        #    [[1, 2, 3, 1, 2, 3],
        #     [3, 4, 5, 3, 4, 5],
        #     [4, 5, 6, 4, 5, 6]]

    # Create matrix from vectors

    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])
    c = np.stack((a, b))  # [[1, 2, 3],
                          #  [2, 3, 4]]

    # Concatenate

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    np.concatenate((a, b), axis=0)
                                            # array([[1, 2],
                                            #        [3, 4],
                                            #        [5, 6]])
    np.concatenate((a, b.T), axis=1)
                                            #  array([[1, 2, 5],
                                            #         [3, 4, 6]])
    np.concatenate((a, b), axis=None)
                                            # array([1, 2, 3, 4, 5, 6])

    # Append
    # Add column

    x = np.array([[10,20,30], [40,50,60]])
    y = np.array([[100], [200]])
    z = np.append(x, y, axis=1)

        #   [[ 10  20  30 100]
        #    [ 40  50  60 200]]

    ### Find minimum value

    min = np.amin(c, axis=1)

    ### Mean

    mean = np.mean(x)

    ### Standard deviation

    std = np.std(x)

    ### Find index of smallest value

    ind = np.unravel_index(np.argmin(a), shape=a.shape)

    ### Create zero or ones matrix of given shape

    zeros = np.zeros_like(a)

    # Ones

    ones = np.ones((3,3))

        #   [[1., 1., 1.],
        #    [1., 1., 1.],
        #    [1., 1., 1.]]

    ### Replace all values with logical condition

    a[a > .5] = .5

    ### Delete member

    a = np.delete(a, 1, axis=0) # There need to be variable before!  axis 0 are rows, 1 are columns

    ### Delete Nan values

    a = a[~np.isnan(a)]

    ### Delete all rows where are Nan

    ar = ar[~np.isnan(ar).any(axis=1)]

    ### Sums

    # Axis 0 is for sums on columns

    np.sum([[0, 1], [0, 5]], axis=0)  # array([0, 6])
    np.sum([[0, 1], [0, 5]], axis=1)  # array([1, 5])

    ### Dot product / multiplication

    # Asterisk means each with each not matrix multiplication

    # For vectors

    x = np.array([1,2,3])
    w = np.array([1,2,3])
    v = x*w # [1, 4, 9]
    v = np.dot(x, w) # 14

    x = np.array([1,2,3])
    w = np.array([[1],[2],[3]])
    v = x*w

        #   [[1 2 3]
        #    [2 4 6]
        #    [3 6 9]]

    v = np.dot(x, w) # 14

    # For matrixes

    x = np.array([[1,2,3], [1,2,3], [1,2,3]])
    w = np.array([[1,2,3], [1,2,3], [1,2,3]])
    v = x*w

        #   [[1 4 9]
        #    [1 4 9]
        #    [1 4 9]]

    v = np.dot(x, w)

        #   [[6 12 18]
        #    [6 12 18]
        #    [6 12 18]]

    ### Shape

    z = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
    z.shape  # (3, 4)

    ### Number of members - count

    count = z.size

    ### Cumulative sum

    y = np.cumsum(x)

    ### Remove non unique values

    unique = np.unique(array, axis=0)

    ### Reshape

    # reshape -1 add members automatically
    z_res = z.reshape(-1) # array([ 1,  2,  3,  4,  5,  6])
    z_res2 = z.reshape(-1,1)

        # array([[ 1],
        #        [ 2],
        #        [ 3],
        #        [ 4],
        #        [ 5],
        #        [ 6]])

    z_res3 = z.reshape(-1, 2)
        # array([[ 1,  2],
        #        [ 3,  4],
        #        [ 5,  6],
        #        [ 7,  8],
        #        [ 9, 10],
        #        [11, 12]])

    a = np.array([[1,2,3], [4,5,6]])

    a_res = np.reshape(a, 6, order='F')
        # array([1, 4, 2, 5, 3, 6])

    ### Transpose

    z = np.array([[[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]], 
                 
                  [[2, 2, 2, 2],
                  [2, 2, 2, 2],
                  [2, 2, 2, 2]],
                  
                 [[3, 3, 3, 3],
                  [3, 3, 3, 3],
                  [3, 3, 3, 3]]
                 ])

    z_tran = z.transpose(1, 0, 2)  # From (10, 100, 1000) create (10, 1000, 100)

        #    array([[[1, 1, 1, 1],
        #            [2, 2, 2, 2],
        #            [3, 3, 3, 3]],
        #
        #           [[1, 1, 1, 1],
        #            [2, 2, 2, 2],
        #            [3, 3, 3, 3]],
        #
        #           [[1, 1, 1, 1],
        #            [2, 2, 2, 2],
        #            [3, 3, 3, 3]]])

    z_tran = z.transpose(1, 2, 0)

        #   array([[[1, 2, 3],
        #           [1, 2, 3],
        #           [1, 2, 3],
        #           [1, 2, 3]],
        #
        #          [[1, 2, 3],
        #           [1, 2, 3],
        #           [1, 2, 3],
        #           [1, 2, 3]],
        #
        #          [[1, 2, 3],
        #           [1, 2, 3],
        #           [1, 2, 3],
        #           [1, 2, 3]]])

    ### Generate points, arange, linspace, random and generate sin

    q = np.random.randn(3, 3)
    t = np.linspace(0,20,1000)  # Generate numbers with the same interval (beginning, end, number)
    t = np.arange(1, 3, 1)  # Start, stop, step - [1, 2]
    t = np.arange(3)  # 0, 1, 2
    y = np.sin(t)

    ### Find index (one) with max / min value

    np.argmax(x)  # or argmin. Also can use parameter axis

    ### Eigen values

    eig = np.linalg.eig(q)

    eigenvalues, V = np.linalg.eig(A)  # eigenvalues[0] is the first eigenvalue
    # V is a 2D array (matrix) that contains the four eigenvectors as columns, hence, V[:,i] is the eigenvector corresponding to the eigenvalue eigenvalues[i]

    plt.scatter(eigenvalues.real, eigenvalues.imag)  # Plot it

    ### Inverse matrix

    q_inv = np.linalg.inv(q)

    ### Determinant

    det = np.linalg.det(q)

    ### Fill with Nan values

    z = np.zeros((2, 3))
    z.fill(np.nan)

    ### Check if Nan values

    if not np.isnan(np.any(z)):
       pass

    ### Zip for arrays

    def azip(*args):
        iters = [iter(arg) for arg in args]
        for i in itertools.count():
            yield tuple([it.next() for it in iters])

## HDF5

    ### Create

    import h5py
    import numpy as np

    arr = np.random.randn(1000)

    with h5py.File('random.hdf5', 'w') as f:
        dset = f.create_dataset("default", data=arr)

    ### Read

    with h5py.File('random.hdf5', 'r') as f:
        data = f['default']
        print(min(data))

    ### Specify Data Types to Optimize Space

    with h5py.File('several_datasets.hdf5', 'w') as f:
        dset_int_1 = f.create_dataset('integers', (10, ), dtype='i1')
        dset_int_8 = f.create_dataset('integers8', (10, ), dtype='i8')
        dset_complex = f.create_dataset('complex', (10, ), dtype='c16')
        dset_int_1[0] = 1200

# Iterator

    iterable = [1, 2, 3]
    iterator = iter(iterable)

Next value

    next(iterator) # => "one"

# LOOPZ
## IF
### If variable exist

    try:
        __IPYTHON__
        my_exec = "%matplotlib notebook"
        exec(my_exec)
    except NameError:
        print('No Jupyter')

    # Or

    variable = [10, 20, 30]
    for i in variable:
        if variable:
            print("variable exist")
        if i > 10:
            print("Something")
            pass  # Do nothing
        elif i < 10:
            print("Variable is smaller than 10")
            continue # Jump to other operation
        else:
            print("Variable is 10 or not a number")
            break # Jump out of the cycle

### Ternary operator - If in argument

    variable = 3
    state = "nice" if variable else "not nice"

## FOR

    for zvire in ["pes", "kočka", "myš"]:
        print("zvire")
    for i in range(4):
        print(i)
    for i in range(4, 8):
        print(i)
    colors  =  ["red",  "green",  "blue",  "purple"]
    for  i  in  range(len(colors)):
        print(colors[i])

### Return indexes and elements

    ints = [8, 23, 45, 12, 78]
    for idx, val in enumerate(ints):
        print(idx, val)

## Generate list of elements from u1 to u5

    uname = ['u{}'.format(n) for n in range(1, 6)]

## Generate values with strings

    for k in range(5):
        exec(f'cat_{k} = k*2')

### For in list comprehension

    [x*5 for x in range(5)] #[0, 5, 10, 15, 20]

### Generate list with for cycle and if

    [x for x in range(5) if x%2 == 0]  #[0, 2, 4]
    [a if a else  2  for a in  [0,1,0,3]]

### Generate list with more parameters

    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    [a + b for a, b in zip(list1, list2)]

### Nested lists

    a = [[1,2,3],[2,3,4],[5,6,7]]
    print(a[1][1])   

## WHILE

    x = 0
    while x < 4:
        print(x)
        x += 1

# Functions

    def secist(x, y):  # Create new function with def
        return x + y  # Return values with return
    secist(5, 6)  # Call the function with parameters, return 11
    secist(y=6, x=5)  # Named arguments
    def return_arguments(*argumenty):  # Variable number of arguments
        return argumenty
    return_arguments(1, 2, 3)  # => (1, 2, 3)
    def return_named_arguments(**pojmenovane_argumenty):  # Varaiable number of named arguments
        return pojmenovane_argumenty
    return_named_arguments(kdo="se bojí", nesmi="do lesa")  # {"kdo": "se bojí", "nesmi": "do lesa"}
    def return_all(*args, **kwargs):  # You can use combination
        print(args, kwargs)  # Return all parameters

### Jump out of function - return

    def print_var():
        a = 8
        if a > 5:
            return
        print_var(2)

### Default parameter

    def funkce(y, lags=50): #If we use lags in call, it will be overwritten
        return 1

### Unknown number of parameters - *args, **kwargs

    def print_all(*args, **kwargs):
        print(args, kwargs)

    print_all(1, 2, a=3, b=4) # Use: (1, 2) {"a": 3, "b": 4}
    tuple = (1, 2, 3, 4)
    dic = {"a": 3, "b": 4}
    print_all(tuple)  # Is like print_all((1, 2, 3, 4)). One parameter - tuple
    print_all(*tuple)  # Is like print_all(1, 2, 3, 4)
    print_all(**dic)  # Is like print_all(a=3, b=4)
    print_all(*tuple, **dic)  # Is like print_all(1, 2, 3, 4, a=3, b=4)

### Global variables

    x = 5
    def setx(cislo):  # Local variable override global
        x = cislo  # => 43
        print(x)  # => 43


    def setglobalx(cislo):
        global x
        print(x) # => 5
        x = cislo # Nastaví globální proměnnou x na 6
        print(x) # => 6

# Functions are objects

    def adder(pricitane_cislo):
        def scitacka(x):
            return x + pricitane_cislo
        return scitacka
    add_10 = adder(10)
    add_10(3)  # => 13

### Function in list generator

    [add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
    [x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

## Functions map(), filter(), reduce()

From the functional programming

Map call funtion (first parameter) on all objects (second parameter)

    map(add_10, [1, 2, 3])

Filter create list (First paratemer), where function is true (second parameter)

    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)  # [-5, -4, -3, -2, -1]

### Reduce - Input sequention into function

    from functools import reduce
    def do_sum(x1, x2): return x1 + x2
    reduce(do_sum, [1, 2, 3, 4]) # 10

# Generators

Generators are functions, that instead return have yield

    def multiplier_2(sequention):
        for i in sequention:
            yield 2 * i

Generator generate values one after one, when it\s needed. Instead of been generated all at once
Example of generator is range(10000)

# Dekorators

Dekorators are functions, that wrap other functions, by that
it can change it's behaviour.

    def nekolikrat(puvodni_funkce):
        def opakovaci_funkce(*args, **kwargs):
            for i in range(3):
                puvodni_funkce(*args, **kwargs)
        return opakovaci_funkce

    @nekolikrat
    def pozdrav(jmeno):
        print("Měj se {}!".format(jmeno))

    pozdrav("Pepo")  # Return 3x: Měj se Pepo!

# Module

Module in python is file with .py on the end.
You can creat your own and import it.

    from math import sqrt

    help(sqrt)  # Help with module

    dir(sqrt)  #  Show objects in module

# Classes

    class Clovek(object):  # Class Human is child (it inherits from) class object

        druh = "H. sapiens"  # Class variable - it's shared with all objects

        def __init__(self, jmeno):
            self.jmeno = jmeno  # Add parameter to object

        def rekni(self, hlaska):
            return "{jmeno}: {hlaska}".format(jmeno=self.jmeno, hlaska=hlaska)

        @classmethod  # First parameter is class and can be changed in subclasses
        def vrat_druh(cls):
            return cls.druh

        @staticmethod  # Do not depend on object - like a normal function and is immutable
        def odkaslej_si():
            return "*ehm*"

    class DecoratorExample:

        def __init__(self):
            self.name = 'Decorator_Example'

        def example_function(self):
            print('I\'m an instance method!')

    de = DecoratorExample()
    de.example_function()


Example of class method

    class Date(object):

        def __init__(self, day=0, month=0, year=0):
            self.day = day
            self.month = month
            self.year = year

        @classmethod
        def from_string(cls, date_as_string):
            day, month, year = map(int, date_as_string.split('-'))
            date1 = cls(day, month, year)
            return date1

        @staticmethod
        def is_date_valid(date_as_string):
            day, month, year = map(int, date_as_string.split('-'))
            return day <= 31 and month <= 12 and year <= 3999

    date2 = Date.from_string('11-09-2012')
    is_date = Date.is_date_valid('11-09-2012')

### Create object

    d = Clovek(jmeno="David")
    a = Clovek("Adéla")
    print(d.rekni("ahoj"))  # "David: ahoj"
    print(a.rekni("nazdar"))  # "Adéla: nazdar"

### Call class method

    d.vrat_druh() # => "H. sapiens"

### Change atribute of class

    d.vrat_druh() # => "H. neanderthalensis"
    a.vrat_druh() # => "H. neanderthalensis"

### Call static method

    Clovek.odkaslej_si() # => "*ehm*"

### Magic methods

Example __call__ method (Allow input of object to function)

The \__call__ method can be used to turn the instances of the class into callables. Functions are callable objects. A callable object is an object which can be used and behaves like a function but might not be a function. By using the \__call__ method it is possible to define classes in a way that the instances will be callable objects. The \__call__ method is called, if the instance is called "like a function", i.e. using brackets. The following example defines a class with which we can create abitrary polynomial functions:

    class Polynomial:

        def __init__(self, *coefficients):

            self.coefficients = coefficients[::-1]

        def __call__(self, x):

            res = 0

            for index, coeff in enumerate(self.coefficients):

                res += coeff * x** index

                return res

    p1 = Polynomial(42)
    p2 = Polynomial(0.75, 2)
    p3 = Polynomial(1, -0.5, 0.75, 2)

    for i in range(1, 10):
        print(i, p1(i), p2(i), p3(i))

Magic methods (For example for change of + behaviour)
What happens when we create an object in python class ?

    '''
    List of magic methods:
    Binary Operators

    Operator           Method\
    +                       object.__add__(self, other)\
    -                        object.__sub__(self, other)\
    *                        object.__mul__(self, other)\
    //                       object.__floordiv__(self, other)\
    /                        object.__div__(self, other)\
    %                      object.__mod__(self, other)\
    **                      object.__pow__(self, other[, modulo])\
    <<                     object.__lshift__(self, other)\
    >>                     object.__rshift__(self, other)\
    &                       object.__and__(self, other)\
    ^                       object.__xor__(self, other)\
    |                        object.__or__(self, other)

    Assignment Operators:

    Operator          Method\
    +=                     object.__iadd__(self, other)\
    -=                      object.__isub__(self, other)\
    *=                      object.__imul__(self, other)\
    /=                      object.__idiv__(self, other)\
    //=                     object.__ifloordiv__(self, other)\
    %=                    object.__imod__(self, other)\
    **=                     object.__ipow__(self, other[, modulo])\
    <<=                   object.__ilshift__(self, other)\
    >>=                   object.__irshift__(self, other)\
    &=                     object.__iand__(self, other)\
    ^=                      object.__ixor__(self, other)\
    |=                      object.__ior__(self, other)

    Unary Operators:

    Operator          Method\
    -                       object.__neg__(self)\
    +                      object.__pos__(self)\
    abs()                object.__abs__(self)\
    ~                      object.__invert__(self)\
    complex()        object.__complex__(self)\
    int()                  object.__int__(self)\
    long()               object.__long__(self)\
    float()               object.__float__(self)\
    oct()                object.__oct__(self)\
    hex()               object.__hex__(self)

    Comparison Operators

    Operator Method\
    <                      object.__lt__(self, other)\
    <=                    object.__le__(self, other)\
    ==                    object.__eq__(self, other)\
    !=                     object.__ne__(self, other)\
    >=                    object.__ge__(self, other)\
    >                      object.__gt__(self, other)
    '''

    # Let's take an example to override the functionality "+" '[__add__]' operator

    class  Vector(object):
        def __init__(self,  *args):
            """ Create a vector, example: v = Vector(1,2) """
            if len(args)  ==  0:
                self.values =  (0,0)
            else:
                self.values = args
        def __add__(self, other):
            """ Returns the vector addition of self and other """
            added = tuple(a + b for a, b in zip(self.values, other.values)  )
            return  Vector(*added)

    # Now use the "+" operator with two vectors

    v1 =  Vector(1,  2)
    v2 =  Vector(10,  13)
    v3 = v1 + v2
    v3.values  # (11,  15)

    # When statement "v3 = v1 + v2 " executes "__add__" is called and it returns a new Vector object.

## __Repr__

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

If Pizza() return __repr__

# FILE I/O
### Import fuction from other file

    from math import sqrt  # First name of file, than function

### Find script's adress

    import os
    # os.path.dirname(__file__)  # Not working in jupyter !

### Import variables from file in the same folder

    # import file  # Then call file.value
    # from file import * # Now call just variable

### If file or dir exists

    from pathlib import Path
    my_file = Path("/path/to/file")
    if my_file.is_file():  # File exists
        pass
    if my_file.is_dir():  # Directory exists
        pass
    if my_file.exists():   # File or dir exists
        pass

### Create module from folder

Add file `__init.py__`
Inside do all imports from .autoregLNU import autoregLNU
Use relative imports with dots

### Show all files in folder

    # all_files = os.listdir("test/")

### Filter for one type data

    # txt_files = filter(lambda x: x[-4:]  ==  '.txt', all_files)

### Load all files with certain suffix

    import glob
    imgs=glob.glob("*.png")  # Všechny obrázky ze složky

    # Wildcard

    for name in glob.glob('dir/file?.txt'):
        print (name)

    for name in glob.glob('dir/*[0-9].*'):
        print (name)

    ### Import txt ###

    from numpy import loadtxt
    # x=loadtxt('realna_data_klapky.txt')

## Work with files

    '''
    Don't wanna save anything to jupyter

    f = open("test.txt", "w+") # open file in current directory

    'r'  Open a file for reading. (default)
    'w'  Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    'x'  Open a file for exclusive creation. If the file already exists, the operation fails.
    'a'  Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
    't'  Open in text mode. (default)
    'b'  Open in binary mode.
    '+'  Open a file for updating (reading and writing)

    f = open("C:/Python33/README.txt") # specifying full path
    f.close()

    with open("test.txt",'w')  as f:
        pass
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

    !!!Use because this will autamatically close the file finally

    f = open("test.txt",'r',encoding =  'utf-8')
    f.read(4) # read the first 4 data - 'This'
    f.read(4) # read the next 4 data - ' is '
    f.read() # read in the rest till end of file - 'my first file\nThis file\ncontains three lines\n'
    f.read() # further reading returns empty sting
    '''

## Manipulate with files

    '''
    ### Copy file ###

    import shutil, os
    s.chdir('C:\\')
    shutil.copy('C:\\spam.txt', 'C:\\delicious')

    ### Copy folder with all files ###
    shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

    ### Move files ###
    shutil.move('C:\\bacon.txt', 'C:\\eggs')

    ### Remove - move to trash bin ###
    import send2trash
    send2trash.send2trash('bacon.txt')

    ### Remove file ###
    os.unlink(path)

    ### Remove folder with all content ###
    shutil.rmtree(path)

    ### File tree - walk ###
    import os

    for folderName, subfolders, filenames in os.walk('C:\\delicious'):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)
    '''

## Pickling

Save file in binary format

    import pickle
    d = {"a": 1, "b": 2}
    # with open(r"someobject.pickle", "wb") as output_file: cPickle.dump(d, output_file)

Load files

    # with open(r"someobject.pickle", "rb") as input_file: e = cPickle.load(input_file)

Result is e = {"a": 1, "b": 2}**

# Paths
## Pathlib - new and correct way

    import pathlib
    path = pathlib.Path.cwd()

    data_folder = pathlib.Path("folder")
    file_to_open = data_folder / "raw_data.txt"

    ### Pathlib as string

    path.as_posix()

    ### Find all adress

    path = pathlib.Path('test.md')
    path.resolve() # ('/home/gahjelle/realpython/test.md')
    path.resolve().parent == pathlib.Path.cwd() # False

    ### Work with file

    filename = pathlib.Path("source_data/text_files/raw_data.txt")

    print(filename.name) # prints "raw_data.txt"
    print(filename.suffix) # prints "txt"
    print(filename.stem) # prints "raw_data"
    if not filename.exists():
        print("Oops, file doesn't exist!")
    else:
        print("Yay, the file exists!")

    ### Relative path

    '''
    !! Next rows just historical - Do not do it that way !!

    # ../data/test_file.csv # ..znamená parent složka

    from os import path
    import os

    file_path = path.relpath("data/data.txt")

    ### Absolute path

    # os.path.abspath(\__file__)  # Not working in jupyter

    ### Add path to files and modules

    import sys
    sys.path.insert(0, '/path/to/application/app/folder')
    sys.path  # Print folders available by system

    ### Working direktory and how to change it

    import os
    cwd = os.getcwd()
    # os.chdir(r"C:\Users\...")

    # new_cwd = os.getcwd() + r"\diplomka"
    # os.chdir(new_cwd)

    ### Full adress
    #Use normal slash!

    import os
    data_folder = "folder/nextfolder/"
    file_to_open = data_folder + "data.txt"

    # For example if jupyter do not see some files

    script_dir0 = os.path.abspath('') # C:\VScode

    # Next

    # script_path = os.path.abspath(\__file__)  # i.e. /path/to/dir/foobar.py  - notworking with jupyter
    script_path = 'C://prog'
    script_dir = os.path.split(script_path)[0]  #i.e. /path/to/dir/
    rel_path =  "2091/data.txt"
    abs_file_path = os.path.join(script_dir, rel_path)  # Result is relative '/path/to/dir/2091/data.txt'
    filename = os.path.join(script_path,  '../same.txt')  # We can use name of file
    # script_dir = os.path.dirname(\__file__)  # We can use adress of file... but not in jupyter

    # You can also do

    # script_dir = os.path.dirname(\__file__)
    rel_path = "test_ data/realna_data_klapky.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    '''

# Try -- Except

    try:
        print(znam)
    except:
        print('except')
    else:
        print('else')
    finally:
        print('final')

    try:
        print(neznam)
    except:
        print('except')
    else:
        print('else')
    finally:
        print('final')

##  Try for all errors and print it
    try:
        linux_interaction()

    except Exception as error:
        print(error)

## Raise exception

    # raise Exception('x should not exceed 5. The value of x was: {}')

## Assert - Require something or error

    x = 5
    assert (x > 4), 'What happened'

# Warnings

    import warnings
    warnings.warn("Warning...........Message")

    # Warnings with word 'HessianInversionWarning' will be caused as errors

    warnings.filterwarnings('error', message=r".*HessianInversionWarning*") 

    # Errory of category depracation will be show everytime

    warnings.filterwarnings('always', category=DeprecationWarning)  
    warnings.filterwarnings('ignore')  # Errory budou vždy ignorovány

    # "default" will print the first occurrence of matching warnings for each location
    # (module + line number) where the warning is issued

    # Other possibilities

    # "once"    |    "error"    |    "ignore"    |    "always"    |    "module"

 print the first occurrence of matching warnings for each module where the warning is issued (regardless of line number)


# Regular expressions

    regs = '''
    import re

    [] 	A set of characters 	"[a-m]" 	
    \ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
    . 	Any character (except newline character) 	"he..o" 	
    ^ 	Starts with 	"^hello" 	
    $ 	Ends with 	"world$" 	
    * 	Zero or more occurrences 	"aix*" 	
    + 	One or more occurrences 	"aix+" 	
    {} 	Exactly the specified number of occurrences 	"al{2}" 	
    | 	Either or 	"falls|stays"

    \A 	Returns a match if the specified characters are at the beginning of the string 	"\AThe" 	
    \b 	Returns a match where the specified characters are at the beginning or at the end of a word 	r"\bain"
    r"ain\b" 	

    \B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word 	r"\Bain"
    r"ain\B" 	

    \d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d" 	
    \D 	Returns a match where the string DOES NOT contain digits 	"\D" 	
    \s 	Returns a match where the string contains a white space character 	"\s" 	
    \S 	Returns a match where the string DOES NOT contain a white space character 	"\S" 	
    \w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w" 	
    \W 	Returns a match where the string DOES NOT contain any word characters 	"\W" 	
    \Z 	Returns a match if the specified characters are at the end of the string 	"Spain\Z"

    [arn] 	Returns a match where one of the specified characters (a, r, or n) are present 	
    [a-n] 	Returns a match for any lower case character, alphabetically between a and n 	
    [^arn] 	Returns a match for any character EXCEPT a, r, and n 	
    [0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
    [0-9] 	Returns a match for any digit between 0 and 9 	
    [0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
    [a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
    [+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

    '''

# Built in functions
### Print
    a = 'hi'
    print('as', a, 'fegg') # Use comma, you can join strings and variables

### Range

    x=range(3+1) # x = 0, 1, 2, 3

### Reverse range

    for i in reversed(range(5)):
        print(i) # 4, 3, 2, 1

### \__name__ - If file is runned from inside or is imported

    if __name__ == "__main__":
        pass

# Date and time

    import datetime as dt
    import time
    now = dt.datetime.now() #datum i čas
    time.sleep(1) # počká 1 vteřinu

# Plots, graphs

## Plotly

    pltl = '''
    import plotly as py

    fig = dict( data=data, layout=layout )
    py.offline.plot( fig, filename='d3-cloropleth-map' )

    # or

    init_notebook_mode(connected=True)
    cf.go_offline()

    data_ft_date.iplot(xTitle='Dates',yTitle='Returns',title='Returns')

    ### Plotly timeseries

    py.plot([{
        'x': data_for_predicts_csv_trimmed.index,
        'y': data_for_predicts_csv_trimmed[col],
        'name': col
    }  for col in data_for_predicts_csv_trimmed.columns])

    ### From matplotlib to plotly

    plot_mpl(fig)

    ### Save picture

    import plotly.io as pio
    static_image_bytes = pio.to_image(fig, format='png')

## Matplotlib

    mtpltlb = '''
    ### Simple plot

    import matplotlib.pyplot as plt
    plt.plot(data)

    ### Load txt and plot it

    from numpy import loadtxt # For one column txt
    x = loadtxt('realna_data_klapky.txt')
    figure(figsize=(20,5))
    plot(x,'-o',label="x");xlabel('i');ylabel('x [sec]');grid();title("realna_data_klapky.txt")
    legend();show()
    plt.savefig('fig1.png', dpi =  300) # uloží graf

    ### Jupyter plot one after one

    # Use not show()
    %matplotlib notebook
    import matplotlib.pyplot as plt
    import numpy as np

    x = [1, 2, 3, 4, 5, 6]

    fig, axes = plt.subplots()
    axes.plot(range(10))
    #figure one


    fig, axes = plt.subplots()
    axes.plot(range(10))
    #figure two


    fig, ((a,b),(c,d)) = plt.subplots(2,2)
    a.plot(x, np.sin(x))
    b.plot(x, np.cos(x))
    c.plot(x, np.tan(x))
    d.plot(x, np.tanh(x))

    ### Histogram

    figure(figsize=(20,5))
    nbins=int(round(1+3.3*log(N))) # Sturge's rule, but depend on data
    xlabel("x");ylabel("number_of_bins"),title("number_of_bins  - values x in intervals");grid()
    a=hist(x,bins=nbins) # vraci dve pole a histogram, tj a[0]=number_of_bins, a[1]=intervaly
    print "number_of_bins=",a[0]
    print "intervaly =",a[1]

    ### Curves and points

    x=arange(-600,100) #
    mu=m1;sigma=sqrt(s2);print "mu=",mu,"sigma=",sigma
    f=1/(sigma*sqrt(2*pi))*exp(-(((x-mu)/sigma)**2)/2)
    figure(figsize=(20,5))
    plot(x,f,'g',label="f(x) spojita");grid()
    plot(x_i,f_odhad,'o',label="f(x) odhad z mereni pro nbin="+str(nbins)+" intervalu")
    legend()

    ### Two graphs

    N=1000 # velikost výběru
    x=random.uniform(-10,10,N)
    x=random.randn(N)*1000-300
    x=random.logistic(3, 10, N)
    x=random.standard_t(3, N)
    x=random.poisson(1, N)*.01+1000
    nbins=int(round(1+3.3*log(N)))
    figure(figsize=(20,5))
    subplot(121);plot(x,'-o');grid();xlabel('index vzorku dat');ylabel("x")
    subplot(122)

    # First number is how much rows and second how much columns
    # Third number is which graph is it - first, second etc.

    a = hist(x,nbins,normed=True) ;# pro vizualni posouzeni
    grid(); ylabel("$\\approx f(x)$"); xlabel("x")
    plt.tight_layout() # Pokud část jednoho překrývá druhý
    plt.subplots_adjust(top=0.88)# po tight_layoutu je potřeba název umístit výš
    subplots_adjust(wspace=.3) # Větší rozestupy mezi grafy

    ### More plots with one legend

    plt.figure(figsize=(12,7))
    plt.subplot(3, 1, 1)
    plt.plot(t, yy, label='Predikce'); plt.xlabel('t')
    plt.plot(t, data, label='Skutečnost'); plt.xlabel('t')
    plt.legend(loc="upper right")
    plt.ylabel("u4 predikované")

    ### More plots with for cycle

    for i in range(1,7):
    plt.subplot(3, 2, i)
    plt.plot(oknomean[i]);plt.grid(); plt.xlabel('t')
    plt.ylabel("u{}".format(i))
    plt.suptitle("Klouzavý průměr okna", fontsize=20)
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.show()

    ### Scatterplot

    import numpy as np
    import matplotlib.pyplot as plt
    N = 60
    g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
    g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
    g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))
    data = (g1, g2, g3)
    colors = ("red", "green", "blue")
    groups = ("coffee", "tea", "water")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
    for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    plt.title('Matplot scatter plot')
    plt.legend(loc=2)
    plt.show()

    ### Text plot

    import matplotlib.pyplot as plt
    fig = [plt.figure](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "View documentation for matplotlib.pyplot.figure")(figsize=(5, 1.5))

    text = fig.text(0.5, 0.5, 'Hello path effects world!\nThis is the normal '
        'path effect.\nPretty dull, huh?',
        ha='center', va='center', size=20)

    [plt.show](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "View documentation for matplotlib.pyplot.show")()

    ### Log axis

    plt.loglog(x, y)  # Both axis are log

    '''

## Table

    from prettytable import PrettyTable
    models_table = PrettyTable()
    models_table = PrettyTable().field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    models_table = PrettyTable().add_row(["Adelaide", 1295, 1158259, 600.5])
    print (models_table)

## Symbolic functions

    '''
    import sympy as smp
    from sympy.plotting import plot as Plot
    from IPython.display import display
    z=smp.Symbol("z")
    fz=1/smp.sqrt(2*smp.pi)*smp.exp(-(z**2/2))
    display("f(z)=",fz)
    Plot(fz)
    display("F_{x\_median}=\int_{-\infty}^{x_{median}="+str(mu)+"}=",smp.integrate(fz,(z,-oo,0)))
    display(" z_{modus}= 0 \Leftrightarrow \dfrac{d f(z)}{ dz} =0=",smp.diff(fz,z))
    '''

# Libraries
## If pip cannot be installed by SSL errorr

    # !  pip install ipykernel --upgrade pip --trusted-host pypi.org

# Jupyter

    # !  jupyter kernelspec list # Ukáže seznam kernelů
    # !  jupyter kernelspec uninstall nazev # Odinstaluje kernel

## If jupyter and run from normal python

try:
    __IPYTHON__

    from IPython.terminal.embed import InteractiveShellEmbed
    ipshell = InteractiveShellEmbed()
    ipshell.dummy_mode = True
    ipshell.magic("%load_ext autoreload")
    ipshell.magic("%autoreload")

except NameError:
    print('No Jupyter')

## Run ipython in normal python

    from IPython.terminal.embed import InteractiveShellEmbed

    ipshell = InteractiveShellEmbed()
    ipshell.dummy_mode = True
    ipshell.magic("%timeit abs(-42)");

## Autoreload

Reload all modules imported with %aimport every time before executing the Python code typed, so it is not necessary to reload kernel everytime some other file changed or new library wa installed

    %load_ext autoreload
    %autoreload  # Reload all modules (except those excluded by %aimport) automatically now.
    %autoreload 0  # Disable automatic reloading.
    %autoreload 1  # Reload all modules imported with %aimport every time before executing the Python code typed.
    %autoreload 2  # Reload all modles (except those excluded by %aimport) every time before executing the Python code typed.
    %aimport  # List modules which are to be automatically imported or not to be imported.
    %aimport foo  # Import module ‘foo’ and mark it to be autoreloaded for %autoreload 1
    %aimport -foo  # Mark module ‘foo’ to not be autoreloaded.


## Link

‚''
[Link name](<https://www.youtube.com/>)
‚''

## Image

‚''
<img src="img/Gini.png" width=400>
‚''

## Youtube

    # from IPython.display import YouTubeVideo
    # YouTubeVideo('7VeUPuFGJHk')

## Show all images from folder

    '''
    import os
    from IPython.display import display, Image
    names = [f for f in os.listdir('../images/ml_demonstrations/') if f.endswith('.png')]
    for name in names[:5]:
        display(Image('../images/ml_demonstrations/' + name, width=100))
    '''

# Requests - API - GET, POST

    '''
    import getpass
    import requests
    username = input('Username: ')
    Username: hroncok
    password = getpass.getpass()
    Password: 
    r = requests.get('https://api.github.com/user', auth=(username, password))
    r.status_code
    r.headers['content-type']  # 'application/json; charset=utf8'
    r.encoding  # 'utf-8'
    r.text  # '{"login":"hroncok"...'
    r.json()  # {'avatar_url': 'https://avatars.githubusercontent.com/u/2401856?v=3', ...}
    '''

# Images, pictures

    '''
    from PIL import Image
    from resizeimage import resizeimage

    ## Show image

    ax1.imshow(img)

    ## Resize

    img = Image.open(im)
    img = resizeimage.resize_contain(img, [100,100]) # nebo
    img = img.resize((1250,890),Image.ANTIALIAS) # antialias

    ## Save

    img.save(soubor[0]+'_resized_'+soubor, img.format)
    img.close()

    ## Convert to black and white

    img = img.convert('L') #Převede na černobílý

    ## Convert image to matrix

    img=np.array(img)
    '''

# Mathematics, statistics, linear algebra
!! Matrix and liear algebra operations discussed in Numpy aray section !!

    ### Display nice math

    from IPython.display import display, Math, Latex
    display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))

    ### Square root ###

    y = 9**(1/2)  # 3

    ### Round ###

    A = round(5.76543, 2)

    ### Natural log - e ###

    from math import e
    a = e  # 2.71

    # Or

    import numpy as np
    a = np.exp(1)

    ### Modulo ###

    a = 7 % 3 # => 1

    ### Power (x on y) ###

    a = 2**4 # => 16

    ### Describe - Statistical values of list ###

    import pandas as pd
    
    df = pd.Series([1, 4, 6, 88])
    df.describe()
    
        #    count     4.000000
        #    mean     24.750000
        #    std      42.216703
        #    min       1.000000
        #    25%       3.250000
        #    50%       5.000000
        #    75%      26.500000
        #    max      88.000000
        #    dtype: float64

    ### Statistical values of array

    from scipy import stats
    a = np.array([1, 3, 5, 77])
    stats = stats.describe(a)

    ## Random
    ### Random numbers in normal distribution

    import numpy as np
    ran = np.random.randn(3)

    q = np.random.randn(3, 4)

        #    [[ 1.33262386 -0.88922967 -0.07056098 0.27340112]
        #     [ 1.00664965 -0.68443807 0.43801295 -0.35874714]
        #     [ -0.19289416 -0.42746963 -1.80435223 0.02751727]]

    ### Random number everytime the same

    np.random.seed(5)

    w = np.random.randn(3)  # [ 0.44122749 -0.33087015  2.43077119]
    w = np.random.randn(3)  # [ 0.44122749 -0.33087015  2.43077119]

    ### Random numbers in normal distribution matrix shape

    s = np.random.normal(2, 6, 1000)  # Mu, Sigma,

    ## Points generation

    t = np.linspace(0,20,1000)  # Generate numbers with the same interval (beginning, end, number)

    t = np.arange(1, 3, 1)  # 1, 2
    t = np.arange(3)  # 0, 1, 2

    ### Mean

    x = np.array([[10,20,30], [40,50,60]])
    np.mean(x)

    ### Standard deviation

    std = np.std(x)

    # Or

    from statistics import stdev
    sample = [1, 2, 3, 4, 5]
    std = stdev(sample)

    ### Bins

    bins = 10
    binss = np.histogram(x, bins)  # binss[0] hodnoty binss[1]
        # original = x = np.array([[10,20,30], [40,50,60]])
        # binss[0] = counts - [1 0 1 0 1 0 1 0 1 1]
        # binss[1] = values [10. 15. 20. 25. 30. 35. 40. 45. 50. 55. 60.]

    ### Cumulative sum

    y = np.cumsum(x)

    ### Derivation

    sample = [1, 2, 8, 4, 5]
    z = np.diff(y)
        # [ 1  6 -4  1]

    ### Latex dislay

    # from IPython.display import display, Math, Latex
    # display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))


    ########################################
    ####### Symbolic python - sympy #######
    #######################################
    '''
    import sympy as sp

    #  Nice display
    init_printing()

    # Or
    # Or use sp.pprint()

    ### Display Latex

    sp.latex(x**2)

    ### Create symbols

    s = sp.Symbol("s")
    x, y, z = sp.symbols('x,y,z')
    d, e, f = sp.symbols('d:f')
    inf = sp.oo

    ### Create one member (fraction) from more members

    ans = sp.together(1/x + 1/y + 1/z)
        #   x*y + x*z + y*z
        #   ---------------
        #        x*y*z

    # Imaginary numbers
    x = 1 + 1*I

    ### Expand

    ans = ((x+y)**2).expand()
        #    x**2 + 2*x*y + y**2

    ### Substitute

    expr = sp.cos(x)
    expr.subs(x, 0) # 1

    ### Compute string

    str_expr = "x**2 + 3*x - 1/2"
    expr = sp.sympify(str_expr)

    ### Simplify equation

    simplified = sp.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
        #    𝑥−1

    ### Evaluate expression

    expr = sp.sqrt(8)
    expr.evalf() # 2.82842712474619

    x_dif = sp.diff(sp.sin(2*x), x)

    ### Use numerical evaluation

    import numpy
    a = numpy.arange(10)
    expr = sp.sin(x)
    f = sp.lambdify(x, expr, "numpy")
    res = f(a)
        # [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
        #  -0.2794155   0.6569866   0.98935825  0.41211849]
    
        ### Combine with numpy

    y_vec = numpy.array([N(((x + pi)**2).subs(x, xx)) for xx in x_vec])  # But lambdify is faster

    ### Solve equation

    solve(x**2 - 1, x)  # [-1, 1]
    solve([x + y - 1, x - y - 1], [x,y])  # {x:1,y:0}

    # Exponential
    from mpmath import e
    y = sp.exp(x)

    # Matrices

    m11, m12, m21, m22 = symbols("m11, m12, m21, m22")
    b1, b2 = symbols("b1, b2")

    A = Matrix([[m11, m12],[m21, m22]])
        #   [ m11    m21
        #     m12    m22 ]
    
    b = Matrix([[b1], [b2]])
        #   [ b1
        #     b2 ]

    # Matrix operations

    sqr_mat = A**2
    mat_mul = A*b
    det = A.det()
    inv = A.inv()

    ### Fast fourier transform

    from numpy.fft import fft, fftfreq, ifft
    import numpy as np

    t = np.arange(0, 10, 0.1)
    y = np.sin(t)

    ffty = fft(y)

    real_ffty = ffty.real
    imag_ffty = ffty.imag

    freqs = fftfreq(N, dt)  # Frequentions assigned to values - 0, 0.1, 0.2...

    ### Sympy plotting

    from sympy.plotting import plot
    p1 = plot(sp.exp(t))
    '''

    ######################################
    ####### Differential equations #######
    ######################################

    import sympy as sp
    f = sp.Function('f')
    x = sp.Symbol('x')
    eq = f(x).diff(x, x) + f(x)
    res = sp.dsolve(eq, f(x))

    ###########################
    ####### Integration #######
    ###########################

    unb_int = '''
    ### Unbounded integral

    import sympy as sp
    from sympy import exp as e
    x = sp.Symbol("x")
    f = e(-x)
    disp("f=",f)
    intf = sp.integrate(f)
    disp("\int " + dfrac(f)+"dx=",intf) # po \int musim byt mezera

    ### Bounded integral

    intf=sp.integrate(f,(x,0,1))
    disp("\int_0^1" + dfrac(f)+" dx=",intf.evalf())
    '''

    ###########################
    ####### Correlation #######
    ###########################

    ### Correlation matrix - values

    import pandas as pd
    df = pd.DataFrame([[1, 2, 3], [4, 5, 9], [7, 8, 78]], columns=['one', 'two', 'three'])
    x_cor = df.corr()

        #               one      two    three
        #    one    1.00000  1.00000  0.89977
        #    two    1.00000  1.00000  0.89977
        #    three  0.89977  0.89977  1.00000

    ### Correlation matrix - plot

    # a = pd.plotting.scatter_matrix(df, figsize=(16,12), alpha=0.3)

    ### Correlation (Pearson corr. matrix)

    import matplotlib.pyplot as plt
    scoreTable = df.corr(method='pearson')
    df.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)

    ### Correlation coefficent

    ar = np.array([1, 2, 4, 5, 9]) 
    ar2 = np.array([7, 8, 78, 34, 2])
    a = np.corrcoef(ar, ar2)

        #    [[ 1.        -0.0475504]
        #     [-0.0475504  1.       ]]

    ##########################
    ####### Statistics #######
    ##########################

    ### Create combinations

    from scipy.special import binom
    a = binom(5,2)

    ### Test of normal distribution

    from statsmodels.stats.stattools import jarque_bera
    residuals = [1, 3, 5, 2, 4]
    score, pvalue, _, _ = jarque_bera(residuals)
    if pvalue < 0.10:
        print ('We have reason to suspect the residuals are not normally distributed.')
    else:
        print ('The residuals seem normally distributed.')

# Machine learning

    #################################################
    ####### Standardization and normalization #######
    #################################################

    ### Standardization: mean = 0 and std = 1

    from sklearn import preprocessing
    import numpy as np
    X_train = np.array([[ 1., -1.,  2.],
                        [ 2.,  0.,  0.],
                        [ 0.,  1., -1.]])
 
    scaler = preprocessing.StandardScaler()

    fitted_scaler = scaler.fit(X_train)
    scaled = fitted_scaler.transform(X_train)

        #    [[ 0.  ..., -1.22...,  1.33...],
        #     [ 1.22...,  0.  ..., -0.26...],
        #     [-1.22...,  1.22..., -1.06...]]

    # inverse transformation
    back = fitted_scaler.inverse_transform(scaled)

    ### Normalization (-1,1)
    # Just replace one row from standard scaler
    scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))

    ### The same way you can use preprocessing.RobustScaler, that is not as much influenced by outliers !!

# Signal processing and controll

    '''
    ## Signal

    import scipy.signal as sig
    y = sg.sawtooth(2*pi/100*t,0.5)  # Create sawtooth signal

    ### Chirp signal
    t = np.linspace(0, 10, 5001)
    w = sig.chirp(t, f0=6, f1=1, t1=10, method='linear') # (t, f0, t1, f1)  # Changing frequency

    ## Hanning window

    w = hanning(N)

    ## Tuckey window

    w = sig.tukey(N)

    ## Fourier transform

    dt = 1./1024
    t = np.arange(0,2,dt)
    N = len(t)
    y = sig.sawtooth(2*np.pi/T1*t,0.5)

    freq = np.fft.fftfreq(N,dt)  # Return frequencies
    ffty = np.fft.fft(y)
    rffty = np.real(ffty)  # Real part
    iffty = np.imag(ffty)  # Imaginary part

    ## Inverse Fourier transform

    y_back = np.fft.ifft(ffty)

    ## Power spectral density

    PSD = (abs(ffty)**2)/N

    ## Hilbert transform - Envelope, phase, frequency

    analytic_signal = hilbert(signal)
    amplitude_envelope = np.abs(analytic_signal)
    instantaneous_phase = np.unwrap(np.angle(analytic_signal))
    instantaneous_frequency = (np.diff(instantaneous_phase) / (2.0*np.pi) * fs)

    ### Filtering

    import scipy.signal as sig
    from scipy.signal import butter,filtfilt

    t = np.linspace(0, 10, 501)
    w = sig.chirp(t, f0=6, f1=0.1, t1=10, method='linear') # (t, f0, t1, f1) 

    Wn = 0.1  # zkuste pozorovat efekt nasobici konstanty na cinnost filtru
    filter_order = 2
    b, a = butter(filter_order, Wn, 'high', analog=False)  #Matlab-style filter design

    x_dem = sig.lfilter(b, a, w) 

    # Or
    x_dem = filtfilt(b, a, w)  # Apply  filtr (forward and backward)

    # You can use scipy or you can use controll

    ####################
    ##### Controll #####
    ####################

    ## State-space representation

    A = [[0. , 1.], [-1., -1.]]
    B = [[0.], [1.]]
    C = [1. , 0.]
    D = 0.

    import control as ct

    sys = ct.ss(A , B, C, D)


    ## Transfer function

    g = ct.tf(1 ,[1 ,1, 1])  # Or ct.tf(sys)

        #        1
        #   -----------
        #   s^2 + s + 1

    sys = ct.ss(g)  # Convert back from transfer to state space

    ## Convert from continuous to discrete

    g = ct.tf(1, [1, 1, 1])
    gd = ct.c2d (g, 0.01)

        #   4.983e-05 z + 4.967e-05
        #   -----------------------
        #     z^2 - 1.99 z + 0.99

    ## Interconnect systems

    ### Parallel


        #      2 s + 3
        #    -------------
        #    s^2 + 3 s + 2


    #################
    ##### Scipy #####
    #################

    # You have to use float here. Not working for int...

    from scipy import signal

    sys = signal.StateSpace(A, B, C, D)

    ### Step response

    t1, y1 = signal.step(sys)

    ################
    ### Simulate ###
    ################
    
    t = np.linspace(0, 100, 101)
    u = np.zeros(len(t))
    u[10:50] = 1.0;  u[50:] = 2.0

    t3, y3, x3 = signal.lsim(sys, u, t)

    import numpy as np
    from scipy.integrate import odeint
    import matplotlib.pyplot as plt

    # function that returns dy/dt
    def model(y,t):
        k = 0.3
        dydt = -k * y
        return dydt

    # initial condition
    y0 = 5

    # time points
    t = np.linspace(0,20)

    # solve ODE
    y = odeint(model,y0,t)

    # plot results
    plt.plot(t,y)
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()

    ### Simulate with time dependent input

    def fdxdt(x,t,u,Omega,eta,b0,b1):    # x=[x1 x2 ... xn] 
          dx1dt=-Omega0**2*x[1]-b0*u
          dx2dt=-2*eta*Omega0*x[1]-b1*u+x[0]
          return(dx1dt,dx2dt)

        dt=.21  #[sec]
        t=arange(0,50,dt) ; N=len(t)  # delka dat
        Npul=int(N/2)   #konverze na integer

        u=sin(2*pi/10*t) ; u[Npul+1:]=sign(u[Npul+1:])

        u=u*1

        figure(figsize=(12,4));grid()
        plot(t,u,'-*',label="u(t)");xlabel("t");legend();title("$Vstup \ u(t) \ se \ meni  \ se \
                \ vzorkovaci \ periodou \ \Delta t $="+str(dt) +" [sec] \n")
        show()

        from scipy.integrate import odeint

        Omega0=10  ;  eta=.1  ;   b0=Omega0**2  ;  b1=0

        #===============================

        y=zeros(N)
        x10=0 ; x20=0  # poc. podm

        x0=[x10,x20]

        for i in range(0,N-1):
            tt=[t[i],t[i+1]]  # [t1 t2]
            x=odeint(fdxdt,x0,t,(u[i],Omega0,eta,b0,b1)) #returns x=[ [x1(t1) x2(t1)] [x1(t2) x2(t2)]]
        #    x=odeint(fdxdt,x0,tt,args=(u[i],)) # <-- pokud je jen jeden extra argument, musi se tak    
            y[i+1]=-x[1,1]
            x0=x[1,:]  # jako nove poc. podm pro dalsi integraci
            
        figure(figsize=(14,6))
        grid()
        plot(t,y,"-*",label="y(t)...simulace scipy.integrate.odeint"),xlabel("t [sec]"),legend()
        show()
        '''

# Miscellaneous

## Measure time

    '''
    # Most simple and maybe the best

    import time
    start = time.time()
    a = 6
    end = time.time()
    print(end - start)

    # Or

    import timeit
    import functools

    def func(*args):
        a = 1
        return a

    t = timeit.Timer('''
    import numpy as np
    a = 12
    ''', 'gc.enable()')
    print(t.timeit(3))  # 3 - measure three times

    # Or you can use
    t = timeit.timeit(func)

    # Measure time of function with inputs
    t = timeit.Timer(functools.partial(func, (1, 2)))
    print (t.timeit(20))
    '''

## Show bytcode

    import dis
    dis.dis("dict()")

        #              0 LOAD_NAME                0 (dict)
        #              2 CALL_FUNCTION            0
        #              4 RETURN_VALUE

# Performance

## Numba

    import numba as nb

    @nb.njit()
    def func():
        return 1

    # Or

    @nb.jit(nopython=True)  # Or use  parallel=True, nogil=True, cache=True
    def func():
        return 1

    # Or

    @nb.vectorize
    def function(a, b):
        return 1

    # Or direct data formats

    import numba as nb
    @nb.jit(nb.int32(nb.int32, nb.int32))
    def function(a, b):
        return a + b

    ### Get numba dtype from other

    numba.typeof(np.empty(3))
    array(float64, 1d, C)

    ### Evaluate chunk sizes

        i = numba.cuda.grid(1)
        while i < x.size:
            # Do something
            i += numba.cuda.grid(1)

    ### Cuda in Numba ###

    import math
    import numpy as np
    from numba import cuda
    import matplotlib.pyplot as plt
    %matplotlib inline

    len(cuda.gpus)  # 1

    cuda.gpus[0].name  # b'GeForce GTX 980M'

    @cuda.jit
    def mandelbrot_numba(m, iterations):
        # Matrix index.
        i, j = cuda.grid(2)
        size = m.shape[0]
        # Skip threads outside the matrix.
        if i >= size or j >= size:
            return
        # Run the simulation.
        c = (-2 + 3. / size * j +
            1j * (1.5 - 3. / size * i))
        z = 0
        for n in range(iterations):
            if abs(z) <= 10:
                z = z * z + c
                m[i, j] = n
            else:
                break

        size = 400
        iterations = 100

        m = np.zeros((size, size))

        # 16x16 threads per block.
        bs = 16
        # Number of blocks in the grid.
        bpg = math.ceil(size / bs)
        # We prepare the GPU function.
        f = mandelbrot_numba[(bpg, bpg), (bs, bs)]

        f(m, iterations)

    # Or

    from numba import cuda
    @cuda.jit(device=True)
    def function(a, b):
        return a + b

## Dask

    dsk = '''
    import dask

    @dask.delayed
    def inc(x):
        return x + 1

    @dask.delayed
    def double(x):
        return x + 2

    @dask.delayed
    def add(x, y):
        return x + y

    data = [1, 2, 3, 4, 5]

    output = []
    for x in data:
        a = inc(x)
        b = double(x)
        c = add(a, b)
        output.append(c)

    total = dask.delayed(sum)(output)
    # maybe add    total.compute()
    '''

### Dask formats

    dsk_frmts = '''
    import pandas as pd
    import dask.array as da
    import dask.dataframe as dd
    x = da.random.random((20, 20), chunks=(10, 10))
    res = x.dot(x.T).sum()
    res.compute()

    # Dataframes implement the Pandas API
    
    df = pd.DataFrame([[1, 2, 3], [1, 5, 3], [5, 6, 7]], columns = ['one', 'two', 'three'])
    dfdsk = dd.from_pandas(df, npartitions=1)

    # Or dd.read_csv('adress')

    from dask_ml.linear_model import LogisticRegression  # Dask-ML implements the Scikit-Learn API
    lr = LogisticRegression()
    lr.fit(dfdsk, dfdsk)

    ## Show task structure

    .visualize()
    '''
## Force to empty memory

    import gc
    gc.collect()

## Max execution time python

    import time, sys
    
    def watchdog(timeout, code, *args, **kwargs):
        "Time-limited execution."
        def tracer(frame, event, arg, start=time.time()):
            "Helper."
            now = time.time()
            if now > start + timeout:
                raise WatchdogTimeoutError(start, now)
            return tracer if event == "call" else None
    
        old_tracer = sys.gettrace()
        try:
            sys.settrace(tracer)
            code(*args, **kwargs)
        finally:
            sys.settrace(old_tracer)
    
    def func(a):
        return 1 + a
    
    watchdog(5, func, 0.1) # First element is time limit - Last argument 0.1 are *args and **kwargs

    # Or
    mx_ex = '''
    from contextlib import contextmanager
    import threading
    import _thread

    class TimeoutException(Exception):
        def __init__(self, msg=''):
            self.msg = msg

    @contextmanager
    def time_limit(seconds, msg=''):
        timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            raise TimeoutException("Timed out for operation {}".format(msg))
        finally:
            # if the acti   on ends in specified time, timer is canceled
            timer.cancel()

    import time
    with time_limit(5, 'slee'):
        time.sleep(10)
    '''

## Profiling
    # !  pip install snakeviz
    # !  python -m cProfile -o program.prof my_program.py
    # !  snakeviz program.prof

# Whole sections

## Encoding JSON with Python

    import json

    data =  {
                'a':  0,
                'b':  9.6,
                'c':  "Hello World",
                'd':  {
                        'a':  4
                }
    }

    json_data = json.dumps(data)
    # Notice how the keys are not sorted by default, you would have to add the sort_keys=True

# Pypi export / create own library

Put on github, add licence, create release. In computer create setup.py. Delete pypi_exp variable. It's here just not to be printed to console.

    pypi_exp = '''

    # This is content of setup.py
    from setuptools import setup, find_packages
    import io
    import os
    import sys

    here = os.path.abspath(os.path.dirname(__file__))

    def read(*filenames, **kwargs):
        encoding = kwargs.get('encoding', 'utf-8')
        sep = kwargs.get('sep', '\n')
        buf = []
        for filename in filenames:
            with io.open(filename, encoding=encoding) as f:
                buf.append(f.read())
        return sep.join(buf)

    long_description = read('README.md')

    setup(
        name='predictit',
        version='0.2',
        url='https://github.com/Malachov/predictit',
        download_url='https://github.com/Malachov/predictit/archive/0.11.tar.gz',
        license='mit',
        author='Daniel Malachov',
        install_requires=[
                'SQLAlchemy',
                'pandas',
                'pyodbc',
                'Keras',
                'sklearn_extensions',
                'tensorflow',
                'prettytable',
                'matplotlib',
                'plotly',
                'cufflinks',
                'numpy',
                'scipy',
                'seaborn',
                'statsmodels',
                'scikit_learn'
        ],
        author_email='malachovd@seznam.cz',
        description='Library/framework for making predictions.',
        long_description=' Automatically choose best of 20 models (ARIMA, regressions, LSTM...). Preprocess data and chose optimal parameters of predictions.',
        packages=find_packages(),
        include_package_data=True,
        platforms='any',
        classifiers = [
            'Programming Language :: Python',
            'Development Status :: 2 - Pre-Alpha',
            'Natural Language :: English',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            ],
        extras_require={
        }
    )

    # Next create setup.cfg

    # Inside of setup.cfg

    [metadata]
    description-file = README.md

    [bdist_wheel]  # Dal pro wheels knihovnu
    universal = 1

    [metadata]
    license_file = LICENSE

    # Load folder in cmd and

    python setup.py sdist

    # Or if you use wheel - better

    python setup.py sdist bdist_wheel

    # Finally

    twine upload dist/*
    '''

# Github

    ### Gitignore

    gtgnr = '''

    Create file called .gitignore
    Filed defined here will be ignored with version controll
    But it must be first ignored, than created, otherwise it will not work

    # Comments must beginn on new line !!!

    # Ignore one file
    readme.txt

    # Ignore folder
    output/

    # ignore all *java files
    *.java

    '''
