$(document).ready(function() {

    setTimeout(function(){
  		$('#flashmessage').hide('slow');
    }, 5000);

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

    $(function () {
	  $('[data-toggle="popover"]').popover()
	})

    $("#uploadimagebtn").click(function() {
	    $("input[id='uploadimage']").click();
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
				    $('#feedback').html("Profile picture updated! Please referesh page");
				    location.reload();
				}
		    });
		});	
    });


    $(function() {
		var Page = (function() {

			var $navArrows = $( '#nav-arrows' ).hide(),
				$shadow = $( '#shadow' ).hide(),
				slicebox = $( '#sb-slider' ).slicebox( {
					onReady : function() {

						$navArrows.show();
						$shadow.show();

					},
					orientation : 'r',
					cuboidsRandom : true,
					autoplay: true,
					disperseFactor : 30
				} ),
				
				init = function() {

					initEvents();
					
				},
				initEvents = function() {

					// add navigation events
					$navArrows.children( ':first' ).on( 'click', function() {

						slicebox.next();
						return false;

					} );

					$navArrows.children( ':last' ).on( 'click', function() {
						
						slicebox.previous();
						return false;

					} );

				};

				return { init : init };

		})();

		Page.init();

	});

	$(function() {
		$( '#nav-prev' ).on( 'mousedown', function( event ) {

			allownavprev = true;
			navprev();
		
		} ).on( 'mouseup mouseleave', function( event ) {

			allownavprev = false;
		
		} );

		$( '#nav-next' ).on( 'mousedown', function( event ) {

			allownavnext = true;
			navnext();
		
		} ).on( 'mouseup mouseleave', function( event ) {

			allownavnext = false;
		
		} );

		function navnext() {
			if( allownavnext ) {
				windy.next();
				setTimeout( function() {	
					navnext();
				}, 150 );
			}
		}

		function navprev() {
			if( allownavprev ) {
				windy.prev();
				setTimeout( function() {	
					navprev();
				}, 150 );
			}
		}

	});

	

	/** code by webdevtrick ( https://webdevtrick.com ) **/
    [...document.querySelectorAll('.single-column')].map(column => {
      column.style.setProperty('--animation', 'slide');
      column.style.setProperty('height', '200%');
      column.innerHTML = column.innerHTML + column.innerHTML;
    });
    
    new ElastiStack( document.getElementById( 'elasticstack' ) );


    var clock, minute;
	
	$(function() {
		var date = new Date(2019, 10, 10);
	    var now = new Date();
	    var diff = (date.getTime()/1000) - (now.getTime()/1000);
	    var clock = $('.clock').FlipClock(diff,{
	        clockFace: 'DailyCounter',
	        countdown: true
	    });  
	});
});


