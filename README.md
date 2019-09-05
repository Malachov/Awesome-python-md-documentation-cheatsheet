# Awesome-python-md-documentation-cheatsheet
Cheatsheet of all stuff that i ever needed in python. It's written in markdown so it's possible to open it in IDE (use right half...))





## Numba
    from numba import njit

    ** První možnost - na všechny funkce**
    @njit()
    def func():  # atd...

## Zobrazení všech obrázků ve složce
import os

from IPython.display import display, Image

names = [f for f in os.listdir('../images/ml_demonstrations/') if f.endswith('.png')]

for name in names[:5]:

 display(Image('../images/ml_demonstrations/' + name, width=100))
