$('.vacancy .add_favorites').click(function(){
    var button = $(this);
    var vacancy_to_favour = $(this).data().vacancy;
    $.get('/api/favorite?vac='+vacancy_to_favour, null, favotite_check);
    function favotite_check(result) {
        if (result == 1){
            $(button).find('span').removeClass('glyphicon-star-empty').addClass('glyphicon-star');
        }else{
            $(button).find('span').removeClass('glyphicon-star').addClass('glyphicon-star-empty');
        }
    }
});
$('.resume .add_favorites').click(function(){
    var button = $(this);
    var resume_to_favour = $(this).data().resume;
    $.get('/api/favorite?res='+resume_to_favour, null, favotite_check);
    function favotite_check(result) {
        if (result == 1){
            $(button).find('span').removeClass('glyphicon-star-empty').addClass('glyphicon-star');
        }else{
            $(button).find('span').removeClass('glyphicon-star').addClass('glyphicon-star-empty');
        }
    }
});
$('.show_seeker_contacts').click(function () {
    var button = $(this);
    var seeker = $(this).data().seeker;
    $.get('/api/getcontacts_seeker?id='+seeker, null, show_contacts);
    function show_contacts(result){
        $(button).replaceWith(result);
        yaCounter39847860.reachGoal('get_contacts_employer');
        return true;
    }
});
$('.show_employer_contacts').click(function(){
    var button = $(this);
    var employer = $(this).data().employer;
    $.get('/api/getcontacts_employer?id='+employer, null, show_contacts);
    function show_contacts(result){
        $(button).replaceWith(result);
        yaCounter39847860.reachGoal('get_contacts_seeker');
        return true;
    }
});