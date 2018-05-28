layui.config({
	base : "js/"
}).use(['form','element','layer','jquery'],function(){
	var form = layui.form(),
		layer = parent.layer === undefined ? layui.layer : parent.layer,
		element = layui.element(),
		$ = layui.jquery;

	$(".panel a").on("click",function(){
		window.parent.addTab($(this));
	})



	//正常出勤数
    $.get("/hrmanager/attendRecordCount/",
        function (data) {
            $(".attendNormal span").text(data.attendNormal);
            $(".attendAbnormal span").text(data.attendAbnormal);
            var obj = data.abnormalData
			var inhtml = '<colgroup><col width="150"></colgroup><tbody><thead><td>异常时间</td><td>异常原因</td><td></td></thead>';
            $.each(obj, function (item, value) {

                inhtml += '<tr><td>' + value.abnormalTime + '</td><td>' + value.abnormalReason + '</td><td><a  href="/hrmanager/page/attendCheck/" style="color: #1b9dec">查看</a></td></tr>'

            })
            inhtml += '</tbody>';
            $("#table_abnormal").html(inhtml);
        }
    )

	//用户数
	$.get("../json/usersList.json",
		function(data){
			$(".userAll span").text(data.length);
		}
	)

	//新消息
	$.get("../json/message.json",
		function(data){
			$(".newMessage span").text(data.length);
		}
	)


	//数字格式化
	$(".panel span").each(function(){
		$(this).html($(this).text()>9999 ? ($(this).text()/10000).toFixed(2) + "<em>万</em>" : $(this).text());	
	})

	//系统基本参数
	if(window.sessionStorage.getItem("systemParameter")){
		var systemParameter = JSON.parse(window.sessionStorage.getItem("systemParameter"));
		fillParameter(systemParameter);
	}else{
		$.ajax({
			url : "../json/systemParameter.json",
			type : "get",
			dataType : "json",
			success : function(data){
				fillParameter(data);
			}
		})
	}

	//填充数据方法
 	function fillParameter(data){
 		//判断字段数据是否存在
 		function nullData(data){
 			if(data == '' || data == "undefined"){
 				return "未定义";
 			}else{
 				return data;
 			}
 		}
 		$(".version").text(nullData(data.version));      //当前版本
		$(".author").text(nullData(data.author));        //开发作者
		$(".homePage").text(nullData(data.homePage));    //网站首页
		$(".server").text(nullData(data.server));        //服务器环境
		$(".dataBase").text(nullData(data.dataBase));    //数据库版本
		$(".maxUpload").text(nullData(data.maxUpload));    //最大上传限制
		$(".userRights").text(nullData(data.userRights));//当前用户权限
 	}

})
