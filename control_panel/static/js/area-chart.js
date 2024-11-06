window.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('areaChart');

    const data = {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            backgroundColor:"rgba(13, 110, 253, 0.4)",
            borderColor: "rgba(0, 0, 255, 1)",
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
            borderRadius: 5,
            fill: true,
            tension: 0.2,
        }]
    };

    const options = {
        resposive: true,
        plugins: {
            title: {
                display: true,
                text: 'Chart.js Line Chart',
            },
            legend: {
                display: true, // Exibe a legenda
                position: 'top'
            },
            tooltip: {
                enabled: true // Exibe tooltip ao passar o mouse
            },
            colors: {
                enabled: false,
                forceOverride: true
            }
        },
        scales: {
            x: {                     // Configurações do eixo X
                title: {
                    display: true,
                    text: '(Meses)'
                },
                beginAtZero: true
            },
            y: {                     // Configurações do eixo Y
                title: {
                    display: true,
                    text: 'Quantidade de Vendas'
                },
                beginAtZero: true
            }
        },
    };

    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data,
            options,
        });
    };
});

