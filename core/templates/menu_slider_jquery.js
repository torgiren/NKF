$('legend').siblings().slideUp(0);
$('.start_open').siblings().slideDown(0);
$(function(){
  $('legend').click(function(a){
//   $(this).siblings().slideToggle("slow");
   $(this).siblings().slideToggle("slow");
		$.ajax({url:"/ajax/menu/"+$(this)[0].id+"/",success:function(result){
//			$("#float").html(result);
//			$("#float").show();
		}});
  });
});
