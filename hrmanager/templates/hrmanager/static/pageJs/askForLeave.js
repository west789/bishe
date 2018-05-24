layui.use(['laydate', 'laypage', 'layer', 'table', 'carousel', 'upload', 'element'], function() {
	var laydate = layui.laydate;
	var curDate = new Date()
	curDate = curDate.getFullYear()+ '-'+ (curDate.getMonth()+1) + '-'+ curDate.getDate()
	laydate.render({
		elem: '#dateleave',
	 	range: true,
		min : curDate,
		//max : '2018-05-30',
	}); //监听工具条
});