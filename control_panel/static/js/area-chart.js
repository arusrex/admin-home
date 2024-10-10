window.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('areaChart');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Gray'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3, 9],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});

