var TOTAL_CASES = 101739;
var TOTAL_DEATHS = 11591;
var TOTAL_REC = 14620;
var ACTIVE_C = 75528;
var SERIOUS = 3981;

var COUNTRY = 'Italy'

var ctx = document.getElementById('chart_statsPerCountry').getContext('2d');
var chart_statsPerCountry = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases', 'Serious Cases'],
        datasets: [{
            label: COUNTRY,
            data: [TOTAL_CASES, TOTAL_DEATHS, TOTAL_REC, ACTIVE_C, SERIOUS],
            backgroundColor: [
                'rgba(255, 99, 132, 0.4)',
                'rgba(255, 159, 64, 0.4)',
                'rgba(75, 192, 192, 0.4)',
                'rgba(255, 206, 86, 0.4)',
                'rgba(153, 102, 255, 0.4)',                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(255, 206, 86, 1)',                        
                'rgba(153, 102, 255, 1)',
            ],
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});