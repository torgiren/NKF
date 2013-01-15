$('legend').siblings().slideUp(0);
$('.start_open').siblings().slideDown(0);
$(function(){
  $('legend').click(function(a){
//   $(this).siblings().slideToggle("slow");
  $(this).siblings().slideToggle("slow",function() {
		var obj=$(this).siblings()[0]
		if($(this).is(":hidden"))
		{
			$.cookie("menu_slide_"+obj.id,null);
		}
		else
		{
			$.cookie("menu_slide_"+obj.id,"tak");
		};
	  });
  });
});
