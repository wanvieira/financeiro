const ctx = document.getElementById('graficoLinha');

const gradient = ctx.getContext('2d').createLinearGradient(0, 0, 0, 400);

gradient.addColorStop(0, 'rgba(124,58,237,0.8)');
gradient.addColorStop(1, 'rgba(124,58,237,0.05)');

new Chart(ctx, {

    type: 'line',

    data: {

        labels: [
            'Jan',
            'Fev',
            'Mar',
            'Abr',
            'Mai',
            'Jun'
        ],

        datasets: [{

            label: 'Faturas',

            data: [
                2000,
                3200,
                2800,
                4500,
                5200,
                4800
            ],

            borderColor: '#7c3aed',

            backgroundColor: gradient,

            fill: true,

            tension: 0.4,

            borderWidth: 4,

            pointBackgroundColor: '#ffffff',

            pointBorderColor: '#7c3aed',

            pointRadius: 6,

            pointHoverRadius: 10

        }]
    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        animation: {

            duration: 2500,

            easing: 'easeOutQuart'

        },

        plugins: {

            legend: {

                labels: {

                    color: '#ffffff',

                    font: {
                        size: 14
                    }
                }
            }
        },

        scales: {

            x: {

                ticks: {
                    color: '#cbd5e1'
                },

                grid: {
                    color: 'rgba(255,255,255,0.05)'
                }
            },

            y: {

                ticks: {
                    color: '#cbd5e1'
                },

                grid: {
                    color: 'rgba(255,255,255,0.05)'
                }
            }
        }
    }
});

const pizza = document.getElementById('graficoPizza');

new Chart(pizza, {

    type: 'doughnut',

    data: {

        labels: [
            'Casa',
            'Tecnologia',
            'Lazer',
            'Financeiro'
        ],

        datasets: [{

            data: [
                1500,
                3200,
                1200,
                5000
            ],

            backgroundColor: [
                '#7c3aed',
                '#06b6d4',
                '#ec4899',
                '#10b981'
            ],

            borderWidth: 0,

            hoverOffset: 15
        }]
    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        cutout: '70%',

        animation: {

            animateRotate: true,

            duration: 2200
        },

        plugins: {

            legend: {

                position: 'bottom',

                labels: {

                    color: '#ffffff',

                    padding: 20,

                    font: {
                        size: 13
                    }
                }
            }
        }
    }
});