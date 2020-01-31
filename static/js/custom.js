function make_footer_bottom() {
    if ($('body').height() < (window.innerHeight - $('footer').height())){
        $('footer').addClass('navbar-fixed-bottom');
        $('body').css('margin-bottom', $('footer').height());
    }
}

$(function () {
    make_footer_bottom();
    $(window).resize(function () {
        make_footer_bottom();
    })
});