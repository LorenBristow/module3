/* Variables we need for the game */

var chat_gb = '';
var chat_min = '';
var chatgb_price = 0;
var chatmin_price = 0;
var frequency = '';
var subtotal = 0;
var total = 0;

//var final_price = 0;

/* Listen for the button clicks*/
$('.chatgb--price').click(function(event) {
  chat_gb = this.getAttribute("data-gb");
  chatgb_price = parseInt(this.getAttribute("data-price"));
  console.log('price ' + chatgb_price);
});

$('.chatmin--price').click(function(event) {
  chat_min = this.getAttribute("data-min");
  chatmin_price = parseInt(this.getAttribute("data-price"));
  console.log('price ' + chatmin_price);
  addup();
    console.log('calc ' + subtotal);
});

function addup() {
subtotal = chatgb_price+chatmin_price;
}

$('.frequency').click(function(event) {
  frequency = this.getAttribute("data-freq");
  $('#frequency').text(frequency);
  console.log('freq1 ' + frequency);
  calculator();
  console.log('freq2 ' + total);
});

function calculator() {

  if (frequency == "per annum") {
    total = 12 * subtotal;
  } else if (frequency == "per month") {
    total = subtotal;
  }
  $('#chat_price').text(total);

  console.log('calc ' + total);
}

//
$(".chatgb--price").click(function(){
  $(".chatgb--price").removeClass("active");
  $(this).addClass("active");

});

$(".chatmin--price").click(function(){
  $(".chatmin--price").removeClass("active");
  $(this).addClass("active");

});

$(".chatgb--price").click(function(){
  $(".chatmin--price").removeClass("active");
$("#chat_price").text("0");});

$(".frequency").click(function(){
  $(".frequency").removeClass("active");
  $(this).addClass("active");
});

$(".btn").click(function(){
  $(".frequency").removeClass("active");
$("#chat_price").text("0");
});

//frequency



$("#buy").click(function(){
//  $(".frequency").removeClass("active");
$("#chat_price").text(total);
});
//prevent deletion of price to pay on screen when 'buy' is clicked.
