# Js reference

This is also reference for TypeScript in own typing section

## TOC

<!-- TOC -->
* [Js reference](#js-reference)
  * [TOC](#toc)
  * [New](#new)
  * [Syntax](#syntax)
    * [Misc](#misc)
  * [Conditions](#conditions)
    * [HTML interaction](#html-interaction)
<!-- TOC -->


## Conditions
```js
if (1 < 2) {
    alert("jo")
}

switch (key) {
    case value:
        
        break;

    default:
        break;
}
```

## Classes

    class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
      // Getter
      get area() {
        return this.calcArea();
      }
      // Method
      calcArea() {
        return this.height * this.width;
      }
      *getSides() {
        yield this.height;
        yield this.width;
        yield this.height;
        yield this.width;
      }
    }

    const square = new Rectangle(10, 10);

### Constructors

    class Polygon {
      constructor() {
        this.name = 'Polygon';
      }
    }

    const poly1 = new Polygon();

    console.log(poly1.name);  // "Polygon"

### Static

    class Point {
      constructor(x, y) {
        this.x = x;
        this.y = y;
      }

      static displayName = "Point";
      static distance(a, b) {
        const dx = a.x - b.x;
        const dy = a.y - b.y;

        return Math.hypot(dx, dy);
      }
    }

    const p1 = new Point(5, 5);
    p1.displayName; // undefined

    console.log(Point.displayName); // "Point"

### Private

    class ClassWithPrivate {
      #privateField;
      #privateFieldWithInitializer = 42;

      #privateMethod() {
        // …
      }

### Inheritance

    class Animal {
      constructor(name) {
        this.name = name;
      }

      speak() {
        console.log(`${this.name} makes a noise.`);
      }
    }

    class Dog extends Animal {
      constructor(name) {
        super(name); // call the super class constructor and pass in the name parameter
      }

      speak() {
        console.log(`${this.name} barks.`);
      }
    }

    const d = new Dog("Mitzie");


### Getters, setters

    const obj = {
      log: ["example", "test"],
      get latest() {
        if (this.log.length === 0) return undefined;
        return this.log[this.log.length - 1];
      },
      set msg(x) {
        this.#msg = `hello ${x}`;
      }
    };
    console.log(obj.latest); // "test"


## Generator

    function* generator(i) {
      yield i;
      yield i + 10;
    }

    const gen = generator(10);

    console.log(gen.next().value);  // 10
    console.log(gen.next().value);  // 20
    console.log(gen.next().value);  // undefined

## Array destructuring

    const names = ['Luke', 'Eva', 'Phil']; 
    const [first] = names;  

## Ternary operator

    var isadult = (age < 18) ? 'tooyoung': 'old enough';

    var exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? '/production-sub-path/'
        : '/'
    }

## Optional Chaining

```js
// When foo is defined, foo.bar.baz() will be computed; but when foo is null or undefined, stop what we’re doing and just return undefined
let x = foo?.bar.baz();

// If object with param not available, use default value

transfersDataSource?.numberOfItems || 0
```

## Types


Return basic type of variable (not custom Classes, just object or literals)
    
    typeof("str")  // string

Return class name of object

    myObj.constructor.name

### Typescript

Type annotated version transpiled to js before run.

TODO

### HTML interaction
```html

<!--Create new elements and populate it-->
<div id="demo">some content</div>

<script>
    // Creating a new element
    var p = document.createElement("p");
    var node = document.createTextNode("Some new text");

    // Adding the text to the paragraph
    p.appendChild(node);

    // Getting the element 
    var div = document.getElementById("demo");

    // Adding the paragraph to the div
    div.appendChild(p);

    // Changing image src
    document.getElementById("qr").src = "/images/new"

    // Remove classes from all elements
    function make_button_visible() {

        var elems = document.getElementsByClassName('nonactive');

        while (elems.length > 0) {
            elems[0].classList.remove('nonactive');
        }
    }
</script>
```
