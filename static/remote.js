var event;
var attendQuery;

$(document).ready(function () {
    //docReady();
});

function clickedOp(service_id, op)
{
    $.ajax({url:'/service/' + service_id + '/' + op});
}


