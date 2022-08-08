'use strict';
// Array

// 1. Declaration
const arr1 = new Array();
const arr2 = [1,2];

// 2. Index position
const fruits = ['🍎','🍌'];
console.log(fruits);
console.log(fruits.length);
console.log(fruits[0]); //apple
console.log(fruits[1]); //banana
console.log(fruits[2]); //undefined
console.log(fruits[fruits.length -1]); //last item

// 3. Looping
// print all fruits
// a. for
for (let i = 0; i < fruits.length; i++){
    console.log(fruits[i])
;}

// b. for of
for (let fruit of fruits){
    console.log(fruit);
}

// c. forEach - can receive three parameters (value, index, array)
fruits.forEach(function(fruit){
    console.log(fruit);
})
// another way to represent this
fruits.forEach((fruit) =>console.log(fruit));

// 4. Addition , deletion, copy
// push: add an item to the end
fruits.push('🍓','🍑');
console.log(fruits);

// pop: remove an item from the end
fruits.pop(); // peach removed
console.log(fruits);

//unshift: add an item to the beginning
fruits.unshift('🍋');
console.log(fruits);

// shift: remove an item from the beginning
fruits.shift();
console.log(fruits);

// NOTE!!! shift and unshift are much slower than push and pop!!

//splice: remove an item by index position
// splice(start: number, deleteCount?: number)
fruits.push('🍓','🍑','🍋');
console.log(fruits)
//fruits.splice(1); // defined only the starting point. everything is deleted from index 1
fruits.splice(1,1); // from the start position index 1, delete 1 item
console.log(fruits);
fruits.splice(1,1,'🍏','🍉'); // start position index 1, delete 1 item, then add the following items on starting position
console.log(fruits);


// combine two arrays
const fruits2 = ['🍐'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits);

// 5. Searching
// find the index

console.clear();

console.log(fruits);
console.log(fruits.indexOf('🍎')); // 0  first index
console.log(fruits.lastIndexOf('🍎')) // last index
console.log(fruits.indexOf('🥥')); // -1
console.log(fruits.includes('🍉')); //true



