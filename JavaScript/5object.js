'use strict';
// Objects
// one of the JavaScript's data types
// a coolection of related data and/or functionality.
// Nearly all objects in JS are instances of Object
// object = {properties : values};

// 1. Literals and properties
//without using obejct
const name = 'Jason';
const age = 4;
print(name, age);
function print(name,age){
    console.log(name);
    console.log(age);
}
// using object
const jason = {name: 'jason', age:4};
function print2(person){
    console.log(person.name);
    console.log(person.age);
}
print2(jason);

//ways to make objects
const obj1 = {}; // 'object literal' syntax
const obj2 = new Object(); // 'object constructor' syntax

// JavaScript magic (dynamically typed language)
// can add properties later
jason.hasJob = true;

// can delete properties later
delete jason.hasJob;


// 2. Computed properties
// key should be always string type
console.log(jason.name);
console.log(jason['name']);

function printValue(obj, key){
    console.log(obj[key]);
}
printValue(jason, 'name');
printValue(jason, 'age');

// 3. Property value shorthand
const person1 = {name: 'bob', age:2};
const person2 = {name: 'steve', age: 3};
const person3 = {name: 'dave', age:4};
const person4 = makePerson('jason',30);
console.log(person4);
function makePerson(name,age){
    return{
        name,age
    };
}

//4. Constructor Function
const person5 = new Person('Jason', 28);
function Person(name, age){
    this.name = name;
    this.age = age;
}

// 5. in operator: property existence check (key in obj)
console.log('name' in jason); //true
console.log('random' in jason); //false
console.log(jason.random); //undefined

// 6. for..in vs for..of
// for (key in obj)
for (const key in jason) {
    console.log(key);
}


// for (value of iterable)
const array = [1,2,4,5];
for(let i = 0; i <array.length; i++){
    console.log(array[i]);
}

// easier way
for(const value of array) {
    console.log(value);
}
///////////////////////////////////////
console.clear();
///////////////////////////////////////

// 7. Fun cloning
// Object.assign(dest, [obj1, obj2, obj3...])
const user = {name: 'jason', age: '20'};
const user2 = user;
user2.name = 'coder';
console.log(user); 
//user name changes as well because user2 is a ref of user

//old way, copying manually
const user3 = {};
for (const key in user) {
    user3[key] = user[key];
}
console.log(user3);

//new way
const user4= Object.assign({}, user);
console.log(user4);
user4.name = 'jason';
console.log(user4);

// in assining multiple sources, latest source gets applied
