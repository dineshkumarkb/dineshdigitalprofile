$(document).ready(function () {
     console.log("Calling hello function");
     hello();
    });


function hello(){
  console.log(" Hello world ");
  $('#mycarousel').carousel('cycle')
  }
