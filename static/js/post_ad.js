$('#form_post_ad').on('submit',(evt)=>{
    evt.preventDefault();
    
    const post_ad_form = $('#form_post_ad');

    // Create an FormData object
    const formInputs = new FormData(document.getElementById('form_post_ad'));
   
     
    $("#post_ad_button").prop("disabled", true);

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "/api/post-ad",
        data: formInputs,
        cache: false,
        processData: false,
        contentType: false,
        success: function (response) {
            console.log("SUCCESS : ", response);
            $("#post_ad_button").prop("disabled", false);
            if (response.redirect) {
                window.location.href = response.redirect;
              }

        },
        error: function (e) {

            alert(e.responseText);
            console.log("ERROR : ", e);
            $("#post_ad_button").prop("disabled", false);

        }
    });


});

$(document).ready(function(){
    $.get('/api/get-all-categories', (res) => {       
                    console.log(res)
                    for(const key in res){
                        $("#category").append("<option value='"+res[key].category_id+"'>"+res[key].category_name+"</option>");
                    }
      });
  });


