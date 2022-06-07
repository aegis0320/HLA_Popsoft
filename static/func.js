function login(text) {
    alert(text);
}

function getData() {
    $.post('data/test',{
        id:"4"
    },
        function (data){
        console.log(data.name);
        console.log(JSON.stringify(data))
    }, "json")
}

$(document).ready(function() {
	
})