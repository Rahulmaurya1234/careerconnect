document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Hero animation
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        heroContent.style.opacity = '0';
        heroContent.style.transform = 'translateY(20px)';

        setTimeout(() => {
            heroContent.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            heroContent.style.opacity = '1';
            heroContent.style.transform = 'translateY(0)';
        }, 200);
    }

    // Handle job application submissions
    document.querySelectorAll('.apply-form').forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new FormData(form)
            })
            .then(response => response.json())
            .then(data => {
                if (data.redirect) {
                    window.location.href = data.url;
                } else if (data.success) {
                    alert(data.message);
                } else {
                    alert('An unexpected error occurred.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while submitting your application.');
            });
        });
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        const dropdown = document.querySelector('.user-profile-dropdown');
        const dropdownMenu = document.getElementById('profileDropdown');
        const trigger = document.querySelector('.profile-trigger');
        
        if (dropdown && dropdownMenu && trigger && !dropdown.contains(e.target)) {
            dropdownMenu.classList.remove('show');
            trigger.classList.remove('active');
        }
    });
});

// Profile dropdown toggle function
function toggleProfileDropdown() {
    const dropdownMenu = document.getElementById('profileDropdown');
    const trigger = document.querySelector('.profile-trigger');
    
    if (dropdownMenu && trigger) {
        dropdownMenu.classList.toggle('show');
        trigger.classList.toggle('active');
    }
}
