layui.use(['laydate', 'laypage', 'layer', 'table', 'carousel', 'upload', 'element'], function() {
	var laydate = layui.laydate;
	laydate.render({
		elem: '#dateleave',
		range: true
	}); //监听工具条
});