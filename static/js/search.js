$(document).ready(function(){
    
    $("#searchKey").val("");
    $("#search_button").click(function(){
        formData={
            searchKey : $('#searchKey').val()};
        
        $.post("/api/search",formData,(res)=>{
            console.log(res);
            $('#list_products_div').empty();
            $('#page_heading').html("");
            for( key in res){
               
                // $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
                // $('#list_products_div').append("<a href='/api/get-product/"+res[key].product_id+"'><img src='"+res[key].s3_image_url+"'/></a>")
                $('#list_products_div').append("<div class='col-md-3 col-sm-6'>"+
                        "<div class='product-grid4'>"+
                  "<div class='product-image4'>"+
                       "<a href='/api/get-product/"+res[key].product_id+"'>"+
                            "<img class='pic-1' src='"+res[key].s3_image_url+"' />"+
                        "</a>"+
                    "</div>"+
                 "<div class='product-contents'>"+
                     "<h3 class='title'><a href='/api/get-product/"+res[key].product_id+"' class='product-name'>"+res[key].title+"</a></h3>"+
                        "<div class='price'>"+
                       
                         "<span class='product-price'><small>$&nbsp</small>"+res[key].price+" &nbsp<small>/day</small></span>"+
                     "</div>"+
                        "<a class='add-to-cart' href='/api/get-product/"+res[key].product_id+"'>RENT THIS</a>"+
                 " </div>"+
                "</div>");
            }


        });
    });
    $("#home_button_user").click(function(){
        window.location.href="/api/home"
    });

    $("#my_ads_button").click(function(){
        $.get("/api/my-ads",(res)=>{
            if (res){
                $('#list_products_div').empty();
                $('#page_heading').html("MY ADS");
                for( key in res){
                    // $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
                    // $('#list_products_div').append("<a href='#'><img src='"+res[key].s3_image_url+"'/></a>")
                    $('#list_products_div').append("<div class='col-md-3 col-sm-6'>"+
                        "<div class='product-grid4'>"+
                  "<div class='product-image4'>"+
                       "<a href='/api/get-product/"+res[key].product_id+"'>"+
                            "<img class='pic-1' src='"+res[key].s3_image_url+"' />"+
                        "</a>"+
                    "</div>"+
                 "<div class='product-contents'>"+
                     "<h3 class='title'><a href='/api/get-product/"+res[key].product_id+"' class='product-name'>"+res[key].title+"</a></h3>"+
                        "<div class='price'>"+
                       
                         "<span class='product-price'><small>$&nbsp</small>"+res[key].price+" &nbsp<small>/day</small></span>"+
                     "</div>"+
                        
                 " </div>"+
                "</div>");
                }
            }
        });
    });
    

    $("#my_rentals_button").click(function(){
        $.get("/api/my-rentals",(res)=>{
            if (res){
                $('#list_products_div').empty();
                $('#page_heading').html("MY RENTALS");
                for( key in res){
                    // $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
                    // $('#list_products_div').append("<a href='#'><img src='"+res[key].s3_image_url+"'/></a>")
                    $('#list_products_div').append("<div class='col-md-3 col-sm-6'>"+
                        "<div class='product-grid4'>"+
                  "<div class='product-image4'>"+
                       "<a href='/api/get-product/"+res[key].product_id+"'>"+
                            "<img class='pic-1' src='"+res[key].s3_image_url+"' />"+
                        "</a>"+
                    "</div>"+
                 "<div class='product-contents'>"+
                     "<h3 class='title'><a href='/api/get-product/"+res[key].product_id+"' class='product-name'>"+res[key].title+"</a></h3>"+
                        "<div class='price'>"+
                       
                         "<span class='product-price'><small>$&nbsp</small>"+res[key].price+" &nbsp<small>/day</small></span>"+
                     "</div>"+
                       
                 " </div>"+
                "</div>");
                }
            }
        });
    });

});
