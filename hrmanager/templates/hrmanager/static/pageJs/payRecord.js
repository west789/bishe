layui.use(['layer', 'table', 'element', 'jquery'], function() {
	var table = layui.table;
	var laydate = layui.laydate;
	$ = layui.jquery;

	//第一个实例
	table.render({
		elem: '#tbl_payRecord',
		height: 500,
		url: '/hrmanager/get_payment/', //数据接口

		page: false, //开启分页
		limit: 20,
		skin: 'line', //行边框风格
		even: true, //开启隔行背景
		//				    size: 'sm' ,//小尺寸的表格
		//width : 1000,
		id: 'testReload',
		cols: [
			[ //表头
				{
					field: 'paymentId',
					title: '记录编号',
					width: 100,
					sort: true,
					fixed: 'left'
				}, {
					field: 'employeeName',
					title: '员工姓名',
					width: 200
				}, {
					field: 'attendResult',
					title: '出勤情况',
					width: 300,
					sort: true
				}, {
					field: 'payment',
					title: '工资总额',
					width: 300,
					sort: true
				}, {
					field: 'createTime',
					title: '创建时间',
					//width: 200
				}
			]
		]
	});
	// table.on('tool(demo)', function(obj) { //注：tool是工具条事件名，test是table原始容器的属性 lay-filter="对应的值"
	// 	var data = obj.data //获得当前行数据
	// 		,
	// 		layEvent = obj.event; //获得 lay-event 对应的值
	// 	if(layEvent === 'detail') {
	// 		layer.msg('查看操作');
	// 	} else if(layEvent === 'del') {
	// 		layer.confirm('真的删除行么', function(index) {
	// 			obj.del(); //删除对应行（tr）的DOM结构
	// 			layer.close(index);
	// 			//向服务端发送删除指令
	// 		});
	// 	} else if(layEvent === 'edit') {
	// 		layer.msg('编辑操作');
	// 	}
	// });
	// active = {
	// 	reload :function () {
    //
	// 		table.reload('testReload',{
  	// 		where:{
  	// 			attendStatus:$('#statusSel').val()
	// 		}
	// 	}); //重载表格
     //    }
	// }
    // $('#check').click(function () {
	// 	 var type = $(this).data('type');
	// 	 active[type] ? active[type].call(this) : '';
    //
    // })
});