async function fetchStats() {
    const res = await fetch("/stats");
    const data = await res.json();

    document.getElementById("total").innerText = data.total_logs;
    document.getElementById("anomalies").innerText = data.anomalies;
}

async function fetchLogs() {
    const res = await fetch("/logs");
    const logs = await res.json();

    const table = document.getElementById("logTable");
    table.innerHTML = "";

    let anomalyFound = false;

    logs.reverse().forEach(log => {
        if (log.anomaly == -1) anomalyFound = true;

        const row = `<tr class="${log.anomaly == -1 ? 'anomaly-row' : ''}">
            <td>${log.timestamp}</td>
            <td>${log.level}</td>
            <td>${log.message}</td>
            <td>${log.anomaly == -1 ? '🚨 ALERT' : 'Normal'}</td>
        </tr>`;
        table.innerHTML += row;
    });

    const alertBox = document.getElementById("alertBox");
    alertBox.style.display = anomalyFound ? "block" : "none";
}

const ctx = document.getElementById('chart');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Total Logs', 'Anomalies'],
        datasets: [{
            label: 'System Activity',
            data: [0,0]
        }]
    }
});

async function updateChart() {
    const res = await fetch("/stats");
    const data = await res.json();

    chart.data.datasets[0].data = [data.total_logs, data.anomalies];
    chart.update();
}

async function update() {
    await fetchStats();
    await fetchLogs();
    await updateChart();
}

setInterval(update, 2000);
update();