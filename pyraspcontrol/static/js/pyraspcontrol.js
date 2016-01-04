(function () {

    function indexCtrl() {
        var ipAddress;
        return $.get('/api/network-ip').then(function (data) {
            ipAddress = data.ip || 'N/A';
        }).always(function () {
             $('.external-ip-loader').hide();

            var ipNode = $('.external-ip');
            ipNode.text(ipAddress || 'N/A');
            ipNode.show();
        });
    }

    function serviceCtrl() {
        return $.get('/api/services').then(function (data) {
            var page = $('.services-page');
            page.removeClass('loading-services');

            page.empty();
            page.append(data);
        });
    }

    /* 1-1 mapping between page controllers and the `location.pathname`. */
    var _controllers = {
        '/':        indexCtrl,
        'services': serviceCtrl
    };
    return _controllers[window.location.pathname]();

})();
