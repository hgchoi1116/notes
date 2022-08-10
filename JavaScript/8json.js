// JSON Javascript Object Notation

// - simplest data interchange format
// - lightweight text-based structure
// - easy to read
// - key-value pairs
// - used for serialization and tramission of
//      data between the network and the network connection
// - independent programming language and platform

// serialize object to string (json)
// desseralize string (json) to object

// 1. Object to JSON
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple','banana']);
console.log(json);


const dog = {
    name: 'bark',
    color: 'gold',
    size: null,
    birthDate: new Date(),
    jump: () => {console.log(`${name} can jump!`)}
};

json = JSON.stringify(dog);
console.log(json); // symbol or functions are not included

json= JSON.stringify(dog,['name', 'color']);
console.log(json);

console.clear();

json= JSON.stringify(dog,(key, value) => {
    console.log( `key: ${key}, value: ${value}`);
    return key, value;
});

console.log(json);

// 2. JSON to Object
console.clear();
json = JSON.stringify(dog);
const obj = JSON.parse(json, (key,value) => {
    console.log( `key: ${key}, value: ${value}`);
    return key === 'birthDate' ? new Date(value) : value;
});
console.log(obj);
dog.jump();
// obj.jump(); // does not exist 

console.log(dog.birthDate.getDate());
console.log(obj.birthDate.getDate()); // error birthdat is string in json


// ref. https://tools.learningcontainer.com/
// json diff - compares and idenfies difference in two json file
// json beautifier - formats broken format 
// json parser - organize the result into objects
// json validator - verifies if there is no error