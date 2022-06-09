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

function getData2() {
    $.post('cata/123',{
        id:"4"
    },
        function (data){
        console.log(JSON.stringify(data))
    }, "json")
}

function showDetail($this){
    let id = $($this).attr("id");
    $.post('/cata/' + id,{
        id:"4"
    },
        function (data){
        $("#title_list").empty()
        for(let i=0, len=data.length; i<len; i++) {
            let pgn=$("<div style=\"text-align: right\"></div>").text(data[i][1])
            let tit=$("<li className='list-group-item'></li>").text(data[i][0])
            tit.append(pgn)
            $("#title_list").append(tit)
        }
    }, "json")
    // 这里接受注释，使用JQuery方法生成杂志目录
}



$(document).ready(function() {
	
})