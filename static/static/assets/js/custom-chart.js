function getTotalInfectionData(){
    var inf = '{{data.inf_total}}'.split(',').map(function(item){return parseInt(item, 10);});
    var labels = [];
    for (i = 1; i <= inf.length; i++) {
       labels.push(i);
    }
    const data = {
       labels: labels,
       datasets: [{
          label: 'Infected',
          data: inf,
          fill: false,
          borderColor: 'blue',
          tension: 0.1
       }]
    };
    return data;
 }
 function getTotalInfectionConfig(){
    const config = {
       type: 'line',
       data: getTotalInfectionData(),
       options: getOptions()
    };
    return config;
 }
 var myTotalInfectionChart = new Chart(
    document.getElementById('Total_Infection'),
    getTotalInfectionConfig()
 );