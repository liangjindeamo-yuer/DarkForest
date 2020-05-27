$(function () {
    $('#not_login').click(function () {
        window.open('/App/login/',target='_self');
    })
})
$(function () {
    $('#not_activate').click(function () {
        $.getJSON('/App/sendemail/',{},function (data) {
            if (data['send_successfully']===true){
                alert('已经向您的邮箱发送激活邮件，请在一天之内及时确认激活')
            }
            else{
                alert('发送邮件失败，请确认您的邮箱是否正确!')
            }

            return true;
        })
    })
})