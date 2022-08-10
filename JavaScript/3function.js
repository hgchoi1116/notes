// Function
// - fundamental building block in the program
// - subprogram can be used multiple times
// - perform a task or calculates a value

//1. function delaration
// function aname (param1, param2) { body... return;}
// one function === one thing
// naming: doSomething, command, verb
// e.g. createCardAndPoint->> createCard, createPoint
// function is object in jS

function printHello() {
    console.log('hello');
}
printHello();

function log(message){
    console.log(message);
}

log('hello@');
log(1234)

// 2. Parameters
// premitive parater: passed by value
// object parameters: passed by reference

function changeName(obj){
    obj.name = 'coder';
}

const jason = {name:'jason'};
changeName(jason);
console.log(jason);

// 3. Default parameters (added in ES6)
// set default parameter in the parameter
function showMessage(message, from = 'unknown'){ 
    console.log(`${message} by ${from}`);
}
showMessage('Hello!');

// 4. Rest parameters (added in ES6)
// 
function printAll(...args) {
    for (let i = 0; i<args.length; i++){
        console.log(args[i]);
    }
    for (const arg of args){
        console.log(arg);
    }
    args.forEach((arg)=>console.log(arg));
}

printAll('Jason','Choi','JavaScript');


// 5. Local Scope
// local can use global, but global cannot see local
let globalMessage = 'global'; //global variable
function printMessage() {
    let message = 'hello';
    console.log(message); // local variable
    console.log(globalMessage);
}
printMessage();

// 6. return a value
function sum(a,b){
    return a+b;
}
const result = sum(1,2); //3
console.log(`sum: ${sum(1,2)}`);

//7. early return, early exit

//bad example
function upgradeUser(user){
    if (user.point > 10) {
        // long upgrade logic...
    }
}

//good example
function upgradeUser(user){
    if (user.point <=10) {
        return;
    }
    //long upgrade logic
}

// first class- function
// functions are treated like any other variable
// can be assigned as a value to variable
// can be passed as an argument to other functions
// can be returned by another function

// 1. Function expression
// a function declaration can be called earlier than it is defined. (hoisted)
// a function expression is created when the execution reaches it.

const print = function () { // anonymous function
    console.log('print');
}

function functionName() { // named function
    console.log('print');
}

// 2. callback function using function expression

function randomQuiz(answer, printYes, printNo){
    if (answer === 'love you'){
        printYes();
    } else {
        printNo();
    }
}

const printYes = function () {
    console.log('yes!');
}
const printNo = function print() {
    console.log('no!');
}

randomQuiz('wrong',printYes,printNo);
randomQuiz('love you',printYes,printNo);

// 3. arrow function
// always anonymous
const simplePrint = function () {
    console.log('simplePrint!');
}
simplePrint();
const simplePrint2 = () => console.log('simpleePrint!');
const add = (a,b) => a+b;
simplePrint2();
console.log(add(3,5));

// 4. IIFE: Immediately Invoked Function Expression
// paranthesis the function and empty parameter at the end calls the function itself
(function hello() {
    console.log('IIFE');
})();

// QUIZ
function calculate (command, a,b){
    switch (command) {
        case 'add':
            return (a+b);
            break;
        case 'subtract':
            return(a-b);
            break;
        case 'divide':
            return (a/b);
            break;
        case 'multiply':
            return(a*b);
            break;
        case 'remainder':
            return(a%b);
            break;
        default:
            return ('invalid command');
            break;
    }
}
