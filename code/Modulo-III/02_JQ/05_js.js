
$(function(){
    $('#btnHideShow').click(efectoHideShow);
    $('#btnFadeInOut').click(efectoFadeInOut);
    $('#btnSlideDownUp').click(efectoSlideDownUp);
});

function efectoHideShow() {
    if ($('#pHideShow').is(":visible")){
        $('#pHideShow').hide(1500);
        $('#btnHideShow').text('Show');
    }else {
        $('#pHideShow').show("fast");
        $('#btnHideShow').text('Hide');
    }
}

function efectoFadeInOut() {
    if ($('#divFadeInOut').is(":visible")) {
        $('#divFadeInOut').fadeOut(2000);    
        $('#btnFadeInOut').text('Fade in');
    }else {
        $('#divFadeInOut').fadeIn(2000);
        $('#btnFadeInOut').text('Fade Out');
    }
}

function efectoSlideDownUp() {
    if ($('#divSlideDownUp').is(":visible")) {
        $('#divSlideDownUp').slideUp(2000);    
        $('#btnSlideDownUp').text('slide Up');
    }else {
        $('#divSlideDownUp').slideDown(2000);
        $('#btnSlideDownUp').text('slide Down');
    }
}