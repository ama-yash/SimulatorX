function hideMyAlert(id){
    var obj = document.getElementsByName(id);
    obj[0].style.display = 'none';
    if(id=='male_alert' || id=='female_alert'){
        var obj = document.getElementsByName('gender_alert');
        obj[0].style.display = 'none';
    }
    if (id == 'white_alert' || id == 'black_alert' || id == 'asian_alert' || id == 'other_alert'){
        var obj = document.getElementsByName('ethnicity_alert');
        obj[0].style.display = 'none';
    }
    if (id == 'child_alert' || id == 'adult_alert' || id == 'senior_alert'){
        var obj = document.getElementsByName('age_alert');
        obj[0].style.display = 'none';
    }
}
function validateForm(){
    var pop_size = document.getElementById('pop_size').value;
    var male = document.getElementById('male').value;
    var female = document.getElementById('female').value;
    var white = document.getElementById('white').value;
    var black = document.getElementById('black').value;
    var asian = document.getElementById('asian').value;
    var other = document.getElementById('other').value;
    var child = document.getElementById('child').value;
    var adult = document.getElementById('adult').value;
    var senior = document.getElementById('senior').value;
    var time = document.getElementById('time').value;
    var seeds = document.getElementById('seeds').value;
    var pop_size_check = validatePopSize(pop_size);
    var male_check = validateMale(male);
    var female_check = validateFemale(female);
    var gender_sum_check = validateGenderSum(male,female);
    var white_check = validateWhite(white);
    var black_check = validateBlack(black);
    var asian_check = validateAsian(asian);
    var other_check = validateOther(other);
    var ethnicity_sum_check = validateEthnicitySum(white,black,asian,other);
    var child_check = validateChild(child);
    var adult_check = validateAdult(adult);
    var senior_check = validateSenior(senior);
    var age_group_sum_check = validateAgeGroupSum(child,adult,senior);
    var time_check = validateTime(time);
    var seeds_check = validateSeeds(seeds);
    if(pop_size_check && male_check && female_check && gender_sum_check && white_check && black_check && asian_check && other_check && ethnicity_sum_check && child_check && adult_check && senior_check && age_group_sum_check && time_check && seeds_check){
        return true;
    }
    else{
        return false;
    }
}

function validatePopSize(pop_size){
    if(pop_size == ''){
        var obj = document.getElementById('pop_size_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('pop_size_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(pop_size)){
        var obj = document.getElementById('pop_size_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('pop_size_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateMale(male){
    if(male == ''){
        var obj = document.getElementById('male_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('male_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(male)){
        var obj = document.getElementById('male_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('male_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(male > 100){
        var obj = document.getElementById('male_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('male_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateFemale(female){
    if(female == ''){
        var obj = document.getElementById('female_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('female_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(female)){
        var obj = document.getElementById('female_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('female_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(female > 100){
        var obj = document.getElementById('female_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('female_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateGenderSum(male,female){
    var sumGen = (parseFloat(male)+parseFloat(female))
    if( sumGen.toFixed(2) != 100){
        var obj = document.getElementById('gender_alert').innerText = 'The sum of gender groups MUST be equal to 100.';
        var obj2 = document.getElementsByName('gender_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateWhite(white){
    if(white == ''){
        var obj = document.getElementById('white_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('white_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(white)){
        var obj = document.getElementById('white_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('white_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(white > 100){
        var obj = document.getElementById('white_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('white_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateBlack(black){
    if(black == ''){
        var obj = document.getElementById('black_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('black_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(black)){
        var obj = document.getElementById('black_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('black_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(black > 100){
        var obj = document.getElementById('black_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('black_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAsian(asian){
    if(asian == ''){
        var obj = document.getElementById('asian_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('asian_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(asian)){
        var obj = document.getElementById('asian_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('asian_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(asian > 100){
        var obj = document.getElementById('asian_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('asian_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateOther(other){
    if(other == ''){
        var obj = document.getElementById('other_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('other_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(other)){
        var obj = document.getElementById('other_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('other_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(other > 100){
        var obj = document.getElementById('other_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('other_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateEthnicitySum(white,black,asian,other){
    var sumEth = (parseFloat(white)+parseFloat(black)+parseFloat(asian)+parseFloat(other));
    if(sumEth.toFixed(2) != 100){
        var obj = document.getElementById('ethnicity_alert').innerText = 'The sum of ethnic groups MUST be equal to 100.';
        var obj2 = document.getElementsByName('ethnicity_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateChild(child){
    if(child == ''){
        var obj = document.getElementById('child_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('child_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(child)){
        var obj = document.getElementById('child_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('child_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(child > 100){
        var obj = document.getElementById('child_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('child_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAdult(adult){
    if(adult == ''){
        var obj = document.getElementById('adult_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('adult_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(adult)){
        var obj = document.getElementById('adult_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('adult_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(adult > 100){
        var obj = document.getElementById('adult_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('adult_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateSenior(senior){
    if(senior == ''){
        var obj = document.getElementById('senior_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('senior_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(senior)){
        var obj = document.getElementById('senior_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('senior_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(other > 100){
        var obj = document.getElementById('senior_alert').innerText = 'The ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('senior_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateAgeGroupSum(child,adult,senior){
    var sumAge = (parseFloat(child)+parseFloat(adult)+parseFloat(senior));
    if( sumAge.toFixed(2) != 100){
        var obj = document.getElementById('age_alert').innerText = 'The sum of age groups MUST be equal to 100.';
        var obj2 = document.getElementsByName('age_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
function validateTime(time){
    if(time == ''){
        var obj = document.getElementById('time_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('time_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(time)){
        var obj = document.getElementById('time_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('time_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}

function validateSeeds(seeds){
    if(seeds == ''){
        var obj = document.getElementById('seeds_alert').innerText = 'This field MUST NOT be null.';
        var obj2 = document.getElementsByName('seeds_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(isNaN(seeds)){
        var obj = document.getElementById('seeds_alert').innerText = 'This field MUST ONLY CONTAIN numbers.';
        var obj2 = document.getElementsByName('seeds_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else if(Number(seeds) > 100){
        var obj = document.getElementById('seeds_alert').innerText = 'The seeds ratio MUST NOT be more than 100.';
        var obj2 = document.getElementsByName('seeds_alert');
        obj2[0].style.display  = 'block';
        return false;
    }
    else{
        return true;
    }
}
