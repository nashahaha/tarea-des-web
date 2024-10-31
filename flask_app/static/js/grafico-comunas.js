Highcharts.chart('container', {
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Número de dispositivos registrados por comuna'
    },
    xAxis: {
        categories: [],
        title: {
            text: 'Comuna'
        }
    },
    yAxis: {
        title: {
            text: 'Número de dispositivos registrados'
        },
        tickInterval: 1, // Ensures only integer ticks
        labels: {
            formatter: function () {
                return Math.floor(this.value); // Forces integer display
            }
        }
    },
    series: [{
        data: [] // Replace with your actual data
    }]
});

fetch("http://127.0.0.1:5000/get-grafico-comunas")
.then((response) => response.json())
.then((data) => {
    const categories = data.map(item => item.comuna);  // x-axis labels
    const seriesData = data.map(item => item.num_disp); // y-axis data
    print(seriesData)
    // Get the chart by ID
    const chart = Highcharts.charts.find(
        (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new categories and data
    chart.update({
        xAxis: [
        {
            categories: categories, // Set x-axis categories to comuna names
        }
        ],
        series: [
        {
            data: seriesData, // y-axis data for each comuna
        },
        ],
        
    });
})
.catch((error) => console.error("Error:", error));