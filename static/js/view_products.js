

$(document).ready(function(){
   $.get('/api/get-available-products',(res)=>{

   
    for( key in res){
        $('#list_products_div').append("<div class='col-sm-4'> <div class='panel panel-success'><div class='panel-heading'>Title:"+res[key].title+"</div><div class='panel-body'><a href='/api/get-product/"+res[key].product_id+"'><img src='"+res[key].s3_image_url+"'class='img-responsive' style='width:100%' alt='Image'/></a></div><div class='panel-footer'>Price:"+res[key].price+"</div></div></div></div>")
         
    }

   });
   
//    <div class="col-sm-4"> 
//       <div class="panel panel-success">
//         <div class="panel-heading">BLACK FRIDAY DEAL</div>
//         <div class="panel-body"><img src="https://placehold.it/150x80?text=IMAGE" class="img-responsive" style="width:100%" alt="Image"></div>
//         <div class="panel-footer">Buy 50 mobiles and get a gift card</div>
//       </div>
//     </div>
//   </div>


    function calculatePrice(start,end,values){
            diffDays = Math.round(Math.abs((start - end)/(values)));
            price = $("#price").val();
            total_price = diffDays * price;
            $('#total_price').text(total_price);
            $('#total').val(total_price);

    };

  $("#rent_button").click(function(){
        $("#rent_modal").modal();
    });
    

    $("#datepicker_from").datepicker({
        onClose: function () {
            $("#datepicker_to").datepicker(
                "change", {
                minDate: new Date($('#datepicker_from').val())
            });
            $("#datepicker_from").datepicker({dateFormat: "mm/dd/yy"});
        }
    });

    $("#datepicker_to").datepicker({
        onClose: function () {
            $("#dateFrom").datepicker(
                "change", {
                maxDate: new Date($('#datepicker_to').val())
            });
            $("#datepicker_to").datepicker({dateFormat: "mm/dd/yy"});

        },
        onSelect: function(dateText, inst) {
           start= $("#datepicker_from").datepicker('getDate').getTime(),
            end = $("#datepicker_to").datepicker('getDate').getTime(),
            values = 24*60*60*1000,
            calculatePrice(start,end,values);
    }
    });

    $("#random_key").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".dropdown-menu li").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });
    
}); 

   




  