layui.use([ 'table', 'jquery'], function() {
	var table = layui.table;
	$ = layui.jquery;

	//第一个实例
	table.render({
		elem: '#paycount',
		height: 300,
		url: '/hrmanager/get_paycount/', //数据接口

		page: true, //开启分页
		limit: 5,
		skin: 'line', //行边框风格
		even: true, //开启隔行背景
		//				    size: 'sm' ,//小尺寸的表格
		//width : 1900,
		cols: [
			[ //表头
				{
					field: 'employeeName',
					title: '员工姓名',
					width: 100,
					sort: true,
					fixed: 'left'
				}, {
					field: 'paytotalDays',
					title: '总天数',
					width: 200
				}, {
					field: 'normalDays',
					title: '正常',
					width: 200
				}, {
					field: 'lessDays',
					title: '缺勤',
					width: 200,
					sort: true
				}, {
					field: 'abnormalDays',
					title: '异常',
					width: 200,
					sort: true
				}, {
					field: 'leaveDays',
					title: '请假',
					width: 200
				}, {
					field: 'absentDays',
					title: '旷工',
					width: 100
				}, {
					field: 'workmoreDays',
					title: '加班',
					width: 100
				}, {
					field: 'normalRate',
					title: '出勤率',
					width: 200
				}
			]
		],
        done: function (res, curr, count) {
            $('#countlist').val(res.countList)
        }
	});

});
$('#proReport').click(function () {
    var countList = $('#countlist').val()
    countList = countList.split('|')
    var myChart = echarts.init(document.getElementById('main'));
var myChart1 = echarts.init(document.getElementById('main1'));

        // 指定图表的配置项和数据
        option = {
    title : {
        text: '当月考勤统计',
        subtext: '以最终统计为准',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['加班','旷工','请假','异常','缺勤','正常']
    },
    series : [
        {
            name: '考勤状态',
            type: 'pie',
            radius : '55%',
            center: ['50%', '50%'],
            data:[
                {value:countList[5], name:'加班'},
                {value:countList[4], name:'旷工'},
                {value:countList[3], name:'请假'},
                {value:countList[2], name:'异常'},
                {value:countList[1], name:'缺勤'},
                {value:countList[0], name:'正常'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};





myChart.setOption(option);
myChart1.title = '堆叠柱状图';

option1 = {
     title : {
        text: '当月考勤统计',
        subtext: '以最终统计为准',
        x:'center'
    },
    xAxis: {
        type: 'category',
        data: ['加班','旷工','请假','异常','缺勤','正常']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [countList[5], countList[4], countList[3], countList[2], countList[1], countList[0]],
        type: 'bar'
    }]
};


myChart1.setOption(option1);
})
$('#proPayReport').click(function () {
    $.get('/hrmanager/paymentAll/',function (data) {
        var paymentObj = JSON.parse(data.paymentData)
        inhtml = '<thead>\n' +
            '            <td>姓名</td>\n' +
            '            <td>出勤状况</td>\n' +
            '        <td>工资</td>\n' +
            '        <td>创建时间</td>\n' +
            '        </thead>\n' +
            '        <tbody><tr>';
        $.each(paymentObj, function (item, value) {
            inhtml += '<tr><td>'+value.fields.employeeId+'</td><td>'+value.fields.attendRecordInfo+'</td>\n' +
                '<td>'+value.fields.payment+'</td><td>'+value.fields.createTime+'</td>\n' +
                '</tr>';
        })
        inhtml += '</tbody>';
        $("#paymentAll").html(inhtml);
    })
})
