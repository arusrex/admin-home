window.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('areaChart');

    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Gray'],
                datasets: [{
                    label: '# of Votes',
                    // backgroundColor:"rgba(0,0,255,1.0)",
                    // borderColor: "rgba(0,0,255,0.1)",
                    data: [12, 19, 3, 5, 2, 3, 9],
                    borderWidth: 1,
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
    };
});

