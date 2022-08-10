'use strict';

// JavaScript is synchronous.
// Execute the code block by order after hoisting.
// hoisting: var, function delaration first

console.log('1');
setTimeout(()=>console.log('2'),1000);//1000ms = 1 sec
console.log('3');

// output 1,3,2 (2 appears after one sec) - ASYNC

// Synchronous callback
function printImmediately(print) {
    print();
}
printImmediately(()=>console.log('hello'));

// Asynchronous callback
function printWithDelay(print, timeout) {
    setTimeout(print, timeout);
}
printWithDelay(()=> console.log('async callback'),2000);

printWithDelay(function(){
    console.log('function',2000);
});

// CALLBACK HELL Example

// hard to read and understand quickly
class UserStorage {
    loginUser(id, password, onSuccess, onError){
        setTimeout(() => {
            if (
                (id ==='ellie' && password === 'dream') ||
            (id === 'coder' && password === 'academy')
            ){
                onSuccess(id);
            } else{
                onError(new Error('not found'));
            }
        },2000);
    }

    getRoles(user, onSuccess, onError) {
        setTimeout(()=>{
            if (user === 'ellie'){
                onSuccess({ name: 'ellie', role: 'admin'});
            } else {
                onError(new Error('no access'));
            }
        },1000);
    }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
    id, 
    password, 
    user => {
    userStorage.getRoles(
        user,
        userWithRole => {
            alert(`Hello ${userWithRole.name}, you have a ${userWithRole.role} role`);
        },
        error => {
            console.log(error);

        }
        );
    },
     error => {
        console.log(error);
    });