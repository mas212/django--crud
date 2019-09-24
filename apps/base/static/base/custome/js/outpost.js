$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
    //list grid setup file
    $('#list').click(function(event){
        event.preventDefault();
        $('#products .item')
        .addClass('col-md-12');
        $('.card > .card-body').addClass('row');
        $('.card > .card-body > .rfcontentIcon').addClass('col-md-4');
        $('.card > .card-body > .rftitle')
        .addClass('col-md-5')
        .css('margin-top','13px');
        $('.card > .card-body > .rfsize').addClass('col-md-2');
        //recent file
        $('.rfolderListTitle > .boxCardListFolder').addClass('row');
        $('.rfolderListTitle > .boxCardListFolder > .rIcon').addClass('col-md-2 iconfile');
        $('.rfolderListTitle > .boxCardListFolder > .rTitle').addClass('col-md-7');
        $('.rfolderListTitle > .boxCardListFolder > .rSize').addClass('col-md-2');
    });

    $('#grid').click(function(event){
        event.preventDefault();
        $('#products .item')
        .removeClass('col-md-12');
        $('#products .item')
        .addClass('col-md-4');
        //remove file
        $('.card > .card-body').removeClass('row');
        $('.card > .card-body > .rfcontentIcon').removeClass('col-md-4');
        $('.card > .card-body > .rftitle')
        .removeClass('col-md-5')
        .css('margin-top','13px');
        $('.card > .card-body > .rfsize').removeClass('col-md-2');
        //recent file
        $('.rfolderListTitle > .boxCardListFolder').removeClass('row');
        $('.rfolderListTitle > .boxCardListFolder > .rIcon').removeClass('col-md-2 iconfile');
        $('.rfolderListTitle > .boxCardListFolder > .rTitle').removeClass('col-md-7');
        $('.rfolderListTitle > .boxCardListFolder > .rSize').removeClass('col-md-2');
    });
});