
$(function(){
    $('#btnToggle').click(efectoToggle); 
    $('#btnAnimate').click(efectoAnimate); 
    $('#btnStop').click(function(){
        $('#cuadro').stop();                 
    }); 
    $('#btnAnimateReturn').click(efectoAnimateReturn); 
}); 

function efectoAnimateReturn() {
    $('#cuadro').animate({
        left:'8px',
        opacity:'1',
        height: '100px',
        width:'100px'
    }, 1500);
}

function efectoToggle() {
    $('#pToggle').toggle(2500); 
}

function efectoAnimate() {
    $('#cuadro').animate({
        left:'500px',
        opacity:'0.5',
        height: '250px',
        width:'250px'
    }, 3000); 
}