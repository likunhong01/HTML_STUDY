(function (arg) {
    var status = 1; // 全局变量

    // 封装变量
    arg.extend({
        'lkk': function () {
            return 'lkk';
        }
    });
})(JQuery);