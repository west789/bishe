layui.use(['laydate', 'laypage', 'layer', 'table', 'carousel', 'upload', 'element'], function() {
	var table = layui.table;
	var laydate = layui.laydate;
	//第一个实例
	table.render({
		elem: '#tbl_attendCheck',
		height: 500,
		url: '../../json/check.json', //数据接口
		page: true, //开启分页
		limit: 20,
		skin: 'line', //行边框风格
		even: true, //开启隔行背景
		cellMinWidth: 200,	
		width: 600,
		cols: [
			[ //表头
				{
					field: 'id',
					title: '工号',
					width: 200,
					sort: true,
					fixed: 'left'
				}, {
					field: 'username',
					title: '姓名',
					width: 200
				}, {
					field: 'classify',
					title: '职位',
					width: 200,
					sort: true
				}
			]
		]
	});
	laydate.render({
		elem: '#dataRange',
		range: true
	}); //监听工具条
});