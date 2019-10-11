$image_crop = $('#cropper').croppie({
	enableExif: true,
	viewport: {
	  width:300,
	  height:300,
	  type:'circle' 
	},
	boundary:{
	  width:300,
	  height:300
	}
});

$(document).ready(function() {
  
    setTimeout(function(){
  	$('#flashmessage').hide('slow');
    }, 4000);

    $image_crop = $('#cropper').croppie({
	enableExif: true,
	viewport: {
	  width:300,
	  height:300,
	  type:'circle' 
	},
	boundary:{
	  width:300,
	  height:300
	}
    });

    $('#uploadimage').on('change', function(){
	var reader = new FileReader();
	reader.onload = function (event) {
	    $image_crop.croppie('bind', {
	    	url: event.target.result
	    }).then(function(){
	    	console.log('jQuery bind complete');
	    });
	}
	reader.readAsDataURL(this.files[0]);
	$('#cropimage').modal('show');
    });
    
    $('#uploadbtn').click(function(event){
	$image_crop.croppie('result', {
	    type: 'canvas',
	    size: 'viewport'
	}).then(function(response){
	    $.ajax({
		url:"/upload_profile",
		type: "POST",
		data:{"image": response},
		success:function(data){
		    $('#cropimage').modal('hide');
		    $('#feedback').html("Profile picture updated"); 
		}
	    });
	})
    });
});
