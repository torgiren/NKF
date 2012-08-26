	$(".show_kontrahent").mouseover(function(e){
		id=e.target.id.split('_');
		$.ajax({url:"/ajax/kontrahent/"+id[1],success:function(result){
			$("#float").html(result);
			$("#float").show();
		}});
	});
	$(".show_kontrahent").mousemove(function(e){
		var pos=$(this).position();
		$("#float").css({position: "absolute",
						top: e.pageY+"px",
						left: (e.pageX+20)+"px"})
	});
	$(".show_kontrahent").mouseout(function(e){
		$("#float").hide();
	});
	$("#float").mouseover(function(){
		$("#float").hide();
	});
