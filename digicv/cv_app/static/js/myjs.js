$(document).ready(function () {
     console.log("Calling hello function");
     hello();
    });


function hello(){
  console.log(" Hello world ");
  $('#mycarousel').carousel('cycle')
  }

$("#sobutton").on('click',function(){
  console.log("Clicked");
})


function changeColor(event){
console.log("Event received" + event)
}