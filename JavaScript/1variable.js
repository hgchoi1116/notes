// refer to MDN site -- developer.mozilla.org
// 1. Use strict
// added in ES 5
// use this for vanilla Javascript
'use strict';

// 2. let vs Constants
//let - mutable data type
//constant - favor immutable data type
// advantage - security, thread safety, reduce human msitake

//global variable - outside bracket, can be used in/out bracket
//block varaible - inside bracket, can be used only inside bracket

let globalName='Choi'; 
{
let firstName = 'Jason';
//block scope variable
console.log(firstName);
firstName = 'hello';
console.log(firstName);
console.log(globalName);
}
console.log(globalName);

//var (do not use this)
//var hoisting (move declaration from bottom to top)
//variable can be declared later and will still work
//var does not care about block scope groups

//3. Variable Types

//number - includes int, short, long, double, float, 
//do not need to declare "number" data type in javascript

//string - char, string
//using quotation
console.log('hi ' + globalName);
//Template literals using backtick `
console.log(`hi ${globalName}!`);

//boolean
// false: 0, null, undefined, NaN, ''
// true: any other value

//null - declared as nothing
//undefined - not declared

//symbol - unique identifiers for objects
const symbol1= Symbol('id');
const symbol2= Symbol('id');
console.log(symbol1===symbol2); //false
const gSymbol1= Symbol.for('id');
const gSymbol2= Symbol.for('id');
console.log(gSymbol1===gSymbol2); //true

//Dynamic Typing: dynamically typed language
let text = 'hello'; //text
text = 1;           //number
text='7'+5;         //75 string
text='8'/'2';       //4 number

//object - mutable data type
const jason = {name:'jason', age:28};
console.log(jason.age);
jason.age=2;
console.log(jason.age);
