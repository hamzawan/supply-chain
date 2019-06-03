$(document).ready(function(){
  count = 1

  function getCookie(c_name)
  {
      if (document.cookie.length > 0)
      {
          c_start = document.cookie.indexOf(c_name + "=");
          if (c_start != -1)
          {
              c_start = c_start + c_name.length + 1;
              c_end = document.cookie.indexOf(";", c_start);
              if (c_end == -1) c_end = document.cookie.length;
              return unescape(document.cookie.substring(c_start,c_end));
          }
      }
      return "";
   }

   $('.add-item').click(function(){
     item_description = $('#item_description').val();
     unit = $('#unit').val();
     type = $('#type').val();
     size = $('#size').val();
     opening_stock = $('#opening_stock').val();
     $.ajax({
       headers: { "X-CSRFToken": getCookie("csrftoken") },
       type: 'POST',
       url: '/inventory/add_item/',
       data:{
         item_description:item_description,
         unit: unit,
         type:type,
         size:size,
         opening_stock:opening_stock
       }
     })
     .done(function done(data){
         var index = $("table tbody tr:last-child").index();
             var row = '<tr>' +
                 '<td>'+count+'</td>' +
                 '<td><pre>'+ data.item_description +'</pre></td>' +
                 '<td>'+data.unit +'</td>'+
                 '<td>'+data.opening_stock +'</td>' +
                 '<td>'+data.size+'</td>' +
                 '<td><pre>'+data.type+'</pre></td>' +
           '<td><a class="add-item" title="Add" data-toggle="tooltip"><i class="material-icons">&#xE03B;</i></a><a class="edit-item" title="Edit" data-toggle="tooltip"><i class="material-icons">&#xE254;</i></a><a class="delete-item" title="Delete" data-toggle="tooltip"><i class="material-icons">&#xE872;</i></a></td>' +
             '</tr>';
           $("table").append(row);
         $("table tbody tr").eq(index + 1).find(".add-item, .edit-item").toggle();
             $('[data-toggle="tooltip"]').tooltip();
     });
   });


           // Add row on add button click
         $(document).on("click", ".add-item", function(){
         var empty = false;
         var input = $(this).parents("tr").find('input[type="text"]');
             input.each(function(){
           if(!$(this).val()){
             $(this).addClass("error");
             empty = true;
           }
           else{
               $(this).removeClass("error");
               }
         });
         $(this).parents("tr").find(".error").first().focus();
         if(!empty){
           input.each(function(){
             $(this).parent("td").html($(this).val());
           });
           $(this).parents("tr").find(".add-item, .edit-item").toggle();
           $(".add-new-row").removeAttr("disabled");
         }
         });

                 // Edit row on edit button click
         $(document).on("click", ".edit-item", function(){
             $(this).parents("tr").find("td:not(:last-child)").each(function(i){
             $(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
         });
             $(this).parents("tr").find(".add-item, .edit-item").toggle();
             $(".add-new-row").attr("disabled", "disabled");
         });

         // Delete row on delete button click
         $(document).on("click", ".delete-item", function(){
             var row =  $(this).closest('tr');
             var siblings = row.siblings();
             siblings.each(function(index) {
             $(this).children('td').first().text(index + 1);
             });
             $(this).parents("tr").remove();
             $(".add-new-row").removeAttr("disabled");
         });


         $('#add-item-form').on('submit',function(e){
           e.preventDefault();
           var table = $('#add-item-table');
           var data = [];

           table.find('tr').each(function (i, el){
             if(i != 0)
             {
               var $tds = $(this).find('td');
               var row = {
                 'item_description' : "",
                 'unit' : "",
                 'opening_stock' : "",
                 'type' : "",
                 'size' : "",
               };
               $tds.each(function(i, el){
                 if (i === 1) {
                   row["item_description"] = ($(this).text());
                 }
                 if (i === 2) {
                   row["unit"] = ($(this).text());
                 }
                 else if (i === 3) {
                     row["opening_stock"] = ($(this).text());
                 }
                 else if (i === 4) {
                     row["type"] = ($(this).text());
                 }
                 else if (i === 5) {
                     row["size"] = ($(this).text());
                 }
               });
               data.push(row);
             }
           });

              req =	$.ajax({
                 headers: { "X-CSRFToken": getCookie("csrftoken") },
                 type: 'POST',
                 url : '/inventory/add_item/',
                 data:{
                   'items': JSON.stringify(data),
                 },
                 dataType: 'json'
               })
               .done(function done(){
                 alert("Item Added");
                 location.reload();
               })
         });


})
