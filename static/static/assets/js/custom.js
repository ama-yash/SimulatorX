function switchFacial() {
    var fac_card = document.getElementById('fac-card');
    var pop_card = document.getElementById('pop-card');
    var reg_card = document.getElementById('reg-card');
    var reg_but = document.getElementById('reg-but');
    var fac_but = document.getElementById('fac-but');
    var pop_but = document.getElementById('man-but');
    pop_card.style.display = 'none';
    fac_card.style.display = 'block';
    reg_card.style.display = 'none';
    reg_but.className = 'btn btn-light';
    fac_but.className = 'btn btn-success';
    pop_but.className = 'btn btn-light';
}
function switchManual() {
    var fac_card = document.getElementById('fac-card');
    var pop_card = document.getElementById('pop-card');
    var reg_card = document.getElementById('reg-card');
    var reg_but = document.getElementById('reg-but');
    var fac_but = document.getElementById('fac-but');
    var pop_but = document.getElementById('man-but');
    reg_card.style.display = 'none';
    reg_but.className = 'btn btn-light';
    fac_card.style.display = 'none';
    pop_card.style.display = 'block';
    pop_but.className = 'btn btn-success';
    fac_but.className = 'btn btn-light';
}
