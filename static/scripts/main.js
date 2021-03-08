function titleCase(str) {
    str = str.toLowerCase().split(' ');
    for (var i = 0; i < str.length; i++) {
      str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
    }
    return str.join(' ');
  }

$(document).ready(function(){
    function change_img(){
        $("#waifu #woman").attr("src",$("#imageURL").val()) 
    }
    $("#imageURL").change(change_img)
    $(".vsliders input").change(function(){
        console.log($(this).parent().id)
        const ranks = "FEDCBA"
        $(this).parent().find("label").html( titleCase($(this).parent().attr('id'))+": ("+ranks[$(this).val()]+")");
    });
    change_img()
});