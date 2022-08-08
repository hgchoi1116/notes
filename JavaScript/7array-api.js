// Make a string out of an array
// - join
{
    const fruits = ['apple', 'banana', 'orange'];
    const answer = fruits.join(); //specify separator in ()
    console.log(answer);
}

// Make an array into an array
// - split
{
    const fruits = 'apple,kiwi,banana,stawberry';
    const answer = fruits.split(',');
    console.log(answer);

    const answer2 = fruits.split(',',3); //array limit size 3
    console.log(answer2); 
}

// Make this array look like this: [5,4,3,2,1]
{
    const array=[1,2,3,4,5];
    const answer = array.reverse();
    console.log(answer);
}

// Make new array without the first two elements
{
    const array = [1,2,3,4,5];
    const answer = array.splice(0,2);
    console.log(answer); // 1,2
    console.log(array); //3,4,5
    //not a new array
    // use slice command

    const array2 = [1,2,3,4,5];
    const correctAnswer = array2.slice(2,5);
    console.log(correctAnswer); // 3,4,5
}

class Student {
    constructor(name,age, enrolled,score) {
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
}
const students = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88),
];

// find a student with the score 90
{
    const result= students.find(function(student){
        return student.score === 90;
    })
    console.log(result);
    // or

    const result2 = students.find((student) => student.score ===90);
    console.log(result2);
}

// make an array of enrolled students
{
    const result = students.filter((student) => student.enrolled === true);
    console.log(result);
}

// make an array containing only the students' scores
// result should be: [45,80,90,66,88]
{
    const result = students.map((student)=> student.score);
    console.log(result);
}

// check if there is a student with the score lower than 50
// return true
{
    const result = students.some((student) => student.score < 50);
    console.log(result);
}

{
    // every - returns true if everyone has lower than 50 
    const result = !students.every((student) => student.score < 50);
    console.log(result); // if any student is not lower than 50, return true
}

console.clear();
// compute students' avg score
{
    const result = students.reduce((prev, curr) => prev + curr.score, 0);
    // starting at 0, add prev (0) + student's score until the end of the arry
    console.log(result/students.length);
}

// make a string containing all the scores
// result should be: '45, 80, 90, 66, 77'
{
    const result = students.map((student) => student.score).join();
    console.log(result);
}

// sort in ascending order
// result should be: '45, 66, 80, 88, 90;
{
    const result = students.map((student)=>student.score)
    .sort((a,b) => a-b) // desending => b-a
    .join();
    console.log(result)
}