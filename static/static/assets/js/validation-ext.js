function hideRecoveryParameters(){
    var obj = document.getElementById('rec-card');
    obj.style.display = 'none';
}
function showRecoveryParameters(){
    var obj = document.getElementById('rec-card');
    obj.style.display = 'block';    
}

function validateFormExt(){
    var val_form = validateForm();
    var white_inf = document.getElementById('white_inf').value;
    var black_inf = document.getElementById('black_inf').value;
    var asian_inf = document.getElementById('asian_inf').value;
    var other_inf = document.getElementById('other_inf').value;
    var male_inf = document.getElementById('male_inf').value;
    var female_inf = document.getElementById('female_inf').value;
    var child_inf = document.getElementById('child_inf').value;
    var adult_inf = document.getElementById('adult_inf').value;
    var senior_inf = document.getElementById('senior_inf').value;
    var rad_si = document.getElementById('si_model');
    if(rad_si.checked == false){
        var white_rec = document.getElementById('white_rec').value;
        var black_rec = document.getElementById('black_rec').value;
        var asian_rec = document.getElementById('asian_rec').value;
        var other_rec = document.getElementById('other_rec').value;
        var male_rec = document.getElementById('male_rec').value;
        var female_rec = document.getElementById('female_rec').value;
        var child_rec = document.getElementById('child_rec').value;
        var adult_rec = document.getElementById('adult_rec').value;
        var senior_rec = document.getElementById('senior_rec').value;
    }
   var white_inf_check = validateWhiteInf(white_inf);
   var black_inf_check = validateBlackInf(black_inf);
   var asian_inf_check = validateAsianInf(asian_inf);
   var other_inf_check = validateOtherInf(other_inf);
   var male_inf_check = validateMaleInf(male_inf);
   var female_inf_check = validateFemaleInf(female_inf);
   var child_inf_check = validateChildInf(child_inf);
   var adult_inf_check = validateAdultInf(adult_inf);
   var senior_inf_check = validateSeniorInf(senior_inf);
   if(rad_si.checked == true)
   {
        if(val_form && white_inf_check && black_inf_check && asian_inf_check && other_inf_check && male_inf_check && female_inf_check && child_inf_check && adult_inf_check && senior_inf_check){
            return true;
        }
        else{
            return false;
        }
   }
   else{
        var white_rec_check = validateWhiteRec(white_rec);
        var black_rec_check = validateBlackRec(black_rec);
        var asian_rec_check = validateAsianRec(asian_rec);
        var other_rec_check = validateOtherRec(other_rec);
        var male_rec_check = validateMaleRec(male_rec);
        var female_rec_check = validateFemaleRec(female_rec);
        var child_rec_check = validateChildRec(child_rec);
        var adult_rec_check = validateAdultRec(adult_rec);
        var senior_rec_check = validateSeniorRec(senior_rec);
        if(val_form && white_inf_check && black_inf_check && asian_inf_check && other_inf_check && male_inf_check && female_inf_check && child_inf_check && adult_inf_check && senior_inf_check && white_rec_check && black_rec_check && asian_rec_check && other_rec_check && male_rec_check && female_rec_check && child_rec_check && adult_rec_check && senior_rec_check){
            return true;
        }
        else{
            return false;
        }
   }
   
}

