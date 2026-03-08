var number = 5; // in-line comment

/* this is a multi-line comment
so you can write multiple */

number = 9;

/* Data Types:
undefined, null, boolean, string, symbol, number, and object
*/

var myName = "Jessica" // var is variable
myName = 8 // in here, var can be changed
let ourName = "freeCodeCamp" // let will only be used within the scope of where you declare that
const pi = 3.14 // variable that can never change

var a; // assign a variable, end a line with ;
var b = 2; // declaring, 2 is being assign to b
console.log(a)

a = 7; // assign 7 to a
b = a;

console.log // allows you to see things in the console (terminal?)
console.log(a);

// initialize these three variables
var c = 5;
var d = 6;
var e = "i am a";

// do not change below this line
a = a + 1;
b = b + 5;
c = c + " string!";

// javascript is case-sensitive StUdLyCapVaR !== STUDLYCAPVAR
// declarations
var StUdLyCapVaR;
var properCamelCase;
var TitleCaseOver;

// assignment
// this wont assign correct, it'll return a "not defined"
STUDLYCAPVAR = 10;
PRoperCAmelCAse = "a string";
tITLEcASEoVER = 9000;

let x = 10;
let y = 3;

console.log(x + y); // addition
console.log(x - y); // subtraction
console.log(x * y); // multiplication
console.log(x / y); // division
console.log(x % y); // remainder

let firstName = "jessica";
let greeting = "hello " + firstName;

console.log(greeting);

let age = 25;
console.log("i am " + age + " years old");

console.log(`i am ${age} years old`); // backtick syntax is modern javascript

console.log(5 > 3);     // true
console.log(5 < 3);     // false
console.log(5 == "5");  // true (loose comparison)
console.log(5 === "5"); // false (strict comparison)


// conditionals
let score = 80;

if (score > 70) {
    console.log("pass");
} else {
    console.log("fail");
}

// function
function greet(name) {
    return "hello " + name;
}

console.log(greet("jessica"));