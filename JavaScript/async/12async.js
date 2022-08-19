// async & await
// clear style of using promise

// 1.async
async function fetchUser() {
        // do network request in 10 secs...
        return 'jason';
}

const user = fetchUser();
console.log(user);

// 2. await
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function getApple() {
    await delay(2000);
    return 'apple';
}

// easy way
async function getBanana() {
    await delay(1000);
    return 'banana';
}

// long way
function getBanana2(){
    return delay(1000)
    .then(()=> 'banana');
}

// good way 
async function pickFruits(){
    const applePromise = getApple(); // both loads at the same time
    const bananaPromise = getBanana(); // instead of one after another

    const apple =await applePromise;
    const banana = await bananaPromise;
    return `good! ${apple} + ${banana}`;
}

// callback hell
function pickFruits2() {
    return getApple()
    .then(apple => {
        return getBanana()
        .then(banana=> `${apple} + ${banana}`);
    });
}


pickFruits().then(console.log);
pickFruits2().then(console.log);


// 3. useful Promise APIs
function pickAllFruits() {
    return Promise.all([getApple(), getBanana()])
    .then(fruits => fruits.join(' + '));
}
pickAllFruits().then(console.log);

function pickOnlyOne(){
    return Promise.race([getApple(), getBanana()]);
    // pick the first item that completes loading first
}

pickOnlyOne().then(console.log);