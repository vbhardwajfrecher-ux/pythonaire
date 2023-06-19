$(document).ready(function() {
    // Submit the Pay In form
    $('form').submit(function(event) {
        event.preventDefault();
        var amount = $('#amount').val();
        var description = $('#description').val();
        // Send the form data to the server using AJAX
        $.ajax({
            type: 'POST',
            url: '/pay_in/',
            data: {
                'amount': amount,
                'description': description,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(data) {
                // Handle the success response from the server
                alert(data.message);
            },
            error: function(data) {
                // Handle the error response from the server
                alert('An error occurred while processing your request.');
            }
        });
    });
    
    // Submit the Pay Out form
    $('form').submit(function(event) {
        event.preventDefault();
        var amount = $('#amount').val();
        var description = $('#description').val();
        // Send the form data to the server using AJAX
        $.ajax({
            type:
