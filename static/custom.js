
// Wrap your code in a function to ensure it runs after the DOM is fully loaded 
document.addEventListener('DOMContentLoaded', function () {
    console.log('DOMContentLoaded event fired'); // Debugging line
   

    function revealTitle() {
        const title = document.querySelector("#title")
        console.log('revealTitle function called'); // Debugging line
        console.log("i am")
        console.log(title)
        title.style.animation = 'none'; // Stop the jumbled animation
        title.textContent = 'DIGI DOC'; // Set the actual text
        title.style.opacity = 0; // Make it initially transparent
       
       // Apply a fade-in effect
        setTimeout(() => {
            title.style.transition = 'opacity 1s';
            title.style.opacity = 1;
        }, 10);
    }

    // Call the revealTitle function after a delay
    setTimeout(revealTitle, 3000); // Adjust the delay as needed
    // revealTitle()
});
