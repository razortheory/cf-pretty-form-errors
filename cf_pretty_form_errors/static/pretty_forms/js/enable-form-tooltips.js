$(document).ready(function(){
    $('[data-toggle="tooltip-help-text"]').tooltip({
        template: '<div class="tooltip tooltip-help-text" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
    });
    $('[data-toggle="tooltip-error-text"]').tooltip({
        template: '<div class="tooltip tooltip-error-text" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
    });
});