/* Lesson 2 */

/* VARIABLES */

// Step 1: declare and instantiate a variable to hold your name
let myName = "Jose Manuel Granados Collazos"

// Step 2: place the value of the name variable into the HTML file (hint: document.querySelector())
let nameHolder = document.querySelector("#name")
nameHolder.innerText = myName;

// Step 3: declare and instantiate a variable to hold the current year
let currentYear = new Date().getFullYear()


// Step 4: place the value of the current year variable into the HTML file
let yearHolder = document.querySelector("#year")
yearHolder.innerText = currentYear

// Step 5: declare and instantiate a variable to hold the name of your picture
let profilePhoto = "images/photo.jpg"

// Step 6: copy your image into the "images" folder

// Step 7: place the value of the picture variable into the HTML file (hint: document.querySelector().setAttribute())
document.querySelector(".photo").setAttribute("src", profilePhoto)



/* ARRAYS */

// Step 1: declare and instantiate an array variable to hold your favorite foods
let favoriteFoods = ["Rice with vegetables and chicken", "Red beans", "Fruits Salad", "Arepa with cheese", "Oatmeal with cinnamon", "Nestún"]

// Step 2: place the values of the favorite foods variable into the HTML file
let foodsList = document.createElement("ul");
foodsList.classList.add("all")

document.querySelector("#food").appendChild(foodsList)

favoriteFoods.map((food)=>{
    let item = document.createElement("li")
    item.textContent = food
    document.querySelector(".all").appendChild(item)
} )




// Step 3: declare and instantiate a variable to hold another favorite food
let addFood = "Pasta bolognese"

// Step 4: add the variable holding another favorite food to the favorite food array
favoriteFoods.push(addFood);

// Step 5: repeat Step 2

document.querySelector(".all").innerHTML = favoriteFoods.toString()
// Step 6: remove the first element in the favorite foods array
favoriteFoods.shift()


// Step 7: repeat Step 2
document.querySelector(".all").innerHTML = favoriteFoods.toString()


// Step 8: remove the last element in the favorite foods array
favoriteFoods.pop()

// Step 7: repeat Step 2
document.querySelector(".all").innerHTML = favoriteFoods.toString()



