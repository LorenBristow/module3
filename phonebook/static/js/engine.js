$('#category-search-form').hide();
$('#name-search-form').hide();
$('#person_search').hide();
$('#business_search').hide();

$('.do_not_hide').show();

$("#person_button").click(function(event) {
  $("#person_search").show();
  $("#business_search").hide();
  $(".results").hide();
});

$("#business_button").click(function(event) {
  $("#business_search").show();
  $("#person_search").hide();
  $(".results").hide();
});


$("#name_button").click(function(event) {
  $("#name-search-form").show();
  $("#category-search-form").hide();
  $(".results").hide();
});

$("#category_button").click(function(event) {
  $("#category-search-form").show();
  $("#name-search-form").hide();
  $(".results").hide();
});

function myFunction() {
  var elmnt = document.getElementById("person_search");
  elmnt.scrollIntoView();
}
function myFunction() {
  var elmnt = document.getElementById("business_search");
  elmnt.scrollIntoView();
}
