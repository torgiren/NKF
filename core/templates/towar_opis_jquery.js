	$(".show_towar").mouseover(function(e){
		id=e.target.id.split('_');
		$.ajax({url:"/ajax/towar/"+id[1],success:function(result){
			$("#float").html(result);
			$("#float").show();
		}});
	});
	$(".show_towar").mousemove(function(e){
//		var pos=$(this).position();
		var scr=$(document).height()
		var height=$('#float').height()
		var dy=e.pageY+height-scr;
		var pos=e.pageY-10;
		if(dy>0)
		{
			pos-=dy
		};
		$("#float").css({position: "absolute",
						top: pos+"px",
						left: (e.pageX+20)+"px"})
	});
	$(".show_towar").mouseout(function(e){
		$("#float").hide();
	});
	$("#float").mouseover(function(){
		$("#float").hide();
	});
