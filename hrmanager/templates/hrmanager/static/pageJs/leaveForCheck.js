layui.use(['laydate', 'laypage', 'layer', 'table', 'carousel', 'upload', 'element'], function() {
	var table = layui.table;
	var laydate = layui.laydate;
	//第一个实例
	table.render({
		elem: '#tbl_attendCheck',
		height: 500,
		url: '/hrmanager/leaveCheck_handle/', //数据接口
		page: true, //开启分页
		limit: 20,
		skin: 'line', //行边框风格
		even: true, //开启隔行背景
		cellMinWidth: 200,	
		//width: 1200,
		cols: [
			[ //表头
				{
					field: 'leaveInfoId',
					title: '请假编号',
					width: 100,
					sort: true,
					fixed: 'left'
				}, {
					field: 'employeeName',
					title: '员工姓名',
					width: 200
				}, {
					field: 'leaveTime',
					title: '请假时间',
					width: 200,
					sort: true
				}, {
					field: 'createTime',
					title: '创建时间',
					width: 200,
					sort: true
				}, {
					field: 'leaveStatus',
					title: '审批状态',
					width: 200,
					sort: true
				}, {
					field: 'leaveDays',
					title: '请假天数',
					//width: 200,
					sort: true
				}, {
					field: 'leaveReason',
					title: '请假原因',
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