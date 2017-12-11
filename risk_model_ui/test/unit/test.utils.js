import jQuery from 'jquery';

window.jQuery = jQuery;
window.$ = jQuery;

window.minify = function(html) {
  return html.replace(/>\s+</g, '><');
}

window.removeAllData = function(object) {
    var jqo = $(object);
    var data = {};

    jqo.find('*').each(function(i, o) { data = Object.assign(data, $(o).data()); });
    $.each(data, function(k, v) { jqo.find('*').removeAttr("data-" + k); });
    return jqo;
}

window.removeClass = function(object) {
    var jqo = $(object);
    jqo.find('*').removeAttr("class");
    return jqo;
}