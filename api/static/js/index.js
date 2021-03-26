
const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo');

const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);

const highlightMenu = () => {
    const elem = document.querySelector('.highlight')
    const homeMenu = document.querySelector('#home-page')
    const aboutMenu = document.querySelector('#about-page')
    const teamMenu = document.querySelector('#team-page')
    let scrollPos = window.scrollY


if(window.innerWidth > 960 && scrollPos < 600) {
    homeMenu.classList.add('highlight')
    aboutMenu.classList.remove('highlight')
    return;
} else if (window.innerWidth > 960 && scrollPos < 1400){
    aboutMenu.classList.add('highlight')
    homeMenu.classList.remove('highlight')
    teamMenu.classList.remove('highlight')
    return;
} else if (window.innerWidth > 960 && scrollPos < 2345){
    teamMenu.classList.add('highlight')
    aboutMenu.classList.remove('highlight')
    return;
}

if ((elem && window.innerWidth <960 && scrollPos <600) || elem) {
        elem.classList.remove('highlight');
    }
};

window.addEventListener('scroll', highlightMenu );
window.addEventListener('click', highlightMenu );

/*-1-----------------------------------*/
        $(document).on('click','.member-1',function(){
            $('.detail-box-1').toggleClass('show-details-1')
            $('.detail-box-2').removeClass('show-details-2')
            $('.detail-box-3').removeClass('show-details-3')
            $('.detail-box-4').removeClass('show-details-4')
            $('.detail-box-5').removeClass('show-details-5')
            $('.detail-box-6').removeClass('show-details-6')
        });
    /*-2-----------------------------------*/
    $(document).on('click','.member-2',function(){
            $('.detail-box-2').toggleClass('show-details-2')
            $('.detail-box-1').removeClass('show-details-1')
            $('.detail-box-3').removeClass('show-details-3')
            $('.detail-box-4').removeClass('show-details-4')
            $('.detail-box-5').removeClass('show-details-5')
            $('.detail-box-6').removeClass('show-details-6')
        });
    /*-3-----------------------------------*/
    $(document).on('click','.member-3',function(){
            $('.detail-box-3').toggleClass('show-details-3')
            $('.detail-box-2').removeClass('show-details-2')
            $('.detail-box-1').removeClass('show-details-1')
            $('.detail-box-4').removeClass('show-details-4')
            $('.detail-box-5').removeClass('show-details-5')
            $('.detail-box-6').removeClass('show-details-6')
        });
    /*-4-----------------------------------*/
    $(document).on('click','.member-4',function(){
            $('.detail-box-4').toggleClass('show-details-4')
            $('.detail-box-2').removeClass('show-details-2')
            $('.detail-box-3').removeClass('show-details-3')
            $('.detail-box-1').removeClass('show-details-1')
            $('.detail-box-5').removeClass('show-details-5')
            $('.detail-box-6').removeClass('show-details-6')
        });
    /*-5-----------------------------------*/
    $(document).on('click','.member-5',function(){
            $('.detail-box-5').toggleClass('show-details-5')
            $('.detail-box-2').removeClass('show-details-2')
            $('.detail-box-3').removeClass('show-details-3')
            $('.detail-box-4').removeClass('show-details-4')
            $('.detail-box-1').removeClass('show-details-1')
            $('.detail-box-6').removeClass('show-details-6')
        });
    /*-6-----------------------------------*/
    $(document).on('click','.member-6',function(){
            $('.detail-box-6').toggleClass('show-details-6')
            $('.detail-box-2').removeClass('show-details-2')
            $('.detail-box-3').removeClass('show-details-3')
            $('.detail-box-4').removeClass('show-details-4')
            $('.detail-box-5').removeClass('show-details-5')
            $('.detail-box-1').removeClass('show-details-1')
        });
 
    /*-cancel------------------*/
    $(document).on('click','.cancel',function(){
            $('.detail-box-1').removeClass('show-details-1')
            $('.detail-box-2').removeClass('show-details-2')
            $('.detail-box-3').removeClass('show-details-3')
            $('.detail-box-4').removeClass('show-details-4')
            $('.detail-box-5').removeClass('show-details-5')
            $('.detail-box-6').removeClass('show-details-6')
        });
 