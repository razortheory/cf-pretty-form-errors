(function ($) {

    //Extend show() so that it trigger our event when called
    var show = $.fn.show;
    $.fn.show = function () {
        var ret = show.apply(this, arguments); //Read comments about these part at the stackoverflow linked above

        $(this).trigger("onShow"); //Trigger our new onShow event

        return ret; //Return object so that it can propagate
    };
    //Extend hide()
    var hide = $.fn.hide;
    $.fn.hide = function () {
        var ret = hide.apply(this, arguments); //Read comments about these part at the stackoverflow linked above

        $(this).trigger("onHide"); //Trigger our new onShow event

        return ret; //Return object so that it can propagate
    };

    //Define new event functions
    $.fn.onShow = function (callback) {
        if (callback != null) {
            $(this).on("onShow", function () {
                callback(); //Trigger callback
            });
        } else {
            $(this).trigger("onShow"); //If no callback exist we trigger the event
        }
        return this;
    };

    $.fn.onHide = function (callback) {
        if (callback != null) {
            $(this).on("onHide", function () {
                callback(); //Trigger callback
            });
        } else {
            $(this).trigger("onHide"); //If no callback exist we trigger the event
        }
        return this;
    };
})(jQuery);