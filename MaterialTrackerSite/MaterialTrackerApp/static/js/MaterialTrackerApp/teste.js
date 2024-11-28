"use strict";
// Define a simple function that greets the user
function greetUser(name) {
    return `Hello, ${name}! Welcome to TypeScript in Django.`;
}
// Fetch an element from the DOM and update its content
document.addEventListener("DOMContentLoaded", () => {
    const greetElement = document.getElementById("greet");
    if (greetElement) {
        greetElement.innerText = greetUser("Django Developer");
    }
});
