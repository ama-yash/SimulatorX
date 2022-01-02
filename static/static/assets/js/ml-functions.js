function postImage(){
    var len = $('#ml input[type=file]').get(0).files.length;
    if(len!=0){
       var form = document.getElementById('ml');
       var alertobj = document.getElementById('alertbox');
       alertobj.style.display = 'block';
       $.ajax({
          type:'POST',
          url:'/facial-recognition/predict',
          data: new FormData(form),
          processData:false,
          contentType:false,
          success:function(data){
             var alertobj = document.getElementById('alertbox');
             alertobj.style.display = 'none';
             if(data.gen == 0){
                var obj = document.getElementById('gender');
                obj.value = 0;
             }
             else{
                var obj = document.getElementById('gender');
                obj.value = 1;
             }
             if(data.eth == 0){
                var obj = document.getElementById('ethnicity');
                obj.value = 0;
             }
             else if(data.eth == 1){
                var obj = document.getElementById('ethnicity');
                obj.value = 1;
             }
             else if(data.eth == 2){
                var obj = document.getElementById('ethnicity');
                obj.value = 2;
             }
             else if(data.eth == 3){
                var obj = document.getElementById('ethnicity');
                obj.value = 3;
             }
             switch(data.age){
                case 0:
                   var obj = document.getElementById('age');
                   obj.value = 2;
                   break;
                case 1:
                   var obj = document.getElementById('age');
                   obj.value = 7;
                   break;
                case 2:
                   var obj = document.getElementById('age');
                   obj.value = 12;
                   break;
                case 3:
                   var obj = document.getElementById('age');
                   obj.value = 17;
                   break;
                case 4:
                   var obj = document.getElementById('age');
                   obj.value = 22;
                   break;
                case 5:
                   var obj = document.getElementById('age');
                   obj.value = 27;
                   break;
                case 6:
                   var obj = document.getElementById('age');
                   obj.value = 32;
                   break;
                case 7:
                   var obj = document.getElementById('age');
                   obj.value = 37;
                   break;
                case 8:
                   var obj = document.getElementById('age');
                   obj.value = 42;
                   break;
                case 9:
                   var obj = document.getElementById('age');
                   obj.value = 47;
                   break;
                case 10:
                   var obj = document.getElementById('age');
                   obj.value = 52;
                   break;
                case 11:
                   var obj = document.getElementById('age');
                   obj.value = 57;
                   break;
                case 12:
                   var obj = document.getElementById('age');
                   obj.value = 62;
                   break;
                case 13:
                   var obj = document.getElementById('age');
                   obj.value = 67;
                   break;
                case 14:
                   var obj = document.getElementById('age');
                   obj.value = 72;
                   break;
                case 15:
                   var obj = document.getElementById('age');
                   obj.value = 77;
                   break;
             }
          }
       })
    }
 }