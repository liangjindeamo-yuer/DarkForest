var flag = true;

$(function () {
    $('a').click(function () {
        if (!flag) {
            return false;
        }
    });
});

on_click_alltask = function (task_id, is_login) {
    flag = false;
    var contact_id = prompt("请输入你想给发布者的联系方式（输入数字1-5，其中1：email，2：QQ，3：wechat，4：telephone,5:其它联系方式）",0);
    $.getJSON('/App/receivetask/', {'task_id': task_id, 'is_login': is_login,'contact_id':contact_id}, function (data) {
        if (data['status'] === 200) {
            alert('任务已接受，请到个人中心查看');
        } else if (data['status'] === 905) {
            alert('请先激活您的账户');
            flag=true;
        } else if (data['status'] === 906) {
            alert('请先登录您的账户!');
            flag=true;
        }
        location.reload();
    })
};