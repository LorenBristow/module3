/*var total=0;
var simnr=0;
var gbprice=0;
var frequency="";

$(".sim1").hide();
$(".sim2").hide();
$(".sim3").hide();
$(".sim4").hide();
$(".sim5").hide();
$(".frq").hide();

$(".sim").click(function(event) {
simnr = parseInt(this.getAttribute("data-simnr"));
  console.log("move: " + simnr);
shouldDisplaySimOptionBtn();
$(".sim").hide();
});



$(".sim1").click(function(event) {
gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".sim1").hide();
  $(".frq").show();
});
$(".sim2").click(function(event) {
gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".sim2").hide();
  $(".frq").show();
});
$(".sim3").click(function(event) {
gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".sim3").hide();
  $(".frq").show();
});
$(".sim4").click(function(event) {
gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".sim4").hide();
  $(".frq").show();
});
$(".sim5").click(function(event) {
gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".sim5").hide();
  $(".frq").show();
});




function shouldDisplaySimOptionBtn(){
  if(simnr=="1"){
    $(".sim1").show();}
  else if (simnr=="2"){
    $(".sim2").show();
  }
  else if (simnr=="3"){
    $(".sim3").show();
  }
  else if (simnr=="4"){
    $(".sim4").show();
  }
  else if (simnr=="5"){
    $(".sim5").show();
  }

}


$(".frq").click(function(event) {
  frequency = this.getAttribute("data-frq");
  console.log("move: "+ frequency);
  calculator();
  $(".frq").hide();
});


function calculator( ) {
 if (frequency=="annually") {
  total = gbprice * 12;
  }
else if (frequency=="monthly") {
    total = gbprice + 0;
  }
  $("#you-pay").text(total);
}*/

var total = 0;
var simnr = 0;
var gbprice = 0;
var frequency = "";

$(".sim1").hide();
$(".sim2").hide();
$(".sim3").hide();
$(".sim4").hide();
$(".sim5").hide();
$(".frq").hide();

$(".sim").click(function(event) {
  simnr = parseInt(this.getAttribute("data-simnr"));
  console.log("move: " + simnr);
  shouldDisplaySimOptionBtn();
});



$(".sim1").click(function(event) {
  gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".frq").show();
});

$(".sim2").click(function(event) {
  gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".frq").show();
});

$(".sim3").click(function(event) {
  gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".frq").show();
});
$(".sim4").click(function(event) {
  gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".frq").show();
});
$(".sim5").click(function(event) {
  gbprice = parseInt(this.getAttribute("data-price"));
  console.log("move: " + gbprice);
  $(".frq").show();
});




function shouldDisplaySimOptionBtn() {
  if (simnr == "1") {
    $(".sim1").show();

    $(".sim2").hide();
    $(".sim3").hide();
    $(".sim4").hide();
    $(".sim5").hide();
  } else if (simnr == "2") {
    $(".sim2").show();
    $(".sim1").hide();

    $(".sim3").hide();
    $(".sim4").hide();
    $(".sim5").hide();
  } else if (simnr == "3") {
    $(".sim3").show();
    $(".sim1").hide();
    $(".sim2").hide();

    $(".sim4").hide();
    $(".sim5").hide();
  } else if (simnr == "4") {
    $(".sim4").show();
    $(".sim1").hide();
    $(".sim2").hide();
    $(".sim3").hide();

    $(".sim5").hide();
  } else if (simnr == "5") {
    $(".sim5").show();
    $(".sim1").hide();
    $(".sim2").hide();
    $(".sim3").hide();
    $(".sim4").hide();

  }

}


$(".frq").click(function(event) {
  frequency = this.getAttribute("data-frq");
  $('#frequency').text(frequency);
  console.log("move: " + frequency);
  calculator();

});


function calculator() {
  if (frequency == "per annum") {
    total = gbprice * 12;
  } else if (frequency == "per month") {
    total = gbprice + 0;
  }
  $("#you-pay").text(total);
}
//end of calculator
$(".sim").click(function(){
  $(".sim").removeClass("active");
  $(this).addClass("active");

});
$(".sim1").click(function(){
  $(".sim1").removeClass("active");
  $(this).addClass("active");
  $(".sim").click(function(){
    $(".sim1").removeClass("active");
  $("#you-pay").text();
  });

});
$(".sim2").click(function(){
  $(".sim2").removeClass("active");
  $(this).addClass("active");

});
$(".sim").click(function(){
  $(".sim2").removeClass("active");
$("#you-pay").text();});

$(".sim3").click(function(){
  $(".sim3").removeClass("active");
  $(this).addClass("active");

});
$(".sim").click(function(){
  $(".sim3").removeClass("active");
$("#you-pay").text();});

$(".sim4").click(function(){
  $(".sim4").removeClass("active");
  $(this).addClass("active");

});
$(".sim").click(function(){
  $(".sim4").removeClass("active");
$("#you-pay").text();});

$(".sim5").click(function(){
  $(".sim5").removeClass("active");
  $(this).addClass("active");


});
$(".sim").click(function(){
  $(".sim5").removeClass("active");
$("#you-pay").text();});

$(".frq").click(function(){
  $(".frq").removeClass("active");
  $(this).addClass("active");
});

$(".btn").click(function(){
$(".frq").removeClass("active");
$("#you-pay").text();
});
//frequency



$("#buy").click(function(){
//  $(".frq").removeClass("active");
$("#you-pay").text(total);
});
//prevent deletion of price to pay on screen when 'buy' is clicked.
