    // Wrap your code in a function to ensure it runs after the DOM is fully loaded 
    document.addEventListener('DOMContentLoaded', function () {
        console.log('DOMContentLoaded event fired'); // Debugging line

        function revealTitle() {
            const title = document.querySelector("#title_name");
            console.log('revealTitle function called'); // Debugging line

            // Set the actual text
            title.textContent = 'DIGI DOC';

            // Make it initially transparent
            title.style.opacity = 0;

            // Apply a fade-in effect
            setTimeout(() => {
                title.style.transition = 'opacity 1s'; // Set the transition
                title.style.opacity = 1; // Make it fully visible
            }, 10);
        }
        // Call the revealTitle function after a delay (adjust the delay as needed)
        setTimeout(revealTitle, 3000);
    });