(function () {
    $.get('/api/network-ip', function (data) {
        $('.external-ip-loader').hide();

        var ipNode = $('.external-ip');
        ipNode.text(data.ip || 'N/A');
        ipNode.show();
    });
})();
