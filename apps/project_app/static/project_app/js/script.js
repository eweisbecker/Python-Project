$(document).ready(function(){
    $('#nameInput').keyup(function(){
        if ($('#nameInput').val().length < 2) {
            $('#new_proj_button').prop('disabled', true);
        } else {
            $('#new_proj_button').prop('disabled', false);
        }
    });
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
    });
})