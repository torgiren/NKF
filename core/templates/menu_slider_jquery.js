$('legend').siblings().slideUp(0);
//$('.start_open').siblings().slideDown(0);
var cookies={};
if(document.cookie && document.cookie!='')
{
	var split=document.cookie.split(';');
//	alert(split.length);
	for (var i=0;i<split.length;i++)
	{
		name=split[i].split('=')[0];
		type=name.split('.')[0].replace(/^ /,'');
//		alert(i+' '+name+' '+type+'('+type.length+')');
		if(type=="slidedown")
		{
//			alert("zgodny");
			id=name.split('.')[1];
//			alert(id);

			$('#'+id).siblings().slideDown(0);
		};
	};
};

$(function(){
  $('legend').click(function(a){
//   $(this).siblings().slideToggle("slow");
  $(this).siblings().slideToggle("slow",function() {
		var obj=$(this).siblings()[0]
		if($(this).is(":hidden"))
		{
			$.cookie("slidedown."+obj.id,null, {path: '/'});
		}
		else
		{
			$.cookie("slidedown."+obj.id,"tak",{path: '/'});
		};
	  });
  });
});
