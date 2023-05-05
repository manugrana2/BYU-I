/* Lesson 3 */

/* FUNCTIONS */
// Step 1: Using function declaration, define a function named add that takes two arguments, number1 and number2
function add(number1, number2){
    // Step 2: In the function, return the sum of the parameters number1 and number2
    return number1 + number2;

}

// Step 3: Step 3: Using function declaration, define another function named addNumbers that gets the values of two HTML form controls with IDs of addend1 and addend2. Pass them to the add function
function addNumbers(){
    number1 = parseFloat(document.getElementById("addend1").value)
    number2 = parseFloat(document.getElementById("addend2").value)
    result = add(number1, number2)
    // Step 4: Assign the return value to an HTML form element with an ID of sum
    document.getElementById("sum").value = result
    

}

// Step 5: Add a "click" event listener to the HTML button with an ID of addNumbers that calls the addNumbers function
document.getElementById("addNumbers").addEventListener("click", addNumbers)
// Step 6: Using function expressions, repeat Steps 1-5 with new functions named subtract and subtractNumbers and HTML form controls with IDs of minuend, subtrahend, difference and subtractNumbers

function subtract(number1, number2){
    return number1 - number2;

}
function subtractNumbers(){
    number1 = parseFloat(document.getElementById("minuend").value)
    number2 = parseFloat(document.getElementById("subtrahend").value)
    result = subtract(number1, number2)
    document.getElementById("difference").value = result
    

}
document.getElementById("subtractNumbers").addEventListener("click", subtractNumbers)



// Step 7: Using arrow functions, repeat Steps 1-5 with new functions named multiply and mulitplyNumbers and HTML form controls with IDs of factor1, factor2, product and multiplyNumbers
const multiply = (factor1, factor2) => factor1 * factor2;

const mulitplyNumbers = () => {
    number1 = parseFloat(document.getElementById("factor1").value)
    number2 = parseFloat(document.getElementById("factor2").value)
    result = multiply(number1, number2)
    document.getElementById("product").value = result

};

document.getElementById("multiplyNumbers").addEventListener("click", mulitplyNumbers)

// Step 8: Using any of the three function declaration types, repeat Steps 1-5 with new functions named divide and divideNumbers and HTML form controls with IDs of dividend, divisor, quotient and divideNumbers
const divide = (factor1, factor2) => factor1 / factor2;

const divideNumbers = () => {
    number1 = parseFloat(document.getElementById("dividend").value)
    number2 = parseFloat(document.getElementById("divisor").value)
    result = divide(number1, number2)
    document.getElementById("quotient").value = result

};

document.getElementById("divideNumbers").addEventListener("click", divideNumbers)
// Step 9: Test all of the mathematical functionality of the task3.html page.
// Testing add function
console.log("Operation 1 + 2, output:", add(1, 2), " | Expected output: 3");
console.log("Operation -1 + 4, output:", add(-1, 4), " | Expected output: 3");
console.log("Operation 0 + 0, output:", add(0, 0), " | Expected output: 0");

// Testing subtract function
console.log("Operation 5 - 3, output:", subtract(5, 3), " | Expected output: 2");
console.log("Operation -1 - 4, output:", subtract(-1, 4), " | Expected output: -5");
console.log("Operation 0 - 0, output:", subtract(0, 0), " | Expected output: 0");

// Testing multiply function
console.log("Operation 2 * 3, output:", multiply(2, 3), " | Expected output: 6");
console.log("Operation -1 * 4, output:", multiply(-1, 4), " | Expected output: -4");
console.log("Operation 0 * 5, output:", multiply(0, 5), " | Expected output: 0");

// Testing divide function
console.log("Operation 6 / 3, output:", divide(6, 3), " | Expected output: 2");
console.log("Operation -8 / 4, output:", divide(-8, 4), " | Expected output: -2");
console.log("Operation 0 / 5, output:", divide(0, 5), " | Expected output: 0");



/* BUILT-IN METHODS */

// Step 1: Declare and instantiate a variable of type Date to hold the current date

let currentDate = new Date()
// Step 2: Declare a variable to hold the current year
let currentYear;

// Step 3: Using the variable declared in Step 1, call the built-in getFullYear() method/function and assign it to the variable declared in Step 2
currentYear = currentDate.getFullYear()
// Step 4: Assign the current year variable to an HTML form element with an ID of year
document.getElementById("year").textContent = currentYear

/* ARRAY METHODS */

// Step 1: Declare and instantiate an array variable to hold the numbers 1 through 25
const toNumber = 25;
const numbersList = Array.from({length: toNumber}, (_, index) => 1 + index)
console.log(numbersList)
// Step 2: Assign the value of the array variable to the HTML element with an ID of "array"
document.getElementById("array").textContent = '['+numbersList+']';

// Step 3: Use the filter array method to find all of the odd numbers of the array variable and assign the result to the HTML element with an ID of "odds" ( hint: % (modulus operartor) )
let oddNumbers = numbersList.filter( number=> number % 2 ===1) 
document.getElementById("odds").textContent = oddNumbers
// Step 4: Use the filter array method to find all of the even numbers of the array variable and assign the result to the HTML element with an ID of "evens"
let evenNumbers = numbersList.filter( number => number % 2 ===0)
document.getElementById("evens").textContent = evenNumbers


// Step 5: Use the reduce array method to sum the array variable elements and assign the result to the HTML element with an ID of "sumOfArray"
let totalFromArr = numbersList.reduce(add)
document.getElementById("sumOfArray").textContent = totalFromArr

// Step 6: Use the map array method to multiple each element in the array variable by 2 and assign the result to the HTML element with an ID of "multiplied"
let mNumbers = numbersList.map(number => number * 2)
document.getElementById("multiplied").textContent = mNumbers

// Step 7: Use the map and reduce array methods to sum the array elements after multiplying each element by two.  Assign the result to the HTML element with an ID of "sumOfMultiplied"
let mSum = numbersList.map(number => number * 2).reduce(add)
document.getElementById("sumOfMultiplied").textContent = mSum
