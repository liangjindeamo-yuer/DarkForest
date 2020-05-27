on_click_base_main = function (is_login, is_activate) {
    if (is_login) {
        if (is_activate) {
            window.location.href = '/App/task/';
            return true;
        }
        else{
            alert('请先激活您的账户！');
            return false;
        }
    } else {
        alert('请先登录您的账户');
        return false;
    }
};