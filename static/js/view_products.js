

$(document).ready(function(){
   $.get('/api/get-available-products',(res)=>{

   
    for( key in res){
        $('#list_products_div').append("<div><div>"+res[key].title+"</div><div>"+res[key].description+"</div></div>")
         $('#list_products_div').append("<a href='/api/get-product/"+res[key].product_id+"'><img src='"+res[key].s3_image_url+"'/></a>")
    }

   });
   }); 

   




  