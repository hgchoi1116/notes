// 1. string concatenation
console.log('my' + ' cat');
console.log('1'+2);

console.log(`string literals:   
string literal
1 + 2 =${1+2}`);

//2. Numeric operators
console.log(1+1);
console.log(2**4); //exponent

//3. Increment and decrement operator
let counter=2;
const preIncrement = ++counter;
//counter = counter +1;
// preIncrement = counter;
console.log(`preIncrement: ${preIncrement}, counter:${counter}`);

const postIncrement = counter++;
// postIncrement = counter;
// counter = counter +1;
console.log(`preIncrement: ${postIncrement}, counter:${counter}`);


// 4. Assignment operators
let x= 3;
let y= 6;
x +=y; // -= *= /=

//5. Comparison operators
console.log(10<6); //< <= > >= returns true or false

//6. logical operators: ||(or), &&(and), !(not)
// OR if true is located on the first variable, 
// rest of the variables does not compute
// functions will preferrable to last of the comparison

// AND if first variable is true, does not care about rest

//7. Equality
const stringFive = '5';
const numberFive  = 5;
// == loose equality, with type conversion
console.log(stringFive == numberFive); //true
console.log(stringFive != numberFive); //false

// === strict equality, no type conversion (preferred)
console.log(stringFive === numberFive); // false
console.log(stringFive !== numberFive); // true


// object equality 
const jason1={name: 'jason'};
const jason2={name: 'jason'};
const jason3=jason1;
console.log(jason1==jason2); //false
console.log(jason1===jason2);//false same contect but different refernece 
console.log(jason1===jason3);//true

//8. Conditional operator: if
//if, else if, else
const name = 'jason';
if (name==='jason')
{
    console.log('welcome, Jason');
}
else if (name ==='choi')
{
    console.log('You are Choi!');
}
else{
    console.log('I do not know you');
}

// 9. Ternary operator: ? only for simple true or false scenario
// condition ? value1 : value2;
console.log(name === 'jason' ? 'yes' : 'no');
//execute left if true / execure right if false

// 10. Switch statement
// use for multiple if check
// use for enum-like value check
// use for multiple type checks in TS
const browser = 'IE';
switch (browser) {
    case 'IE':
        console.log('no!');
        break;
    case 'Chrome':
    case 'Firefox':
        console.log('good!');
        break;
    default:
        console.log('what browser?');
        break;
}

//11. Loops
// while loop, while the condition is true
let i =3;
while (i>0) {
    console.log(`while: ${i}`);
    i--;
}
// do while loop, body code is executed first,
// then check the condition
do{
    console.log(`do while: ${i}`);
    i--;
}while (i>0);

//for loop for(begin; condition; increment)
for (i=3; i>0; i--) {
    console.log(`for: ${i}`);
}

//nested loops
for (let i =0; i<10; i++){
    for (let j=0;j<10;j++){
        console.log(`i: ${i}, j: ${j}`);
    }
}

//break, continue
for (let i=0; i<=10; i++){ //print only even numbers
    if (i % 2 == 1)
    {
        continue; //continues to next loop
    }
    else{
        console.log(`i: ${i}`);
    }
}

for (let i=0; i<=10; i++){
    if (i ===8){
        break;
    }
    console.log(`i: ${i} break`);
}