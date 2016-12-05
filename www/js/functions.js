  $(document).ready(function(){
     $(".button-collapse").sideNav();

     $('select').material_select();

     $('.neuro-btn').on('click', function(){
	    $('.neuro-btn').removeClass('selected');
	    $(this).addClass('selected');
	});

     $('.clinical-btn').on('click', function(){
	    $('.clinical-btn').removeClass('selected');
	    $(this).addClass('selected');
	});
  
  });