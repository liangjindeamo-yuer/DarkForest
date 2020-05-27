function check() {
    var $username = $('#username_input');
    var username = $username.val().trim();
    if (!username) {
        var $user_info = $('#username_info');
        $user_info.html('用户名不能为空').css('color', 'grey');
        return false;
    }
    var $password = $('#password_input');
    var password = $password.val().trim();
    password = password.toString();
    if (!password) {
        var $password_info = $('#password_info');
        $password_info.html('密码不能为空').css('color', 'grey');
        return false;
    }
    var username_info = $('#username_info');
    var password_info = $('#password_info');
    username_info.empty();
    password_info.empty();
    $.getJSON('/App/checklogin/', {
        'username': username,
        'password': password,
    }, function (data) {
        if (data['status'] === 903) {
            password_info.html('密码错误').css('color', 'red');
            alert('密码错误');
            return false;
        } else if (data['status'] === 904) {
            username_info.html('用户名不存在').css('color', 'red');
            alert('用户名不存在');
            return false;
        } else if (data['status'] === 200) {
            return true;
        }
    })
}