function validateWhiteInf(white_inf){
    if(white_inf == ''){
        var obj = document.getElementById('white_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('white_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(white_inf)){
        var obj = document.getElementById('white_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('white_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(white_inf > 1){
        var obj = document.getElementById('white_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('white_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateBlackInf(black_inf){
    if(black_inf == ''){
        var obj = document.getElementById('black_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('black_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(black_inf)){
        var obj = document.getElementById('black_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('black_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(black_inf > 1){
        var obj = document.getElementById('black_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('black_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAsianInf(asian_inf){
    if(asian_inf == ''){
        var obj = document.getElementById('asian_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('asian_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(asian_inf)){
        var obj = document.getElementById('asian_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('asian_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(asian_inf > 1){
        var obj = document.getElementById('asian_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('asian_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateOtherInf(other_inf){
    if(other_inf == ''){
        var obj = document.getElementById('other_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('other_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(other_inf)){
        var obj = document.getElementById('other_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('other_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(other_inf > 1){
        var obj = document.getElementById('other_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('other_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateMaleInf(male_inf){
    if(male_inf == ''){
        var obj = document.getElementById('male_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('male_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(male_inf)){
        var obj = document.getElementById('male_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('male_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(male_inf > 1){
        var obj = document.getElementById('male_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('male_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateFemaleInf(female_inf){
    if(female_inf == ''){
        var obj = document.getElementById('female_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('female_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(female_inf)){
        var obj = document.getElementById('female_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('female_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(female_inf > 1){
        var obj = document.getElementById('female_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('female_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateChildInf(child_inf){
    if(child_inf == ''){
        var obj = document.getElementById('child_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('child_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(child_inf)){
        var obj = document.getElementById('child_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('child_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(child_inf > 1){
        var obj = document.getElementById('child_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('child_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAdultInf(adult_inf){
    if(adult_inf == ''){
        var obj = document.getElementById('adult_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('adult_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(adult_inf)){
        var obj = document.getElementById('adult_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('adult_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(adult_inf > 1){
        var obj = document.getElementById('adult_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('adult_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateSeniorInf(senior_inf){
    if(senior_inf == ''){
        var obj = document.getElementById('senior_inf_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('senior_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(senior_inf)){
        var obj = document.getElementById('senior_inf_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('senior_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(senior_inf > 1){
        var obj = document.getElementById('senior_inf_alert').innerText = 'The infection rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('senior_inf_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateWhiteRec(white_rec){
    if(white_rec == ''){
        var obj = document.getElementById('white_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('white_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(white_rec)){
        var obj = document.getElementById('white_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('white_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(white_rec > 1){
        var obj = document.getElementById('white_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('white_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateBlackRec(black_rec){
    if(black_rec == ''){
        var obj = document.getElementById('black_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('black_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(black_rec)){
        var obj = document.getElementById('black_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('black_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(black_rec > 1){
        var obj = document.getElementById('black_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('black_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAsianRec(asian_rec){
    if(asian_rec == ''){
        var obj = document.getElementById('asian_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('asian_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(asian_rec)){
        var obj = document.getElementById('asian_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('asian_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(asian_rec > 1){
        var obj = document.getElementById('asian_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('asian_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateOtherRec(other_rec){
    if(other_rec == ''){
        var obj = document.getElementById('other_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('other_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(other_rec)){
        var obj = document.getElementById('other_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('other_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(other_rec > 1){
        var obj = document.getElementById('other_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('other_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateMaleRec(male_rec){
    if(male_rec == ''){
        var obj = document.getElementById('male_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('male_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(male_rec)){
        var obj = document.getElementById('male_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('male_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(male_rec > 1){
        var obj = document.getElementById('male_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('male_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateFemaleRec(female_rec){
    if(female_rec == ''){
        var obj = document.getElementById('female_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('female_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(female_rec)){
        var obj = document.getElementById('female_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('female_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(female_rec > 1){
        var obj = document.getElementById('female_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('female_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateChildRec(child_rec){
    if(child_rec == ''){
        var obj = document.getElementById('child_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('child_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(child_rec)){
        var obj = document.getElementById('child_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('child_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(child_rec > 1){
        var obj = document.getElementById('child_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('child_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAdultRec(adult_rec){
    if(adult_rec == ''){
        var obj = document.getElementById('adult_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('adult_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(adult_rec)){
        var obj = document.getElementById('adult_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('adult_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(adult_rec > 1){
        var obj = document.getElementById('adult_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('adult_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateSeniorRec(senior_rec){
    if(senior_rec == ''){
        var obj = document.getElementById('senior_rec_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('senior_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(senior_rec)){
        var obj = document.getElementById('senior_rec_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('senior_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(senior_rec > 1){
        var obj = document.getElementById('senior_rec_alert').innerText = 'The recovery rate MUST NOT be more than 1.0';
        var obj2 = document.getElementsByName('senior_rec_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
