
$(function() {
    var form = $('#commentform');
    
    function restore_commentbutton() {
    	$("#commentbutton").attr({'disabled': false, 'value': 'Pošalji komentar'});
    }
    
	function callback_post(response) {
	    restore_commentbutton();
	    $('#comments').append('<tr><td>' + response.new_comment + '</td></tr>');
	}
	
	function callback_load(response) {
	    restore_commentbutton();
	}
	
	function on_submit(event) {
	    event.preventDefault();
	    $("#commentbutton").attr({'disabled': true, 'value': 'Šaljem...'});
	    
	    $.post(form.attr('action'), form.serializeArray(), callback_post, 'json');
		/*$('#comments').load(form.attr('action') + ' #comments',
			                form.serializeArray(), callback_load);//*/
	}
	
    form.submit(on_submit);
});

