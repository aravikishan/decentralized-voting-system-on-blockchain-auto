// Navigation Interactions
const navLinks = document.querySelectorAll('nav ul li a');
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

// Smooth Scrolling
const smoothScroll = (target, duration) => {
    const targetPosition = document.querySelector(target).offsetTop;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }

    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
};

// Form Validation
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', function(event) {
        const inputs = form.querySelectorAll('input[required]');
        let valid = true;
        inputs.forEach(input => {
            if (!input.value) {
                valid = false;
                input.classList.add('is-invalid');
            } else {
                input.classList.remove('is-invalid');
            }
        });
        if (!valid) {
            event.preventDefault();
            alert('Please fill out all required fields.');
        }
    });
});

// Dynamic Content Loading
async function loadContent(url, elementId) {
    const response = await fetch(url);
    const data = await response.json();
    const element = document.getElementById(elementId);
    element.innerHTML = JSON.stringify(data, null, 2);
}

// Example usage
// loadContent('/api/elections', 'electionList');