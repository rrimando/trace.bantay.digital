$(document).ready(function(){

    var wyvern_content_editor = $('#wyvern-content-editor').trumbowyg({
        autogrow: true
    });

    var wyvern_content_editor_modal = $('#custom-content-editor-modal');
    var content_content = '';
    var site = document.domain;

    var save_button = $('.wyvern-content-editors-save');
    var content_slug = '';

    $('.wyvern-content-editor').each(function(){

        var edit_button = $('<i class="fa fa-pencil wyvern-content-edit-button"></i>');
        var slug = $(this).attr('data-slug');

        edit_button.on('click', function(){
            content_slug = slug;
        });

        edit_button.css({
            'position': 'relative',
            'top': 0,
            'right': 0,
            'z-index': 1,
            'cursor': 'pointer'
        });

        $('#custom-content-editor-title').css({
            'color': '#000000'
        });

        $(this).before(edit_button);    
    });

    $('.wyvern-content-edit-button').on('click', function(){
        /* Fetch Custom Content */
        $.get( "/cc/fetch/" + content_slug + "/" + site + "/", function( data ) {
            $('#custom-content-editor-title, .modal-title').text(data['title']);
            wyvern_content_editor.html('');
            wyvern_content_editor.html(data['content']);
        });

        wyvern_content_editor_modal.modal();
    });

     save_button.on('click', function(){

        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

        /* Save Custom Content  */
        console.log('Save');
        $.ajax({
            type: "POST",
            url: "/cc/update/" + content_slug + "/" + site + "/",
            data: {
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'wyvern_custom_content_content': wyvern_content_editor.trumbowyg('html')
            },
            success: function(){
                location.reload();
            }
        });

    });

});