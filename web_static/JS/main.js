const navMenu = document.getElementById('navbar'),
    toggleMenu = document.getElementById('nav-toggle'),
    closeMenu = document.getElementById('nav-close')


/*---GSAP animation---*/
gsap.from('.logo, .nav__toggle', {opacity: 0, duration: 1, delay:2, y: 10})
gsap.from('.navbar', {opacity: 0, duration: 1, delay: 2.1, y: 30, stagger: 0.2,})