$('legend').siblings().slideUp(0);
$(function(){
  $('legend').click(function(){
   $(this).siblings().slideToggle("slow");
  });
});
