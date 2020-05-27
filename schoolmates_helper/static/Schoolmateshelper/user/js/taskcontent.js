checktask = function () {
    var $comment = $('#comment_input');
    var comment = $comment.val().trim();
    if (!comment) {
        var $comment_info = $('#comment_info');
        $comment_info.html('好歹说两句').css('color', 'grey');
        alert("评论不能为空");
        return false;
    }
    alert('添加评价成功');
    return true;
};
checkresponse = function ( discuss_id ) {
    var d = discuss_id.toString();
    var $response = $('#response_input'+d);
    var response = $response.val().trim();
    if (!response) {
        var $response_info = $('#response_info'+d);
        $response_info.html('好歹说两句').css('color', 'grey');
        alert("回复不能为空");
        return false;
    }
    alert('回复成功');
    return true;
};
checkdiscuss = function () {
    var $discuss = $('#discuss_input');
    var discuss = $discuss.val().trim();
    if (!discuss) {
        var $discuss_info = $('#discuss_info');
        $discuss_info.html('好歹说两句').css('color', 'grey');
        alert("帖子不能为空");
        return false;
    }
    alert('添加帖子成功');
    return true;
};