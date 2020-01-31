$(document).ready(function () {
    function renew_collapse() {
        var form_grps = $('.form-group');
            $(form_grps).each(function () {
                if ($($(this)[0].lastElementChild).hasClass('multiple-checkbox')){
                    $($(this)['context'].children[0]).addClass('dropping');
                    if($($(this)['context'].children[1]).find('input:checkbox:checked').length == 0){
                        $($(this)['context'].children[1]).hide();
                    }
                }
            });
        }

    function collapse_form(){
        renew_collapse();
        $('.dropping').click(function () {
            if($($($(this)[0].parentNode)['context'].children[1]).is(':hidden')){
                $($($(this)[0].parentNode)['context'].children[1]).slideDown();
            }else{
                $($($(this)[0].parentNode)['context'].children[1]).slideUp();
                $($($(this)[0].parentNode)['context'].children[1])
            }
        })
    }

    function reset() {
        var reset_btn = $('#reset');
        reset_btn.click(function () {
             $('input:checkbox:checked').each(function () {
                 $(this).removeAttr('checked');
                 renew_collapse();
             });
        })
    }
    collapse_form();
    reset();
});