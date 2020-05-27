
checktask = function () {
    var $taskname = $('#taskname_input');
    var taskname = $taskname.val().trim();
    if (!taskname) {
        var $taskname_info = $('#taskname_info');
        $taskname_info.html('任务名称不能为空').css('color', 'grey');
        return false;
    }
    var $taskreward = $('#taskreward_input');
    var taskreward = $taskreward.val().trim();
    if(!taskreward){
        var $taskreward_info = $('#taskreward_info');
        $taskreward_info.html('天下没有免费的午餐，多少给点吧！').css('color','grey');
        return false;
    }
    alert('发布任务成功!可到个人中心查看');
    return true;
};
$(function () {
    var $taskname = $('#taskname_input');
    $taskname.change(function () {
        var $taskname_info = $('#taskname_info');
        $taskname_info.html('');
    });
    var $taskreward = $('#taskreward_input');
    $taskreward.change(function () {
        var $taskreward_info = $('#taskreward_info');
        $taskreward_info.html('');
    });
});
