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
    /* Establishment */
    $('#establishment_username').val($('#establishment_email').val());
    $('#establishment_email').on('keyup', function(){
        // Autofill Username
        var username = $(this).val();

        $('#establishment_username').val(username);
    });

    /* Resident */
    $('#resident_username').val($('#resident_email').val());
    $('#resident_email').on('keyup', function(){
        // Autofill Username
        var username = $(this).val();

        $('#resident_username').val(username);
    });
    
    /* End Signup Form*/

});