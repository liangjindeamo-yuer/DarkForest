var flag = true;
relievetask2 = function (task_id) {
    flag = false;
    var reason = prompt('可以告诉我为什么取消这次任务么？','无');

    $.getJSON('/App/relievetask2/',{'task_id':task_id,'reason':reason},function (data) {
          alert('已与该发布者解除任务，任务将重新放回任务大厅');
          location.reload();
    })
};
$(function () {
    $('a').click(function () {
        if(!flag){
            return false;
        }
    });
});