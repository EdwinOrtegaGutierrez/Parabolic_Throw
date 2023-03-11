// Obtener los datos del archivo pt.json
fetch('static/json/pt.json').then(response => response.json()).then(data => {
    // Crear un array con los valores de x, y
    const xValues = data.map(item => item.x);
    const yValues = data.map(item => item.y);
    
    // Crear un gráfico
    const ctx = document.getElementById('myChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xValues,
            datasets: [{
                label: 'Projectile Motion',
                data: yValues,
                borderColor: 'rgb(255, 99, 132)',
                fill: false
            }]
        },
        options: {
            scales: {
                y: {
                    title: {
                        display: true,
                        text: 'Height (m)',
                        color: 'white' // cambiar el color aquí
                    },
                    grid: {
                        color: 'transparent' // color de la línea de la fila
                    },
                    ticks: {
                        color: 'white' // cambiar el color aquí
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Horizontal distance (m)',
                        color: 'white' // cambiar el color aquí
                    },
                    grid: {
                        color: 'transparent' // color de la línea de la columna
                    },
                    ticks: {
                        color: 'white' // cambiar el color aquí
                    }
                }
            }
        }
    });    
});
