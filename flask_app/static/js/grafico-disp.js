Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Número de dispositivos por tipo'
    },
    xAxis: {
        categories: ["Pantalla", "Notebook", "Tablet", "Celular", "Consola", "Mouse", "Teclado", "Impresora", "Parlante", "Audifonos", "Otro"],
        title: {
            text: 'Tipo del dispositivo'
        }
    },
    yAxis: {
        title: {
            text: 'Número de dispositivos registrados'
        },
        tickInterval: 1 // Ensures only integer ticks
    },
    series: [{ 
        data: [], // Replace with your actual data
        showInLegend: false
    }]
});

fetch("http://127.0.0.1:5000/get-grafico-tipo-disp")
.then((response) => response.json())
.then((data) => {
    const seriesData = data.map(item => item.num_disp); // y-axis data
   
    // Get the chart by ID
    const chart = Highcharts.charts.find(
        (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new categories and data
    chart.update({
        series: [
        {
            data: seriesData // y-axis data for each comuna
        },
        ],
        
    });
})
.catch((error) => console.error("Error:", error));