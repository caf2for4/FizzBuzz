var end_target = document.getElementById('end_submit');
end_target.addEventListener('click', end_send, false);

var span_target = document.getElementById('span_submit');
span_target.addEventListener('click', span_send, false);

function end_send(){
    var num = document.getElementById('num_1_1').value;
    $.ajax({
        url: 'http://127.0.0.1:5000/execute/' + num,
        type: 'GET',
        success: function(res){
            document.getElementById('end_result').innerText = res;
        },
        error: function(xhr, status, error){
            alert(error);
        }
    })
}

function span_send(){
    var num1 = document.getElementById('num_2_1').value;
    var num2 = document.getElementById('num_2_2').value;
    $.ajax({
        url: 'http://127.0.0.1:5000/execute/json',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "start": num1, "end": num2 }),
        success: function(res){
            document.getElementById('span_result').innerHTML = res;
        },
        error: function(xhr, status, error){
            alert(error);
        }
    })
}

// jqueryらしく書く
//　エラーハンドリング、try-catch
// 一旦ソース上げる
// サーバサイドデバッグとフロントエンドデバッグを分ける
// テストの残りを書く
