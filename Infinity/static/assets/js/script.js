/*--Inspect elements-*/
// document.addEventListener('contextmenu',function(event){
//   alert("Design and Developed by Aptsol Global Tech Pvt Ltd");
//   event.preventDefault();
// })

/*--Navbar starts-*/
window.addEventListener('scroll',function (){
    let navbar =this.document.querySelector('.navbar');
    if(this.window.scrollY > 140){
      navbar.classList.add('scrolled');
    }
    else{
      navbar.classList.remove('scrolled');
    }
  })
  /*--Navbar ends-*/
  $('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})