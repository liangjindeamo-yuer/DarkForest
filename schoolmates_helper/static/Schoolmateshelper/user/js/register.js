var key = false;
$(function () {

    var $username = $('#username_input');
    $username.change(function () {
        var username = $username.val().trim();
        if (username.length) {
            //将用户名发送服务器预校验
            $.getJSON('/App/checkuser/', {'username': username}, function (data) {
                console.log(data);
                var $username_info = $('#username_info');
                if (data['status'] === 200) {
                    $username_info.html('用户名可用').css('color', 'green');
                } else if (data['status'] === 901) {
                    $username_info.html('用户名已存在').css('color', 'red');
                }
            })

        }
    })
});
$(function () {
    var $email = $('#email_input');
    $email.change(function () {
        var email = $email.val().trim();
        if (email.length) {
            //将邮箱发送服务器预校验
            $.getJSON('/App/checkemail/', {'email': email}, function (data) {
                console.log(data);
                var $email_info = $('#email_info');
                if (data['status'] === 200) {
                    $email_info.html('邮箱可用').css('color', 'green');
                } else if (data['status'] === 902) {
                    $email_info.html('该邮箱已被注册').css('color', 'red');
                }
            })

        }
    })
});


$(function () {
    var $password_confirm = $('#password_confirm_input');
    var $password = $('#password_input');
    $password_confirm.change(function () {
        var password_confirm = $password_confirm.val().trim();
        password_confirm = password_confirm.toString();

        var password = $password.val().trim();
        password = password.toString();
        if (password.length<=6){
            var $password_info = $('#password_info');
            $password_info.html('你的密码过于简单').css('color', 'red');
        }
        else{
             var $password_info = $('#password_info');
            $password_info.html('密码安全').css('color', 'green');
        }
        if (!(password_confirm == password)) {
            var $password_confirm_info = $('#password_confirm_info');
            $password_confirm_info.html('验证密码不一致').css('color', 'red');
        }
        else {
            var $password_confirm_info = $('#password_confirm_info');
            $password_confirm_info.html('验证密码一致').css('color', 'green');
        }
    });
    $password.change(function () {
        var password_confirm = $password_confirm.val().trim();
        password_confirm = password_confirm.toString();

        var password = $password.val().trim();
        password = password.toString();
        if (password.length<=6){
            var $password_info = $('#password_info');
            $password_info.html('你的密码过于简单').css('color', 'red');
        }
        else{
             var $password_info = $('#password_info');
            $password_info.html('密码安全').css('color', 'green');
        }
        if (!(password_confirm == password)) {
            var $password_confirm_info = $('#password_confirm_info');
            $password_confirm_info.html('验证密码不一致').css('color', 'red');
        }
        else {
            var $password_confirm_info = $('#password_confirm_info');
            $password_confirm_info.html('验证密码一致').css('color', 'green');
        }
    })
});

function check() {

    var $username = $('#username_input');
    var username = $username.val().trim();
    if (!username) {
        var $user_info = $('#username_info');
        $user_info.html('用户名不能为空').css('color', 'grey');
        return false;
    }

    var $email = $('#email_input');
    var email = $email.val().trim();
    email = email.toString();
    if (!email) {
        var $email_info = $('#email_info');
        $email_info.html('邮箱不能为空').css('color', 'grey');
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

    var $password_confirm = $('#password_confirm_input');
    var password_confirm = $password_confirm.val().trim();
    password_confirm = password_confirm.toString();
    if (!password_confirm) {
        var $password_confirm_info = $('#password_confirm_info');
        $password_confirm_info.html('请确认你的密码').css('color', 'grey');
        return false;
    }

    var $icon = $('#icon_input');
    var icon = $icon.val().trim();

    if (!icon.length) {
        var $icon = $('#icon_info');
        $icon.html('请选择你的头像').css('color', 'grey');
        return false;
    }



    var info_username_color = $('#username_info').css('color');
    var info_email_color = $('#email_info').css('color');
    var info_password_confirm_color = $('#password_confirm_info').css('color');
    var info_password_color = $('#password_info').css('color')
    if (info_username_color == 'rgb(255, 0, 0)' || info_email_color == 'rgb(255, 0, 0)' || info_password_confirm_color == 'rgb(255, 0, 0)'||info_password_color == 'rgb(255, 0, 0)') {
        return false;
    } else {
        alert('注册成功，请注意前往邮箱激活您的账户');
        return true;
    }
}
