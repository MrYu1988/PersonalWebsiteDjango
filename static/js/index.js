$(function(){
	alert('goods');

	// 设置男士显示高度为宽度的1.8倍
	var manWidth = $(".manBoxBanner").width();
	$(".manBoxBanner").height(manWidth*1.6);
	
	// 设置女士显示高度为宽度的1.8倍
	var lidyWidth = $(".lidyBox").width();
	$(".lidyBox").height(lidyWidth*1.6);
	
	$(".bigScreen").height(lidyWidth*0.5)
	
	$(".leftBlockClass").height(lidyWidth*1.6);
	$(".rightBlock").height(lidyWidth*1.6);
})

$(window).resize(function(){
	// 设置男士显示高度为宽度的1.8倍
	var manWidth = $(".manBoxBanner").width();
	$(".manBoxBanner").height(manWidth*1.6);
	
	// 设置女士显示高度为宽度的1.8倍
	var lidyWidth = $(".lidyBox").width();
	$(".lidyBox").height(lidyWidth*1.6);
	
	//设置大屏幕的高度为女士宽度的0.5倍	
	$(".bigScreen").height(lidyWidth*0.5)
	
	// 设置左右空白处高度
	$(".leftBlockClass").height(lidyWidth*1.6);
	$(".rightBlock").height(lidyWidth*1.6);
	
})