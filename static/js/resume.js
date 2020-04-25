$(function(){
	var bigScreenWidth = $(".bigScreen").width();
	if (bigScreenWidth < 763)
		$(".introduce").hide();
	else
		$(".introduce").show();
	
	// 获取leftcol的与左边界的坐标,对	introduce修改为leftcol坐标
	var leftCol = $(".leftCol").offset();
	var introduceTop = $(".bigScreen").height();
	$(".introduce").offset({top:introduceTop,left:leftCol.left});
	
})

$(window).resize(function(){
	var bigScreenWidth = $(".bigScreen").width();
	
	if (bigScreenWidth < 763)
		$(".introduce").hide();
	else
		$(".introduce").show();	
		
	// 获取leftcol的与左边界的坐标,对	introduce修改为leftcol坐标	
	var leftCol = $(".leftCol").offset();
	var introduceTop = $(".bigScreen").height();
	$(".introduce").offset({top:introduceTop,left:leftCol.left});
	
})