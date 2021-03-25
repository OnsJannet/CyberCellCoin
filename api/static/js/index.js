const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo');

const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);
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
 