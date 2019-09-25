# Awesome-python-md-documentation
This is python user documentation created in markdown so it can be visualized in IDE. How it can look is on this printscreen.

![Printscreen of documentation use](https://raw.githubusercontent.com/Malachov/Awesome-python-md-documentation-cheatsheet/master/printscreen.png)

Feel free to colab...

- [Awesome-python-md-documentation](#awesome-python-md-documentation)
- [General](#general)
  - [Show installed libraries](#show-installed-libraries)
  - [Virtual env](#virtual-env)
  - [Requirements - bulk libraries install](#requirements---bulk-libraries-install)
  - [One line comment](#one-line-comment)
  - [Multiline comment](#multiline-comment)
  - [Documentation - docstrings](#documentation---docstrings)
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
  - [Import variables from other modules](#import-variables-from-other-modules)
    - [Find name of variable, list or dictionary](#find-name-of-variable-list-or-dictionary)
- [DATA TYPES](#data-types)
    - [Type of variable as condition](#type-of-variable-as-condition)
    - [If exist](#if-exist)
  - [String](#string)
    - [Format](#format)
    - [String to code](#string-to-code)
    - [Join - concatenate](#join---concatenate)
- [List](#list)
    - [Check if list is empty or not](#check-if-list-is-empty-or-not)
    - [Create list from 0 to 10](#create-list-from-0-to-10)
    - [Create list - List comprehension](#create-list---list-comprehension)
    - [Function in list generator](#function-in-list-generator)
    - [One value more times](#one-value-more-times)
    - [Multiple list](#multiple-list)
    - [Find index](#find-index)
    - [Access members](#access-members)
      - [Slices](#slices)
    - [Reverse](#reverse)
    - [Iterate in reverse order](#iterate-in-reverse-order)
    - [Nested lists](#nested-lists)
    - [Every first member of nested lists](#every-first-member-of-nested-lists)
    - [Remove member](#remove-member)
    - [Minimum](#minimum)
    - [Find maximum and it's index](#find-maximum-and-its-index)
    - [Sum](#sum)
    - [If member exist](#if-member-exist)
    - [Length of list](#length-of-list)
    - [Every value just once](#every-value-just-once)
    - [Intersection and inclusive](#intersection-and-inclusive)
    - [Add first with first, second with second](#add-first-with-first-second-with-second)
    - [List of functions](#list-of-functions)
    - [How many times members in list](#how-many-times-members-in-list)
  - [Deque](#deque)
  - [Tuple](#tuple)
- [Dictionary](#dictionary)
    - [Add value](#add-value)
    - [Create dictionary from two lists](#create-dictionary-from-two-lists)
    - [Miscelanious](#miscelanious)
    - [Last key in dictionary](#last-key-in-dictionary)
    - [For cycle for all keys](#for-cycle-for-all-keys)
    - [Maximum value and its index](#maximum-value-and-its-index)
    - [Values](#values)
    - [Find key from value](#find-key-from-value)
    - [For cycle for dictionaries](#for-cycle-for-dictionaries)
  - [Join two dictionaries](#join-two-dictionaries)
    - [Enumerate in dictionaries](#enumerate-in-dictionaries)
    - [Dictionary as arguments into function](#dictionary-as-arguments-into-function)
    - [Nested dictionaries - for examples name of functions and it's parameters](#nested-dictionaries---for-examples-name-of-functions-and-its-parameters)
    - [Nested dictionaries - Find minimum](#nested-dictionaries---find-minimum)
    - [Dictionary comprehension](#dictionary-comprehension)
- [Set](#set)
- [Iterator](#iterator)
- [Dataframe](#dataframe)
    - [Import from csv](#import-from-csv)
    - [Access column](#access-column)
    - [Subset of columns](#subset-of-columns)
    - [Column to new dataframe](#column-to-new-dataframe)
    - [Subset of rows and columns](#subset-of-rows-and-columns)
    - [Concat 2 columns](#concat-2-columns)
    - [Find index from column name](#find-index-from-column-name)
    - [Zvolit index ze sloupce](#zvolit-index-ze-sloupce)
    - [Create](#create)
    - [Convert into array](#convert-into-array)
    - [Convert into list](#convert-into-list)
    - [Date and time and datetime, range](#date-and-time-and-datetime-range)
    - [Join 2 dataframes - Add rows](#join-2-dataframes---add-rows)
    - [Join 2 dataframes - Add columns](#join-2-dataframes---add-columns)
    - [Transpose - Rows into columns](#transpose---rows-into-columns)
    - [Save into CSV](#save-into-csv)
    - [Group by](#group-by)
    - [Moving average](#moving-average)
    - [Remove outliers](#remove-outliers)
    - [Resample dataframe](#resample-dataframe)
- [Numpy Array](#numpy-array)
    - [Convert](#convert)
    - [Slicing](#slicing)
      - [Only column - not retain shape](#only-column---not-retain-shape)
      - [Columns with same shape](#columns-with-same-shape)
    - [Only rows](#only-rows)
    - [Matrix from two arrays](#matrix-from-two-arrays)
    - [Join two matrixes - add columns](#join-two-matrixes---add-columns)
    - [Find minimum value](#find-minimum-value)
    - [Find index of smallest value](#find-index-of-smallest-value)
    - [Convert to other format](#convert-to-other-format)
    - [Create zero matrix of given shape](#create-zero-matrix-of-given-shape)
    - [Replace all values with logical condition](#replace-all-values-with-logical-condition)
    - [Delete member](#delete-member)
    - [Delete Nan values](#delete-nan-values)
    - [Delete all rows where are Nan](#delete-all-rows-where-are-nan)
    - [Add column](#add-column)
    - [Join two arrays into one](#join-two-arrays-into-one)
    - [Miscellaneous](#miscellaneous)
    - [Sums](#sums)
    - [Dot product / multiplication](#dot-product--multiplication)
    - [Shape](#shape)
    - [Remove non unique values](#remove-non-unique-values)
    - [Reshape](#reshape)
    - [Transpose](#transpose)
    - [Find index (one) with max / min value](#find-index-one-with-max--min-value)
    - [Fill with Nan values](#fill-with-nan-values)
    - [Check if Nan values](#check-if-nan-values)
    - [Zip for arrays](#zip-for-arrays)
- [LOOPZ](#loopz)
  - [IF](#if)
    - [Zda existuje proměnná](#zda-existuje-prom%c4%9bnn%c3%a1)
    - [Ternary operator - If in argument](#ternary-operator---if-in-argument)
  - [FOR](#for)
    - [Return indexes and elements](#return-indexes-and-elements)
  - [Generate list of elements from u1 to u5](#generate-list-of-elements-from-u1-to-u5)
  - [Generate values with strings](#generate-values-with-strings)
    - [For in list comprehension](#for-in-list-comprehension)
    - [Generate list with for cycle and if](#generate-list-with-for-cycle-and-if)
    - [Generate list with more parameters](#generate-list-with-more-parameters)
    - [Nested lists](#nested-lists-1)
  - [WHILE](#while)
- [Functions](#functions)
    - [Jump out of function - return](#jump-out-of-function---return)
    - [Default parameter](#default-parameter)
    - [Global variables](#global-variables)
  - [Funkcions map(), filter(), reduce()](#funkcions-map-filter-reduce)
    - [Reduce - Input sequention into function](#reduce---input-sequention-into-function)
- [Generator](#generator)
- [Dekorator](#dekorator)
- [Module](#module)
- [Classes](#classes)
    - [Create object](#create-object)
    - [Call class method](#call-class-method)
    - [Change atribute of class](#change-atribute-of-class)
    - [Call static method](#call-static-method)
- [FILE I/O](#file-io)
  - [Import fuction from other file](#import-fuction-from-other-file)
    - [Find script's adress](#find-scripts-adress)
    - [Import variables from file in the same folder](#import-variables-from-file-in-the-same-folder)
  - [If file or dir exists](#if-file-or-dir-exists)
  - [Pathlib - new and correct way](#pathlib---new-and-correct-way)
    - [Pathlib as string](#pathlib-as-string)
    - [Find all adress](#find-all-adress)
    - [Work with file](#work-with-file)
  - [Relative path](#relative-path)
  - [Absolute path](#absolute-path)
  - [Add path to files and modules](#add-path-to-files-and-modules)
  - [Create module from folder](#create-module-from-folder)
  - [Working direktory](#working-direktory)
  - [Change current working directiory](#change-current-working-directiory)
  - [Full adress](#full-adress)
  - [Show all files in folder](#show-all-files-in-folder)
  - [Load all files with certain suffix](#load-all-files-with-certain-suffix)
  - [Filter for one type data](#filter-for-one-type-data)
- [Work with files](#work-with-files)
  - [Import txt](#import-txt)
  - [Pickling](#pickling)
- [Try -- Except](#try----except)
  - [Try for all errors](#try-for-all-errors)
  - [Raise exception](#raise-exception)
  - [Assert - Require something or error](#assert---require-something-or-error)
- [Warnings](#warnings)
- [Regular expressions](#regular-expressions)
- [Built in functions](#built-in-functions)
    - [Print](#print)
    - [Range](#range)
    - [Reverse range](#reverse-range)
    - [\__name__ - If file is runned from inside or is imported](#name---if-file-is-runned-from-inside-or-is-imported)
- [Date and time](#date-and-time)
- [Plots, graphs](#plots-graphs)
    - [Plotly timeseries](#plotly-timeseries)
    - [From matplotlib to plotly](#from-matplotlib-to-plotly)
    - [Save picture](#save-picture)
  - [Matplotlib](#matplotlib)
    - [Simple plot](#simple-plot)
    - [Load txt and plot it](#load-txt-and-plot-it)
    - [Histogram](#histogram)
    - [Curves and points](#curves-and-points)
    - [Two graphs](#two-graphs)
    - [More plots with one legend](#more-plots-with-one-legend)
    - [More plots with for cycle](#more-plots-with-for-cycle)
    - [Scatterplot](#scatterplot)
    - [Text plot](#text-plot)
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
- [Requests - API - GET, POST](#requests---api---get-post)
- [Pictures](#pictures)
  - [Show image](#show-image)
  - [Resize](#resize)
  - [Save](#save)
  - [Convert to black and white](#convert-to-black-and-white)
  - [Convert image to matrix](#convert-image-to-matrix)
- [Mahematics, statistics, linear algebra](#mahematics-statistics-linear-algebra)
  - [Square root](#square-root)
  - [Random numbers in normal distribution](#random-numbers-in-normal-distribution)
  - [Random number everytime the same](#random-number-everytime-the-same)
  - [Random numbers in normal distribution matrix shape](#random-numbers-in-normal-distribution-matrix-shape)
  - [Eigen values](#eigen-values)
  - [Inverse matrix](#inverse-matrix)
  - [Determinant](#determinant)
  - [Ones matrix](#ones-matrix)
  - [Matrix transpozition](#matrix-transpozition)
  - [Points generation](#points-generation)
  - [Mean](#mean)
  - [Standard deviation](#standard-deviation)
  - [Add shape - matrix dimensions (rows, columns etc.)](#add-shape---matrix-dimensions-rows-columns-etc)
  - [Number of members - count](#number-of-members---count)
    - [Bins](#bins)
    - [Cumulative sum](#cumulative-sum)
    - [Derivation](#derivation)
    - [Latex dislay](#latex-dislay)
  - [Integration](#integration)
    - [Unbounded integral](#unbounded-integral)
    - [Bounded integral](#bounded-integral)
  - [Round](#round)
  - [Modulo](#modulo)
  - [Power (x on y)](#power-x-on-y)
    - [Describe - Statistical values of list](#describe---statistical-values-of-list)
    - [Statistical values of array](#statistical-values-of-array)
    - [Correlation matrix - values](#correlation-matrix---values)
    - [Correlation matrix - plot](#correlation-matrix---plot)
    - [Correlation (Pearson corr. matrix)](#correlation-pearson-corr-matrix)
    - [Correlation coefficent](#correlation-coefficent)
    - [Test of normal distribution](#test-of-normal-distribution)
- [Machine learning](#machine-learning)
    - [Standardization: mean = 0 and std = 1](#standardization-mean--0-and-std--1)
    - [Normalization (-1,1)](#normalization--11)
- [Signal processig and controll](#signal-processig-and-controll)
- [Miscellaneou](#miscellaneou)
  - [Function for change relative path](#function-for-change-relative-path)
  - [Measure time](#measure-time)
    - [Measure time of function with inputs](#measure-time-of-function-with-inputs)
    - [Measure time on multiline](#measure-time-on-multiline)
    - [Measure between two lines](#measure-between-two-lines)
  - [Show bytcode](#show-bytcode)
- [Performance](#performance)
  - [Type hinting](#type-hinting)
  - [Numba](#numba)
    - [Cuda in Numba](#cuda-in-numba)
  - [Dask](#dask)
    - [Dask formats](#dask-formats)
  - [Force to empty memory](#force-to-empty-memory)
  - [Max execution time python](#max-execution-time-python)
  - [Profiling](#profiling)
- [Whole sections](#whole-sections)
  - [Encoding JSON with Python](#encoding-json-with-python)
- [Pypi export / create own library](#pypi-export--create-own-library)
- [Inside of setup.cfg](#inside-of-setupcfg)
# General

## Show installed libraries
    pip list

Show outdated libraries

    pip list --outdated

## Virtual env
    pip install virtualenv
    virtualenv daniel  # Vytvoří novou virtuálku
    C:\VSCODE\Diplomka\pokus\Scripts\activate.bat  # Activate virtual env

## Requirements - bulk libraries install
Create requirements

    pipreqs --encoding=utf8 C:\VSCODE\Diplomka

Deprecated

    (pip freeze > requirements.txt)

How to use

    pip install -r /path/to/requirements.txt

## One line comment
    # This is comment

## Multiline comment
    """ Víceřádkové komentáře používají tři uvozovky nebo apostrofy
    a jsou často využívány jako dokumentační komentáře k metodám
    """

## Documentation - docstrings
Posible modes - DocBlockR, ReST, Numpy, Google

### reStructured text
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

### docBlockR
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

## Multi line code
    poi = { "1": 3,
            "2": 4, 
            "6": 8 }

or use brackets or \\

    a = (   1 + 2
            + 3 + 4 )

    a = 1 + 2 \
        + 3 + 4

Function example

    f = some_function(  '1' + '2'
                        + '3' - '4')

### Show where python is installed
    where python

# Logical conditions
## Not
    not True # => False
    is not
    !=

## Greater than, lower than
    >=

## And, or
    0 and 2 # => 0
    -5 or 0 # => -5
    0 == False # => True
    if a > b and c > a:

Logical conditions can be combined

    1 < 2 < 3 # => True

## None
None is object (NULL, nil, ...)

    None  # => None

So don't use "==" for comparison. Rather use "is"

    None is None # => True

None, 0, and empty string/list/dictionary is False, everything else True

    bool(0) # => False
    bool("") # => False
    bool([]) # => False
    bool({}) # => False

# Variables
    y = int(2.8)

    x += 1 # Zkrácený zápis x = x + 1. Pozor, žádné x++ neexisuje

Int divided by int
    3 / 2  # = 1.5
    3 // 2  # = 1

## Declaration of more variables at once
    a = b = c = 1

    a,b,c = 1,2,"john"

### Swap variables values
    e, d = d, e # d is now 5, e is now 4

    name = ['mike', 'john', 'steve']  

    age = [20, 32, 19]

    for x,y in zip(name, age):

    globals()[x] = y  # mike = 20 ...

    uname = ['u{}'.format(n) for n in range(7)] # [u1, u2, u3...]

###Check if variable exist
    if 'myVar' in locals():

## Import variables from other modules
Creat config.py

There for example

    x=1

In main then use

    confi.x = 2 ....

### Find name of variable, list or dictionary
    my_var_name = [k for k,v in globals().items() if v == promenna][0]

# DATA TYPES
    type(a)  # Return type

### Type of variable as condition
    if isinstance(o, str):  # Check if it's string (or int etc...)

More types at once

    isinstance(y,  (np.ndarray, np.generic)  )
    if a is list: # Zjistí, zda jde přímo o string
    pd.DataFrame  # For dataframe

Also work if object is includes in class

### If exist
    if callable(objekt)

## String
Strings " or ' and can contain UTF8 symbols

    "This is string."
    'This is also string.'

In python 3

    print('strings are now utf-8 \u03BCnico\u0394é!')  # strings are now utf-8 μnicoΔé!

Strings can use + but don't use

    "Hello " + "world!" # => "Hello world!"

Can be concatenated without '+'

    "Hello " "world!" # => "Hello world!"

String is list of symbols

    "This is list"[0] # => 'T'

### Format
Old

    '%s  %s' % ('one', 'two')

Newer

    '{} {}'.format('one', 'two')
Format can be used multiple times

    "{0} {1} stříkaček stříkalo přes {0} {1} střech".format("tři sta třicet tři", "stříbrných")

You can use named arguments

"{jmeno} si dal {jidlo}".format(jmeno="Franta", jidlo="guláš") # => "Franta si dal guláš"

###Newest and fastest format- f'strings'
    f"Hello, {name}. You are {2 * 17}. Also functions {name.lower()}."
    If you use """ no escape symbols will be used

Also can use dictionaries, but "" is necesarry
Dont use # in f strings

### String to code
    exec(mycode)
    x = eval("2+2") # number ze stringu

### Join - concatenate
    words = ["this", 'is', 'a', 'list', 'of', "strings"]
    ' '.join(words)  #returns "This is a list of strings"

# List
    sez = []
    sez.append(1) # sez je nyní [1]
    a.insert(2, 2) # do indexu 2 vloží 2
    sez.pop() # Vymaže poslední hodnotu
    sez.remove(2) # Vymaže první 2 v seznamu
    del a[1] # vymaže druhý prvek v seznamu
    del m[:] # Vymaže všechny elementy
    a + b # seřadí za sebe
    b.extend(a) # Seřadí za sebe

If list a = list b and we change one of them, the other also change therefor

    Listb = lista.copy()

### Check if list is empty or not
    if a:
    if not a:

### Create list from 0 to 10
    l = range(10) #  [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]

### Create list - List comprehension
    [x*5 for x in range(5)] #[0, 5, 10, 15, 20]
    [x for x in range(5) if x%2 == 0] #[0, 2, 4]
    [a if a else  2  for a in  [0,1,0,3]]

List comprehension from more entities

    [(i, j) for i, j in zip(list_1, list_2)] # [(1, 'a'), (2, 'b'...]

### Function in list generator

    [pricist_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
    [x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

### One value more times
    listOfStr = ['Hi'] * 3 # ['Hi', 'Hi', 'Hi']

### Multiple list
    my_list =  [1,  2,  3,  4,  5]
    my_new_list =  [i *  5  for i in my_list]

### Find index
    a.index(3)

### Access members
    sez = [1, 2, 3, 4]
    sez[0]  # => 1
    sez[-1]  # => 3

#### Slices
    sez[1:3]  # => [2, 4]
    sez[2:]  # => [4, 3]
    sez[:3] # => [1, 2, 4]

Every second member

    sez[::2] # =>[1, 4]

### Reverse
    sez[::-1] # => [3, 4, 2, 1]
Or

    a.reverse()

### Iterate in reverse order
    for i in reversed(a):

### Nested lists
    t = [[1,2], [3,4]]
    print(t[1][1])  # 4

### Every first member of nested lists
    L = [[[0,1,2],[3,4,5],[6,7,8]],  [[0,1,2],[3,4,5],[6,7,8]],  [[0,1,2],[3,4,5],[6,7,8]]]
    R = [[x[0]  for x in sl ]  for sl in L ]
    Lst = [[1,2,3],[11,12,13],[21,22,23]]

Or

    list(zip(*lst))[0]

### Remove member
    del sez[2] # sez je nyní [1, 2, 3]

### Minimum
    youngest = min(ages)

### Find maximum and it's index
    m = max(a)
    [i for i, j in enumerate(a) if j == m] # pro a = [1,2,0]  # 1

### Sum
    suma = sum(ages)

### If member exist

    1 in sez # => True

### Length of list
    len(sez) # => 6

### Every value just once
    t =  [1,  2,  3,  1,  2,  5,  6,  7,  8]
    list(set(t))  # [1,  2,  3,  5,  6,  7,  8]

### Intersection and inclusive
    Zip(List1a2, Listb1b2) # {(a1, b1), (a2, b2)}
    j2 = [i for i in j if i >=  5]

### Add first with first, second with second
    [a + b for a, b in zip(list1, list2)]

### List of functions
    def func1():return 1
    def func2():return 2
    def func3():return 3
    fl = [func1,func2,func3]
    [f() for f in fl] # [1, 2, 3]

### How many times members in list
    print( collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))

## Deque
You can iterate from both sides

    append(x)  # Add x to the right side of the deque.
    appendleft(x)  # Add x to the left side of the deque.
    clear()  # Remove all elements from the deque leaving it with length 0.
    count(x)  # Count the number of deque elements equal to x.
    extend(iterable)  # Extend the right side of the deque by appending elements from the iterable argument.
    pop()  # Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
    popleft()  # Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
    remove(value)  # Remove the first occurrence of value. If not found, raises a ValueError.
    reverse()  # Reverse the elements of the deque in-place and then return None.
    rotate(n=1)  # Rotate the deque n steps to the right. If n is negative, rotate to the left.


## Tuple
Tuple is like list but imutable  !!! [] i can change - () i cannot change !!!

    tuple = (1, 2, 3)
    tuple[0]  # => 1
    tuple[0] = 3  # Raise TypeError

# Dictionary
    empty_dic = {}
    dic = {"jedna": 1, "dva": 2, "tři": 3}
    dict_variable = {key:value for (key,value) in dictonary.items()}

### Add value
    Slovnik['čtyři'] = 4  # If key is already there it's updated

### Create dictionary from two lists
    name = ['mike', 'john', 'steve']  
    age = [20, 32, 19]
    dic=dict(zip(name, age))

### Miscelanious
    del thisdict['b'] # vymaze seznam
    thisdict.has_key('e') returns False
    thisdict.items() returns [('a', 1), ('c', 'eggs')]

All keys

    dic.keys()
You need list sometimes not iterables

    list(dic.keys())

### Last key in dictionary
    max(stats)

### For cycle for all keys
    for s in stats:
        print(s)

### Maximum value and its index
    stats = {'a':1000, 'b':3000, 'c': 100}
    maxname = max(stats, key=stats.get))
    maxvalue = stats(maxname)

### Values
    list(dic.values()) # => [3, 2, 1]
    "jedna" in dic # => True if value is in dictionary
    dic.get("čtyři") # => None - don't raise error if key not in dic
    dic.setdefault("pět", 5) # dic["pět"] default 5

### Find key from value
    list(modelsnames.keys())[list(modelsnames.values()).index(prear)]

### For cycle for dictionaries
    for k in dict: # Iteruje přes všechny klíče
        print(k)

    for k, v in dict.items(): # Iteruje řes všechny klíče a hodnoty
        print(k,v)

## Join two dictionaries
    c = {**a, **b}

### Enumerate in dictionaries
    for i, (j, k) in enumerate(aa.items()):

### Dictionary as arguments into function
    t = (47,11)
    d = {'x':'extract','y':'yes'}
    f(*t, **d) # It's the same as f(47, 11, x=extract, y=yes)

### Nested dictionaries - for examples name of functions and it's parameters
    models = {"AR (Autoregression)": ar, "Linear neural unit": autoregLNU}
    modelsparameters = {"AR (Autoregression)": {"predicts": predicts}, "Linear neural unit": {"predicts": predicts}}
    modelscomplet = zip(models.keys(), models.values(), modelsparameters.values())
    modelsresults = []

    for i, j, k in modelscomplet:
        modelsresults.append({i: j(data0, **k)})

### Nested dictionaries - Find minimum
    for key, value in best_of_data.items():
        for inkey, invalue in value.items():
            if invalue < top:
                best_model_name = key
                best_data = inkey
                top = invalue

### Dictionary comprehension
    {x: x**2 for x in range(1, 5)} # => {1: 1, 2: 4, 3: 9, 4: 16}
    {pismeno for pismeno in "abeceda"} # => {"d", "a", "c", "e", "b"}

# Set
It is not oredered and every value is just once!

    empty_set = set()
    set = {1, 1, 2, 2, 3, 4}  # {1, 2, 3, 4}
    set.add(5)  # {1, 2, 3, 4, 5}
    jina_set = {3, 4, 5, 6}

Intersect of 2 sets

    set & jina_set # => {3, 4, 5}

Union

    set | jina_set # => {1, 2, 3, 4, 5, 6}

Exception

    {1, 2, 3, 4} - {2, 3, 5} # => {1, 4}

If member exist

    2 in set # => True
    9 in set # => False

# Iterator
    iterator = iter(iterable)

Next value

    next(iterator) # => "jedna"

# Dataframe
Panda library is necessary

### Import from csv
    data = pd.read_csv(
        "data/files/complex_data_example.tsv",
        sep='\t' # Tab-separated value file.
        quotechar="'", # single quote allowed as quote character
        dtype={"salary": int}, # Parse the salary column as an integer
        usecols=['name', 'birth_date']. # Ma byt carka podle me - Only columns
        parse_dates=['birth_date'], # Intepret the birth_date column as a date
        skiprows=10, # Skip the first 10 rows of the file
        na_values=['.', '??'] # Take any '.' or '??' values as NA
)

### Access column
    df['name']

### Subset of columns
With name

    df1 = df[['a','b']]
    df[df.columns[0]]  # Columns return name of column

with index

    df1 = df.iloc[:,0:2]

### Column to new dataframe
    df.pop('class')
    column_for_prediction_dataframe = data_for_predictions_full[[predicted_column_name]]

### Subset of rows and columns
    df1 = df.loc['Jirka']
    df1 = df.iloc[0]  # First row

###Logical conditions
    df = data.loc[data['Name'] == Marko]
    df = corr_column.loc[:, corr_column['aa'] >= 0.5]

### Concat 2 columns
    df1['state_and_code'] = df1['State'] + df1['State_code']

### Find index from column name
    a = df.columns.get_loc("pear")

### Zvolit index ze sloupce
    Df.set_index('date', inplace=True)
    df.reset_index(level=None, drop=False, inplace=False)

### Create
one column dataframe

    s2 = pd.Series([1,2,3,4])

dataframe

    s2 = pd.DataFrame([1,2,3,4])

from dictionary

    newdatf = DataFrame.from_dict(newlist, orient='index')

from array

    pd.DataFrame(data=data[1:,1:], # values
        index=data[1:,0], # 1st column as index
        columns=data[0,1:])

### Convert into array
    df['a'].values
    b=dat.iloc[:,1:].values # každý sloupec zvlast

### Convert into list
    df['a'].values.tolist()

### Date and time and datetime, range
Convert from datetime to time, the same to datetime

    dataframe['DimTimeId'] = dataframe['EventStart'].dt.time

Range

    dataframe_to_sql['EventStart'] = pd.date_range(start=start, periods=lenght+1, freq='H')

Datetime from values

    start = pd.Timestamp(year=year, month=month, day=day, hour=hour)

### Join 2 dataframes - Add rows
    df3 = pd.concat([df1, df2])

### Join 2 dataframes - Add columns
    df3 = pd.append([df1, df2]) # může být , ignore_index

### Transpose - Rows into columns
    df = df.T

### Save into CSV
    Df.to_csv('newcsv.csv') # bez názvů , header=False

### Group by
    tips.groupby('day').agg({'tip': np.mean, 'day': np.size})

### Moving average
    df['STD'] = pd.rolling_std(dff, 2)

### Remove outliers
    df = df[ (df['STD'] < df_std) ]

### Resample dataframe
    series.resample('3T').sum() # Méně řádků na výstupu

# Numpy Array
Create

    ar = np.array([1,2,3], [4, 5, 6])

Přístup k prvkům

    a = ar[1, 2]  # 5

### Convert
    datta.tolist() # Převede na list -- mozna to je omyl s dataframem

On one dimensional list

    qw = np.array(data).reshape(-1)
qw = qw.tolist()

### Slicing
    a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
    #    [[1 2 3]
    #    [3 4 5]
    #    [4 5 6]] 

#### Only column - not retain shape
    a = a[:, 1]  # [2 4 5]

#### Columns with same shape
    a = a[:, 1:2]  #   [[2]
                        [4]
                        [5]]

### Only rows
    a = a[1, :]

### Matrix from two arrays
    np.vstack([a,a])

### Join two matrixes - add columns
    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])
    np.stack((a, b))  # array([[1, 2, 3],
                      #        [2, 3, 4]])

### Find minimum value
    min = amin(a, axis=1)

### Find index of smallest value
    ind = np.unravel_index(np.argmin(models_parameters), shape=models_parameters.shape)

### Convert to other format
    arr.astype(int) # convert on np.int
    arr.item() # from np.int convert on int

### Create zero matrix of given shape
    zeros = numpy.zeros_like

### Replace all values with logical condition
    x[x > .5] = .5

### Delete member
    test = np.delete(test, 1, axis=0) # There need to pe variable before!  axis 0 are rows, 1 are columns

### Delete Nan values
    asd = asd[~np.isnan(asd)]

### Delete all rows where are Nan
    x = x[~np.isnan(x).any(axis=1)]

### Add column
    x = np.array([[10,20,30], [40,50,60]])
    y = np.array([[100], [200]])
    print(np.append(x, y, axis=1))

### Join two arrays into one
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

### Miscellaneous
    X = np.append(X, 3)  # Add element to the end
    a = np.insert(a,3,[11,12])  # Into a on index 3 insert [11,12], next parameter can be axis
    np.delete`(*arr*, *obj*, *axis=None*)
    np.roll(x,2) # Posune array o 2 doprava
    wo = np.array([1,2,3]) # Shape (3,)
    wo = np.array([[1,2,3,4,5]]) # Shape (1,5)
    wo = np.array([[1],[2],[3],[4],[5]]) # Shape (5,1)
    Numpy.shape(matice) # `(n,m) počet řádků, sloupců atd`. `Y.shape[0] pouze řádky`
    mat = np.array([[2., 4.],[4., 2.]])
                # [[ 2. 4.]
                #  [ 4. 2.]]

### Sums
Axis 0 is for sums on columns

    np.sum([[0, 1], [0, 5]], axis=0)  # array([0, 6])
    np.sum([[0, 1], [0, 5]], axis=1)  # array([1, 5])

### Dot product / multiplication
    x = np.array([1,2,3])
    w = np.array([1,2,3])
    v = x*w # [1, 4, 9]
    v = np.dot(x, w) # 14

### Shape
    z = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
    z.shape  # (3, 4)

### Remove non unique values
    unique = np.unique(array, axis=0)

### Reshape
    reshape -1 add members automatically
    z.reshape(-1) # array([ 1,  2,  3,  4,  5,  6])
    z.reshape(-1,1)

        # array([[ 1],
        #        [ 2],
        #        [ 3],
        #        [ 4],
        #        [ 5],
        #        [ 6]])

    z.reshape(-1, 2)
        # array([[ 1,  2],
        #        [ 3,  4],
        #        [ 5,  6],
        #        [ 7,  8],
        #        [ 9, 10],
        #        [11, 12]])

    a = np.array([[1,2,3], [4,5,6]])
    np.reshape(a, 6, order='F')
        # array([1, 4, 2, 5, 3, 6])

### Transpose
    data.transpose(1,0,2)  # From (10, 100, 1000) create (10, 1000, 100)

### Find index (one) with max / min value
    np.argmax(a)  # or argmin. Also can use parameter axis

### Fill with Nan values
    z = np.zeros(N)
    z.fill(np.nan)

### Check if Nan values
    if not np.isnan(z[i]):

### Zip for arrays
  def azip(*args):
    iters = [iter(arg) for arg in args]
    for i in itertools.count():
      yield tuple([it.next() for it in iters])

# LOOPZ
## IF
### Zda existuje proměnná
    if f:
        print("f exist")
    if promenna > 10:
    print("proměnná je velká jak Rusko")
    elif promenna < 10:
    print("proměnná je menší než 10")
    else:
    print("proměnná je právě 10")
    continue # Jump to other operation
    break # Jump out of the cycle
    pass 3 # Do nothing

### Ternary operator - If in argument
    state = "nice" if is_nice else "not nice"

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
        print("x je {} a y je {}".format(x, y))
        return x + y  # Return values with return
    secist(5, 6)  # Call the function with parameters, return 11
    secist(y=6, x=5)  # Named arguments
    def vrat_argumenty(*argumenty):  # Variable number of arguments
        return argumenty
    vrat_argumenty(1, 2, 3)  # => (1, 2, 3)
    def vrat_pojmenovane_argumenty(**pojmenovane_argumenty):  # Varaiable number of named arguments
        return pojmenovane_argumenty
    vrat_pojmenovane_argumenty(kdo="se bojí", nesmi="do lesa")  # {"kdo": "se bojí", "nesmi": "do lesa"}
    def vypis_vse(*args, **kwargs):  # You can use combination
        print(args, kwargs) # print() vypíše všechny své parametry oddělené mezerou

### Jump out of function - return
    def print():
        a = 8
        if a > 5:
            return
        print(2)

### Default parameter
    def funkce(y, lags=50): If we use lags in call, it will be overwritten
    vypis_vse(1, 2, a=3, b=4) # Use: (1, 2) {"a": 3, "b": 4}
    tuple = (1, 2, 3, 4)
    dic = {"a": 3, "b": 4}
    vypis_vse(tuple)  # Is like vypis_vse((1, 2, 3, 4)). One parameter - tuple
    vypis_vse(*tuple)  # Is like vypis_vse(1, 2, 3, 4)
    vypis_vse(**dic)  # Is like vypis_vse(a=3, b=4)
    vypis_vse(*tuple, **dic)  # Is like vypis_vse(1, 2, 3, 4, a=3, b=4)

### Global variables
    x = 5
    def nastavX(cislo):  # Local variable override global
        x = cislo  # => 43
        print(x)  # => 43
    global x
    def nastavGlobalniX(cislo):
        print(x) # => 5
        x = cislo # Nastaví globální proměnnou x na 6
        print(x) # => 6
Functions are objects

    def vyrobit_scitacku(pricitane_cislo):
        def scitacka(x):
            return x + pricitane_cislo
        return scitacka
    pricist_10 = vyrobit_scitacku(10)
    pricist_10(3)  # => 13

## Funkcions map(), filter(), reduce()
** From functional programming**

Map call funtion (first parameter) on all objects (second parameter)

    map(pricist_10, [1, 2, 3])

Filter create list (First paratemer), where function is true (second parameter)

    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)  # [-5, -4, -3, -2, -1]

### Reduce - Input sequention into function
    from functools import reduce
    def do_sum(x1, x2): return x1 + x2
    reduce(do_sum, [1, 2, 3, 4]) # 10

# Generator
Generators are functions, that instead return have yield

    def multiplier_2(sequention):
        for i in sequention:
        yield 2 * i

Generator generate values one after one, when it\s needed. Instead of been generated all at once
Example of generator is range(10000)

# Dekorator
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

    from my_module import my_function

    help(module)  # Help with module

    dir(module)  #  Show objects in module

# Classes
    class Clovek(object):  # Class Human is child (it inherits from) class object

        druh = "H. sapiens"  # Class variable - it's shared with all objects

        def __init__(self, jmeno):
            self.jmeno = jmeno  # Add parameter to object


Class method

    def rekni(self, hlaska):
        return "{jmeno}: {hlaska}".format(jmeno=self.jmeno, hlaska=hlaska)

    @classmethod  # First parameter is class and can be changed in subclasses
    def vrat_druh(cls):
        return cls.druh

    @staticmethod  # Do not depend on object - like a normal function and is immutable
    def odkaslej_si():
        return "*ehm*"

Example of class method

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    date2 = Date.from_string('11-09-2012')

### Create object
    d = Clovek(jmeno="David")
    a = Clovek("Adéla")
    print(d.rekni("ahoj"))  # "David: ahoj"
    print(a.rekni("nazdar"))  # "Adéla: nazdar"

### Call class method
    d.vrat_druh() # => "H. sapiens"

### Change atribute of class
    Clovek.druh = "H. neanderthalensis"
    d.vrat_druh() # => "H. neanderthalensis"
    a.vrat_druh() # => "H. neanderthalensis"

### Call static method
    Clovek.odkaslej_si() # => "*ehm*"

# FILE I/O
## Import fuction from other file

    from analyze import analyze  # First name of file, than function

### Find script's adress
    os.path.dirname(__file__)

### Import variables from file in the same folder
    import file  # Then call file.value
    from file import * # Now call just variable

## If file or dir exists
    from pathlib import Path
    my_file = Path("/path/to/file")
    if my_file.is_file():  # File exists
    if my_file.is_dir():  # Directory exists
    if my_file.exists():   # File or dir exists

## Pathlib - new and correct way
    from pathlib import Path
    path = pathlib.Path.cwd()

    data_folder = Path("folder")
    file_to_open = data_folder / "raw_data.txt"

### Pathlib as string
    path.as_posix()

### Find all adress
    path = pathlib.Path('test.md')
    path.resolve() # ('/home/gahjelle/realpython/test.md')
    path.resolve().parent == pathlib.Path.cwd() # False

### Work with file
    filename = Path("source_data/text_files/raw_data.txt")

    print(filename.name) # prints "raw_data.txt"
    print(filename.suffix) # prints "txt"
    print(filename.stem) # prints "raw_data"
    if not filename.exists():
        print("Oops, file doesn't exist!")
    else:
        print("Yay, the file exists!")

**Next rows just historical - Do not do it that way**
## Relative path
    *../data/test_file.csv # ..znamená parent složka*
    *from os import path*
    *file_path = path.relpath("data/data.txt")*

## Absolute path
    os.path.abspath(\__file__)

## Add path to files and modules

    import sys
    sys.path.insert(0, '/path/to/application/app/folder')
    import file
    sys.path # vytiskne adresáře, ke kterým má soubor přístup

## Create module from folder

Add file `__init.py__`
Inside do all imports from .autoregLNU import autoregLNU
Use relative imports with dots

## Working direktory

    import os
    cwd = os.getcwd()
    os.chdir(r"C:\Users\...")

## Change current working directiory 
    cwd = os.getcwd() + r"\diplomka"
    os.chdir(cwd)

## Full adress
**Use normal slash!!**

    import os
    data_folder = "folder/nextfolder/"
    file_to_open = data_folder + "data.txt"

For example if jupyter do not see some files

    script_dir0 = os.path.abspath('') # C:\VScode

Next

    script_path = os.path.abspath(\__file__)  # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0]  #i.e. /path/to/dir/
    rel_path =  "2091/data.txt"
    abs_file_path = os.path.join(script_dir, rel_path)  # Result is relative '/path/to/dir/2091/data.txt'

    filename = os.path.join(script_path,  '../same.txt')  # We can use name of file

    script_dir = os.path.dirname(\__file__)  # We can use adress of file

You can also do

    script_dir = os.path.dirname(\__file__)
    rel_path = "test_ data/realna_data_klapky.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

## Show all files in folder
    all_files = os.listdir("test/")

## Load all files with certain suffix
    import glob
    imgs=glob.glob("*.png")  # Všechny obrázky ze složky

**Wildcard**

    for name in glob.glob('dir/file?.txt'):
        print name

    for name in glob.glob('dir/*[0-9].*'):
        print name

## Filter for one type data
    txt_files = filter(lambda x: x[-4:]  ==  '.txt', all_files)

# Work with files
    f = open("test.txt") # open file in current directory
    f = open("C:/Python33/README.txt") # specifying full path
    'r'  Open a file for reading. (default)
    'w'  Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    'x'  Open a file for exclusive creation. If the file already exists, the operation fails.
    'a'  Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
    't'  Open in text mode. (default)
    'b'  Open in binary mode.
    '+'  Open a file for updating (reading and writing)
    f.close()
    with open("test.txt",'w')  as f:

    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

!!!Use because this will autamatically close the file finally

    f = open("test.txt",'r',encoding =  'utf-8')
    f.read(4) # read the first 4 data - 'This'
    f.read(4) # read the next 4 data - ' is '
    f.read() # read in the rest till end of file - 'my first file\nThis file\ncontains three lines\n'
    f.read() # further reading returns empty sting

## Import txt

    from numpy import loadtxt
    x=loadtxt('realna_data_klapky.txt')

## Pickling
Save file in binary format

    import pickle
    d = {"a": 1, "b": 2}
    with open(r"someobject.pickle", "wb") as output_file: cPickle.dump(d, output_file)

Load files

    with open(r"someobject.pickle", "rb") as input_file: e = cPickle.load(input_file)

Result is e = {"a": 1, "b": 2}**

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

Print founded error

    try:
        linux_interaction()

    except AssertionError as error:
        print(error)

##  Try for all errors
    except Exception as e:

## Raise exception
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

## Assert - Require something or error
    assert (x > 4), 'What happened'

# Warnings
    import warnings
    warnings.warn("Warning...........Message")

    warnings.filterwarnings('error', message=r".*HessianInversionWarning*")  # Errory budou brány jako chyby u upozornění, kde je slovo HessianInversionWarning"
    warnings.filterwarnings('always', category=DeprecationWarning)  # Errory typu category budou vždy ukázány
    warnings.filterwarnings('ignore')  # Errory budou vždy ignorovány

    "default"
    print the first occurrence of matching warnings for each location (module + line number) where the warning is issued

    "error"
    "ignore"
    "always"
    "module"
    print the first occurrence of matching warnings for each module where the warning is issued (regardless of line number)

    "once"

# Regular expressions
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

# Built in functions
### Print
    print('as', a, 'fegg') # používáme čárky, jde pak spojit string s proměnnou

### Range
    x=range(n+1) # x=0,1,2,...,n

### Reverse range
    for i in reversed(range(5)):
        print(i) # 4, 3, 2, 1

### \__name__ - If file is runned from inside or is imported

    if __name__ == "__main__":

# Date and time
    now = dt.datetime.now() #datum i čas
    time.sleep(1) # počká 1 vteřinu

# Plots, graphs
##Plotly
    import plotly as py

    fig = dict( data=data, layout=layout )
    py.offline.plot( fig, filename='d3-cloropleth-map' )

Nebo

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
### Simple plot
    pyplot.plot(test)

### Load txt and plot it
    from numpy import loadtxt # pro jeden sloupeček čísel
    from matplotlib.pyplot import *
    x=loadtxt('realna_data_klapky.txt')
    figure(figsize=(20,5))
    plot(x,'-o',label="x");xlabel('i');ylabel('x [sec]');grid();title("realna_data_klapky.txt")
    legend();show()
    plt.savefig('fig1.png', dpi =  300) # uloží graf

### Histogram
    figure(figsize=(20,5))
    nbins=int(round(1+3.3*log(N))) # Sturge's rule, ale zalezi na datech, atd
    xlabel("x");ylabel("cetnosti"),title("cetnosti hodnoty x v intervalech");grid()
    a=hist(x,bins=nbins) # vraci dve pole a histogram, tj a[0]=cetnosti, a[1]=intervaly
    print "cetnosti=",a[0]
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

First number is how much rows and second how much columns
Third number is which graph is it - first, second etc.

    a=hist(x,nbins,normed=True) ;# pro vizualni posouzeni
    grid();ylabel("$\\approx f(x)$");xlabel("x")
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

## Table
    from prettytable import PrettyTable
    x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    x.add_row(["Adelaide", 1295, 1158259, 600.5])

## Symbolic functions
    import sympy as smp
    from sympy.plotting import plot as Plot
    z=smp.Symbol("z")
    fz=1/smp.sqrt(2*smp.pi)*smp.exp(-(z**2/2))
    disp("f(z)=",fz)
    Plot(fz)
    disp("F_{x\_median}=\int_{-\infty}^{x_{median}="+str(mu)+"}=",smp.integrate(fz,(z,-oo,0)))
    disp(" z_{modus}= 0 \Leftrightarrow \dfrac{d f(z)}{ dz} =0=",smp.diff(fz,z))

# Libraries
## If pip cannot be installed by SSL errorr
    pip install ipykernel --upgrade pip --trusted-host pypi.org

# Jupyter
    jupyter kernelspec list # Ukáže seznam kernelů
    jupyter kernelspec uninstall nazev # Odinstaluje kernel

## Autoreload
Load imported module everytime

Reload all modules imported with %aimport every time before executing the Python code typed.

    %autoreload 1

Reload all modules (except those excluded by %aimport) every time before executing the Python code typed.

    %autoreload 2

Sometimes its necessary to import concrete modules

    %aimport modul1, modul2


## Link
    ‚''
    [Youtubeplaylist](<https://www.youtube.com/>)
    ‚''

## Image
    ‚''
    <img src="img/Gini.png" width=400>
    ‚''

## Youtube
    from IPython.display import YouTubeVideo
    YouTubeVideo('7VeUPuFGJHk')

## Show all images from folder
    import os
    from IPython.display import display, Image
    names = [f for f in os.listdir('../images/ml_demonstrations/') if f.endswith('.png')]
    for name in names[:5]:
    display(Image('../images/ml_demonstrations/' + name, width=100))

# Requests - API - GET, POST

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

# Pictures
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

# Mahematics, statistics, linear algebra
## Square root
y = 9**(1/2)  # 3

## Random numbers in normal distribution
    w = np.random.randn(3)

## Random number everytime the same
    np.random.seed(5)

    w = np.random.randn(3)  # [ 0.44122749 -0.33087015  2.43077119]
    w = np.random.randn(3)  # [ 0.44122749 -0.33087015  2.43077119]

## Random numbers in normal distribution matrix shape
    s = np.random.normal(mu, sigma, 1000)
    numpy.random.randn(3, 4) #[ 1.33262386 -0.88922967 -0.07056098]

        #    [[ 1.33262386 -0.88922967 -0.07056098 0.27340112]
        #     [ 1.00664965 -0.68443807 0.43801295 -0.35874714]
        #     [ -0.19289416 -0.42746963 -1.80435223 0.02751727]]

## Eigen values
    np.linalg.eig(mat)

## Inverse matrix
    np.linalg.inv(mat)

## Determinant
    np.linalg.det(mat)

## Ones matrix
    np.ones([[3,3]])

## Matrix transpozition
    A.T

## Points generation
    t = np.linspace(0,20,1000) #generuje řadu čísel se stejnými intervaly (Začátek konec, počet)

    t = np.arange(start, stop, step)
    t = np.arange(3)  # 0, 1, 2

## Mean
    np.mean(data)

## Standard deviation
    np.std(data)

Or

    from statistics import stdev
    sample = [1, 2, 3, 4, 5]
    std = statistics.stdev(sample)

## Add shape - matrix dimensions (rows, columns etc.)
    y.shape

## Number of members - count
    y.size

### Bins
    binss = numpy.histogram(data, bins)  # binss[0] hodnoty binss[1]

### Cumulative sum
    y = np.cumsum(x)

### Derivation
    z = np.diff(y)                      

### Latex dislay
    from IPython.display import display, Math, Latex
    display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))

## Integration
### Unbounded integral
For some functions with we need to load from SymPy exp(). Otherwise use numpy functions.

    import sympy as smp
    from sympy import exp as e
    x=smp.Symbol("x")
    f=e(-x)
    disp("f=",f)
    intf=smp.integrate(f)
    disp("\int " + dfrac(f)+"dx=",intf) # po \int musim byt mezera

### Bounded integral
    intf=smp.integrate(f,(x,0,1))
    disp("\int_0^1" + dfrac(f)+" dx=",intf.evalf())

## Round
    x = round(5.76543, 2)

## Modulo
    7 % 3 # => 1

## Power (x on y)
    2**4 # => 16

### Describe - Statistical values of list
    List.describe()

### Statistical values of array
    from scipy import stats
    print(stats.describe(data[1]))

### Correlation matrix - values
    x = dat.corr()

### Correlation matrix - plot

    scatter_matrix(dat, figsize=(16,12), alpha=0.3)
    plt.show()

### Correlation (Pearson corr. matrix)
    scoreTable = dat.corr(method='pearson')
    dat.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)

### Correlation coefficent
    np.corrcoef(data, data_n)

### Test of normal distribution
    from statsmodels.stats.stattools import jarque_bera
    score, pvalue, _, _ = jarque_bera(mdl.resid)
    if pvalue < 0.10:
        print 'We have reason to suspect the residuals are not normally distributed.'
    else:
        print 'The residuals seem normally distributed.'

# Machine learning
### Standardization: mean = 0 and std = 1
    from sklearn import preprocessing
    clustervar['ALCEVR1']=preprocessing.scale(clustervar['ALCEVR1'].astype('float64'))

Or

    names = dat.columns
    scaler = preprocessing.StandardScaler()
    scaled = scaler.fit_transform(datastand.T)
    scaled = pd.DataFrame(scaled, columns=names)
    scaledvalT = scaled.values
    scaledval = scaledvalT.T

Or

    normalized_X = preprocessing.normalize([x_array])

Denormalization

    ach = scaler.inverse_transform(scaled)

### Normalization (-1,1)
    datat = data.reshape(-1, 1) # občas je per = preprocessing.MinMaxScaler(feature_range=(-1, 1))
    rescaledXT = scaler.fit_transform(datastand)

# Signal processig and controll
# Miscellaneou

## Function for change relative path
import os

try:
    os.chdir(os.path.join(os.getcwd(), '..\..\..\relcesta'))
    print(os.getcwd())

except:
    pass

## Measure time
    import timeit
    timeit.timeit(moje funkce)

### Measure time of function with inputs
    import timeit, functools
    t = timeit.Timer(functools.partial(autoregLNU, trainall[0]))
    print (t.timeit(20))

### Measure time on multiline
    t = timeit.Timer(''' ‚''
    from models import ar, autoregLNU
    from data_prep import split
    import numpy as np
    ‚'' ''', 'gc.enable()')
    print(t.timeit(3))  # 3 - measure three times

### Measure between two lines
    import time
    start = time.time()
    print("hello")
    end = time.time()
    print(end - start)

## Show bytcode
    import dis
    dis.dis("dict()")

    import numpy as np...
    1           0 LOAD_NAME                0 (dict)
                  2 CALL_FUNCTION            0
                  4 RETURN_VALUE

##The \__call__ method (Allow input of object to function)

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

    These are the results of the previous function:

    1 42 2.75 3.25
    2 42 3.5 9.5
    3 42 4.25 26.75
    4 42 5.0 61.0
    5 42 5.75 118.25
    6 42 6.5 204.5
    7 42 7.25 325.75
    8 42 8.0 488.0
    9 42 8.75 697.25

Magic methods (For example for change of + behaviour)
What happens when we create an object in python class ?

    class  Address(object):

        def __init__(self, city, pin):
            self.city = city
            self.pin = pin

Creating instance of the object

a =  Address("hyderabad",  "500082")

before creating the instance of the class **"__new__"** method will be called. This method takes  parameter **"class", "args", "kwargs" **and  It will bind the *data type* to given class. After it will call the **"__init__"** method with arguments and keyword arguments.

    a =  Address.__new__(Address)
    type(a)

    __main__.Address
    a.city

    # AttributeError:  'Address'  object has no attribute 'city'

Object created but not initialised that's the reason we get error

    a.__init__("hyderabad",  "500082")

Now we can access the attributes

    a.city

We can cosider bilt-in methods of an object as magic methods. We can also override the built-in methods functionality.

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

Let's take an example to override the functionality "+" [__add__] operator

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

Now use the "+" operator with two vectors

    v1 =  Vector(1,  2)
    v2 =  Vector(10,  13)
    v3 = v1 + v2
    v3.values  # (11,  15)

When statement "v3 = v1 + v2 " executes "__add__" is called and it returns a new Vector object.


# Performance
## Type hinting
    def sentence_has_animal(sentence: str) -> bool:
      return "animal" in sentence
    sentence_has_animal("Donald had a farm without animals")
    # True

## Numba
    from numba import njit

Works on all functions

    @njit()
    def func():  # atd...

Or

    hypot = jit(fce)

Or

    @vectorize
    def function(a, b):

Or direct data formats

    @jit(int32(int32, int32))
    def function(a, b):

### Cuda in Numba
    from numba import cuda
    @cuda.jit(device=True)
    def function(a, b):

## Dask
    @delay
    def sq(x):
        return x**2# Now you can use these functions any way you want, Dask will 
    result.compute()

### Dask formats
    import dask.array as da  # Arrays implement the Numpy API
    x = da.random.random(size=(10000, 10000),
                        chunks=(1000, 1000))
    x + x.T - x.mean(axis=0)

    import dask.dataframe as dd  # Dataframes implement the Pandas API
    df = dd.read_csv('s3://.../2018-*-*.csv')
    df.groupby(df.account_id).balance.sum()

    from dask_ml.linear_model import LogisticRegression  # Dask-ML implements the Scikit-Learn API
    lr = LogisticRegression()
    lr.fit(train, test)

##Show task structure
    .visualize()

## Force to empty memory
    import gc
    gc.collect()

## Max execution time python
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

    watchdog(5, func, 0.1)# za 0.1 doplnit *args **kwargs

Or

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
            # if the action ends in specified time, timer is canceled
            timer.cancel()

    import time
    with time_limit(5, 'slee'):
        time.sleep(10)

## Profiling
    import cProfile
    print(cProfile.run(‘whatever statements you want to run’))

I would suggest putting your statements in a function, so that this call can be like

    print(cProfile.run(‘your_function(input)’))

# Whole sections
## Encoding JSON with Python

Python comes pre-equipped with a JSON encoder and decoder to make it very simple to play nice with JSON in your applications

The simplest way to encode JSON is with a dictionary. This basic dictionary holds random values of various datatypes.

data =  {
            a:  0,
            b:  9.6,
            c:  "Hello World",
            d:  {
                    a:  4
            }
}

We then use json.dumps() to convert the dictionary to a JSON object.

    import json
    json_data = json.dumps(data)
    print(json_data)  # {"c":  "Hello World",  "b":  9.6,  "d":  {"e":  [89,  90]},  "a":  0}

Notice how the keys are not sorted by default, you would have to add the sort_keys=True argument to json.dumps() like so.


json_data = json.dumps(data, sort_keys=True)

print(json_data)  # {"a":  0,  "b":  9.6,  "c":  "Hello World",  "d":  {"e":  [89,  90]}}

# Pypi export / create own library
Put on github, add licence, create release. In computer create setup.py

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

Next create setup.cfg

# Inside of setup.cfg
    [metadata]
    description-file = README.md

    [bdist_wheel]  # Dal pro wheels knihovnu
    universal = 1

    [metadata]
    license_file = LICENSE

Load folder in cmd

    python setup.py sdist

If you use wheel - better

    python setup.py sdist bdist_wheel

    twine upload dist/*

