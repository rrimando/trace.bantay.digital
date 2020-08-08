$(document).ready(function(){

    
    /* Delete Confirm Dialog */
    $('.delete-confirm').on('click', function() {
        console.log('Test');
        if (confirm("Are you sure?")) {
            return true;
        }
        return false;
    });
    /* End Delete Confirm Dialog */


    /* Signup Form */
    $('#id_username').val($('#id_email').val());
    $('#id_email').on('keyup', function(){
        // Autofill Username
        var username = $(this).val();

        $('#id_username').val(username);
        $('#id_wyvernlms_email_address').val(username);
    });
    /* End Signup Form*/

});