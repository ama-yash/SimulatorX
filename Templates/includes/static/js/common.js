function switchFacial() {
  var fac_card = document.getElementById("fac-card");
  var pop_card = document.getElementById("pop-card");
  var reg_card = document.getElementById("reg-card");
  var reg_but = document.getElementById("reg-but");
  var fac_but = document.getElementById("fac-but");
  var pop_but = document.getElementById("man-but");
  pop_card.style.display = "none";
  fac_card.style.display = "block";
  reg_card.style.display = "none";
  reg_but.className = "btn btn-light";
  fac_but.className = "btn btn-success";
  pop_but.className = "btn btn-light";
}
function switchManual() {
  var fac_card = document.getElementById("fac-card");
  var pop_card = document.getElementById("pop-card");
  var reg_card = document.getElementById("reg-card");
  var reg_but = document.getElementById("reg-but");
  var fac_but = document.getElementById("fac-but");
  var pop_but = document.getElementById("man-but");
  reg_card.style.display = "none";
  reg_but.className = "btn btn-light";
  fac_card.style.display = "none";
  pop_card.style.display = "block";
  pop_but.className = "btn btn-success";
  fac_but.className = "btn btn-light";
}
function switchRegional() {
  var fac_card = document.getElementById("fac-card");
  var pop_card = document.getElementById("pop-card");
  var reg_card = document.getElementById("reg-card");
  var reg_but = document.getElementById("reg-but");
  var fac_but = document.getElementById("fac-but");
  var pop_but = document.getElementById("man-but");
  reg_card.style.display = "block";
  reg_but.className = "btn btn-success";
  fac_card.style.display = "none";
  pop_card.style.display = "block";
  pop_but.className = "btn btn-light";
  fac_but.className = "btn btn-light";
}


function getDemographyData() {
  var id = document.getElementById('region').value;
  $.ajax({
      url: '/semi-auto/get_data',
      type: 'POST',
      data: {
          id: id,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function (data) {
          var n_obj = document.getElementById('pop_size').value = data.population;
          var white = document.getElementById('white').value = data.white;
          var black = document.getElementById('black').value = data.black;
          var asian = document.getElementById('asian').value = data.asian;
          var other = document.getElementById('other').value = data.other;
          var male = document.getElementById('male').value = data.male;
          var female = document.getElementById('female').value = data.female;
          var child = document.getElementById('child').value = data.child;
          var adult = document.getElementById('adult').value = data.adult;
          var senior = document.getElementById('senior').value = data.senior;
      }
  })
}

function uploadImages() {
  var len = $('#my_form input[type=file]').get(0).files.length;
  if (len < 10) {
      var obj2 = document.getElementById('upload_alert').innerText = 'Minimum 10 image files MUST be uploaded.'
      var obj = document.getElementsByName('upload_alert');
      obj[0].style.display = 'block';
  } else {
      var obj = document.getElementsByName('upload_alert');
      obj[0].style.display = 'none';
      var form = document.getElementById('my_form');
      var alertobj = document.getElementById('alertbox');
      alertobj.style.display = 'block';
      $.ajax({
          type: 'POST',
          url: '/facial-recognition',
          data: new FormData(form),
          processData: false,
          contentType: false,
          success: function (data) {
              var alertobj = document.getElementById('alertbox');
              alertobj.style.display = 'none';
              var msg_obj = document.getElementById('msg').style.display = 'block';
              var n_obj = document.getElementById('fr_n').innerHTML = 'N: '.concat(data.N);
              var w_obj = document.getElementById('fr_white').innerHTML = 'White: '.concat(data.white);
              var b_obj = document.getElementById('fr_black').innerHTML = 'Black: '.concat(data.black);
              var a_obj = document.getElementById('fr_asian').innerHTML = 'Asian: '.concat(data.asian);
              var o_obj = document.getElementById('fr_other').innerHTML = 'Other: '.concat(data.other);
              var m_obj = document.getElementById('fr_male').innerHTML = 'Male: '.concat(data.male);
              var f_obj = document.getElementById('fr_female').innerHTML = 'Female: '.concat(data.female);
              var ch_obj = document.getElementById('fr_child').innerHTML = 'Child: '.concat(data.child);
              var ad_obj = document.getElementById('fr_adult').innerHTML = 'Adult: '.concat(data.adult);
              var s_obj = document.getElementById('fr_senior').innerHTML = 'Senior: '.concat(data.senior);
              var pop_obj = document.getElementById('pop_size').value = data.N;
              var white = document.getElementById('white').value = data.white;
              var black = document.getElementById('black').value = data.black;
              var asian = document.getElementById('asian').value = data.asian;
              var other = document.getElementById('other').value = data.other;
              var male = document.getElementById('male').value = data.male;
              var female = document.getElementById('female').value = data.female;
              var child = document.getElementById('child').value = data.child;
              var adult = document.getElementById('adult').value = data.adult;
              var senior = document.getElementById('senior').value = data.senior;
          }
      })
  }
}