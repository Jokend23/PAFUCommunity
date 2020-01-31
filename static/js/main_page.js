$(document).ready(function(){
    $.get('/api/gethotvacancies', null, makehotvacancy, 'html');
    function makehotvacancy(data) {
        $('.hot_vac').append(data).hide().slideDown();
    }

    $.get('/api/getjobru', null, makejobru, 'html');
    function makejobru(data){
        $('.job_ru').append('<div class="job_ru_news" >'+data+'</div>').hide().slideDown();
    }
});