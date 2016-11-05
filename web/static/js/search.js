

function search_options(){
    var options = {
	ajax: true,
	url: "/api/search.json",
	multiSelect: true,
	selection: false,
	rowSelect: false,
	multiSort: false,
	navigation: 2,
	ajaxSettings: {
	    method: "GET",
	    cache: false
	},
	post: function ()
	{
	    var values = {};
	    $.each($('#mbform').serializeArray(), function(i, field) {
		    values[field.name] = field.value;
		});
	    
	    return values;
	},

    };
    return options;
}

var options = search_options();
$("#grid-data").bootgrid( options );