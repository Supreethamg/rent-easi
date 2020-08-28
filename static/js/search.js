$(document).ready(function(){
    
    $("#searchKey").val("");
    $("#search_button").click(function(){
        formData={
            searchKey : $('#searchKey').val()};
        
        $.post("/api/search",formData,(res)=>{
            console.log(res);
            $('#list_products_div').empty();
            for( key in res){
               
                $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
                $('#list_products_div').append("<a href='/api/get-product/"+res[key].product_id+"'><img src='"+res[key].s3_image_url+"'/></a>")
            }


        });
    });

    $("#my_ads_button").click(function(){
        $.get("/api/my-ads",(res)=>{
            if (res){
                $('#list_products_div').empty();
                for( key in res){
                    $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
                    $('#list_products_div').append("<a href='#'><img src='"+res[key].s3_image_url+"'/></a>")
                }
            }
        });
    });
    

    $("#my_rentals_button").click(function(){
        $.get("/api/my-rentals",(res)=>{
            if (res){
                $('#list_products_div').empty();
                for( key in res){
                    $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
                    $('#list_products_div').append("<a href='#'><img src='"+res[key].s3_image_url+"'/></a>")
                }
            }
        });
    });

});
