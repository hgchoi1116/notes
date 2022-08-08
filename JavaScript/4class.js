// Class
// - template
// - declare once
// - no data in

// Object
// - instance of a class
// - created many times
// - data in

'use strict';

// OOP
// class: template
// object: instance of a class
// JS classes
// - introduced in ES6
// - syntactical sugar over prototype-based inheritance

// 1. class declaration
class person {
    //constructor
    constructor (name, age) {
    //fields
    this.name = name;
    this.age = age;
    }
    // methods
    speak(){
        console.log(`${this.name}: hello!`);
    }
}

const jason = new person('jason','28');
console.log(jason.name);
console.log(jason.age);
jason.speak();


// 2. Getter and Setter

class User{
    constructor(firstName, lastName, age){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }
    get age(){
        return this._age;
    }  
    set age(value){
        this._age=value < 0 ? 0 : value;
    }

}

const user1= new User('Steve','Job','-1');
console.log(user1.age);

// 3. Field (public, private)

class Experiment {
    publicField=2;
    #privateField = 0;
}
const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);

// 4. Static properties and methods

class Article {
    static publisher = 'Jason Choi';
    constructor(articleNumber){
        this.articleNumber = articleNumber;
    }

    static printPublisher(){
        console.log(Article.publisher);
    }
}

const article1=new Article(1);
const article2 = new Article(2);
console.log(Article.publisher);
Article.printPublisher();

// 5. Inheritance
// a way for one class to extend another class
class Shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }
    draw(){
        console.log(`drawing ${this.color} color of `);
    }

    getArea() {
        return this.width * this.height;
    }
}

class Rectangle extends Shape {}
class Triangle extends Shape{
    draw(){
        super.draw(); //run parent method
        console.log("🔺")
    }
    getArea() {
        return (this.width * this.height)/2;
    }
}
const rectangle = new Rectangle(20,20,'blue');
rectangle.draw();
console.log(rectangle.getArea());
const triangle = new Triangle (20,20,'red');
triangle.draw();
console.log(triangle.getArea());

// 6. Class checking: instanceOf
console.log(rectangle instanceof Rectangle);
console.log(triangle instanceof Rectangle);
