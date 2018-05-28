layui.use(['layer',  'element', 'jquery'], function () {
    
    var $ = layui.jquery;
    var myChart = echarts.init(document.getElementById('main'));
    var myChart1 = echarts.init(document.getElementById('main1'));
    $.get('/hrmanager/attendRecordCount/',function (data) {
        $("#attendNormal").text(data.attendNormal);
        $("#attendAbnormal").text(data.attendAbnormal);
        option = {
        title: {
            text: '当月个人考勤统计',
            subtext: '以最终统计为准',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['加班', '旷工', '请假', '异常', '缺勤', '正常']
        },
        series: [
            {
                name: '考勤状态',
                type: 'pie',
                radius: '55%',
                center: ['50%', '50%'],
                data: [
                    {value: 1, name: '加班'},
                    {value: 2, name: '旷工'},
                    {value: 4, name: '请假'},
                    {value: 1, name: '异常'},
                    {value: 3, name: '缺勤'},
                    {value: data.attendNormal, name: '正常'}
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
    })

    // 指定图表的配置项和数据

    myChart1.title = '堆叠柱状图';

    option1 = {
        title: {
            text: '各月考勤',
            subtext: '以最终统计为准',

        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        legend: {
            data: ['加班', '旷工', '请假', '异常', '缺勤', '正常']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ['一月份', '二月份', '三月份', '四月份', '五月份']
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '加班',
                type: 'bar',
                data: [11, 11, 10, 9, 8, 15, 8]
            },
            {
                name: '旷工',
                type: 'bar',
                barWidth: 5,
                data: [1, 0, 0, 0, 1, 0, 1]
            },
            {
                name: '请假',
                type: 'bar',
                data: [3, 1, 2, 1, 3, 1, 1]
            },
            {
                name: '异常',
                type: 'bar',
                stack: '广告',
                data: [5, 4, 5, 4, 5, 4, 3]
            },
            {
                name: '缺勤',
                type: 'bar',
                data: [1, 2, 1, 2, 1, 2, 1]
            },
            {
                name: '正常',
                type: 'bar',
                data: [22, 23, 22, 23, 21, 20, 21],
            }
        ]
    };


    myChart1.setOption(option1);
});