/* Variables we need for the game */

var wolf_gb = '';
var wolf_price = 0;
var frequency = '';
var total = 0;
//var final_price = 0;

/* Listen for the button clicks*/
$('.wolf--price').click(function(event) {
  wolf_gb = this.getAttribute("data-gb");
  wolf_price = parseInt(this.getAttribute("data-price"));
  console.log('price ' + wolf_price);
  //$('#wolf_price').text(wolf_price);
});

$('.frequency').click(function(event) {
  frequency = this.getAttribute("data-freq");
  $('#frequency').text(frequency);
  console.log('freq1 ' + frequency);
  calculator();
  // wolf_price = 0;
  console.log('freq2 ' + wolf_price);

});

function calculator() {

  if (frequency == "per annum") {
    total = 12 * wolf_price;
  } else if (frequency == "per month") {
    total = wolf_price;
  }
  $('#wolf_price').text(total);

  console.log('calc ' + total);
}
//end of calculator
$(".wolf--price").click(function(){
  $(".wolf--price").removeClass("active");
  $(this).addClass("active");

});


$(".frequency").click(function(){
  $(".frequency").removeClass("active");
  $(this).addClass("active");


});
$(".btn").click(function(){
  $(".frequency").removeClass("active");
$("#wolf_price").text();
});
//frequency


$("#buy").click(function(){
//  $(".frequency").removeClass("active");
$("#wolf_price").text();
});
//prevent deletion of price to pay on screen when 'buy' is clicked.
