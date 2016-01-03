(function () {
    $.get('/api/services', function (data) {
        var page = $('.services-page');
        page.removeClass('loading-services');

        page.empty();
        page.append(data);
    });
})();
