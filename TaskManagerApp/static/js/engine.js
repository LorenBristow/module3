$(".important-indicator").click(function()
{
    $(this).find('input[type=radio]').prop("checked", "true");
})

$(".status-indicator").click(function()
{
    $(this).find('input[type=checkbox]').prop("checked", "true");
})
