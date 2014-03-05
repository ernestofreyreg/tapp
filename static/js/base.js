
$(function() {

    $('#connect').click(function(){
        $.oauthpopup({
            path: '/tw/login',
            callback: function(){
                window.location.reload();
            }
        });
//        location.href = "/tw/login";
        return false;
    });


});