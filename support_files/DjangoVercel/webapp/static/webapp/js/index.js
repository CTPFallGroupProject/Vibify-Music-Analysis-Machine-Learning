const btn = document.getElementById('btn');
btn.addEventListener('click', (e) =>{
    const pclass = document.getElementById('pclass').value;
    const sex = document.getElementById('sex').value;
    const fare = document.getElementById('fare').value;
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        method : "POST",
        url: "/send-data",
        data: {
          'pclass' : pclass,
          'fare' : fare,
          'sex' : sex,
           csrfmiddlewaretoken : token
        },
        success: (response) =>{
          res = response
          console.log(res.status)
          if(res.status == 1){
           // window.location.href = 'show_result'
          }
        }
      })
})