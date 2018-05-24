layui.config({
	base : "/static/js/"
}).use(['form','layer','jquery','laypage'],function() {
    var form = layui.form(),
        layer = parent.layer === undefined ? layui.layer : parent.layer,
        laypage = layui.laypage,
        $ = layui.jquery;

    //$('input').attr('disabled', true);
    $('#edit').click(function () {
        $('.able').attr('disabled', false);

    })
    $("#form1").ajaxForm(function(data){

            layer.alert("提交成功！", {icon: 1});

    });
    // $('#save').click(function () {
    //     // $.post('/hrmanager/personSave/',{csrfmiddlewaretoken:$("input:first").val()}, function(data){
    //     // 	if(data.code == 200){
    //     // 		layer.alert('保存成功', {icon: 1});
		// 	// }
    //     // })
    //     $.post(function () {
    //
    //     })
    // })
    //加载页面数据
    var newsData = '';
    $.get("/hrmanager//newsList.json", function (data) {
        var newArray = [];
        //单击首页“待审核文章”加载的信息
        if ($(".top_tab li.layui-this cite", parent.document).text() == "待审核文章") {
            if (window.sessionStorage.getItem("addNews")) {
                var addNews = window.sessionStorage.getItem("addNews");
                newsData = JSON.parse(addNews).concat(data);
            } else {
                newsData = data;
            }
            for (var i = 0; i < newsData.length; i++) {
                if (newsData[i].newsStatus == "待审核") {
                    newArray.push(newsData[i]);
                }
            }
            newsData = newArray;
            newsList(newsData);
        } else {    //正常加载信息
            newsData = data;
            if (window.sessionStorage.getItem("addNews")) {
                var addNews = window.sessionStorage.getItem("addNews");
                newsData = JSON.parse(addNews).concat(newsData);
            }
            //执行加载数据的方法
            newsList();
        }
    })
})




	// 	//改变窗口大小时，重置弹窗的高度，防止超出可视区域（如F12调出debug的操作）
	// 	$(window).resize(function(){
	// 		layui.layer.full(index);
	// 	})
	// 	layui.layer.full(index);
	// })



	//是否展示
	// form.on('switch(isShow)', function(data){
	// 	var index = layer.msg('修改中，请稍候',{icon: 16,time:false,shade:0.8});
     //    setTimeout(function(){
     //        layer.close(index);
	// 		layer.msg("展示状态修改成功！");
     //    },2000);
	// })
    //
	// //操作
	// $("body").on("click",".news_edit",function(){  //编辑
	// 	layer.alert('您点击了文章编辑按钮，由于是纯静态页面，所以暂时不存在编辑内容，后期会添加，敬请谅解。。。',{icon:6, title:'文章编辑'});
	// })
    //
	// $("body").on("click",".news_collect",function(){  //收藏.
	// 	if($(this).text().indexOf("已收藏") > 0){
	// 		layer.msg("取消收藏成功！");
	// 		$(this).html("<i class='layui-icon'>&#xe600;</i> 收藏");
	// 	}else{
	// 		layer.msg("收藏成功！");
	// 		$(this).html("<i class='iconfont icon-star'></i> 已收藏");
	// 	}
	// })





