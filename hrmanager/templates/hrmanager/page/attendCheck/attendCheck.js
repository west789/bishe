layui.use(['laydate', 'laypage', 'layer', 'table', 'carousel', 'upload', 'element'], function() {
	var table = layui.table;
	var laydate = layui.laydate;
	//第一个实例
	table.render({
		elem: '#tbl_attendCheck',
		height: 315,
		url: '../../json/check.json', //数据接口
		page: true, //开启分页
		limit: 20,
		skin: 'line', //行边框风格
		even: true, //开启隔行背景
		//				    size: 'sm' ,//小尺寸的表格
		cols: [
			[ //表头
				{
					field: 'id',
					title: 'ID',
					width: 80,
					sort: true,
					fixed: 'left'
				}, {
					field: 'username',
					title: '用户名',
					width: 80
				}, {
					field: 'sex',
					title: '性别',
					width: 80,
					sort: true
				}, {
					field: 'city',
					title: '城市',
					width: 80
				}, {
					field: 'sign',
					title: '签名',
					width: 177
				}, {
					field: 'experience',
					title: '积分',
					width: 80,
					sort: true
				}, {
					field: 'score',
					title: '评分',
					width: 80,
					sort: true
				}, {
					field: 'classify',
					title: '职业',
					width: 80
				}, {
					field: 'wealth',
					title: '财富',
					width: 135,
					sort: true
				}, {
					fixed: 'right',
					width: 165,
					align: 'center',
					toolbar: '#barDemo'
				}
			]
		]
	});
	laydate.render({
		elem: '#dataRange',
		range: true
	}); //监听工具条
	table.on('tool(demo)', function(obj) { //注：tool是工具条事件名，test是table原始容器的属性 lay-filter="对应的值"
		var data = obj.data //获得当前行数据
			,
			layEvent = obj.event; //获得 lay-event 对应的值
		if(layEvent === 'detail') {
			layer.msg('查看操作');
		} else if(layEvent === 'del') {
			layer.confirm('真的删除行么', function(index) {
				obj.del(); //删除对应行（tr）的DOM结构
				layer.close(index);
				//向服务端发送删除指令
			});
		} else if(layEvent === 'edit') {
			layer.msg('编辑操作');
		}
	});
});