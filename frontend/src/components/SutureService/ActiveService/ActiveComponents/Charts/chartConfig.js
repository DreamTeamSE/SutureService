import Status from '../../../../../DTOs/Status';

export const getChartData = (labels, metrics, name) => {
  if (!metrics || !metrics.points) return { labels: [], datasets: [] };
  
  return {
    labels,
    datasets: [
      {
        label: name,
        data: metrics.points,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        fill: false,
      },
    ],
  };
};

export const getChartOptions = (name) => ({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      type: 'time',
      time: {
        unit: 'second',
        displayFormats: {
          second: 'mm:ss',
        },
        tooltipFormat: 'HH:mm:ss',
      },
      title: {
        display: true,
        text: 'Time (seconds)',
      },
    },
    y: {
      title: {
        display: true,
        text: name === Status.VELOCITY ? 'Velocity (mm/s)' : 'Acceleration (mm/s²)',
      },
    },
  },
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: `${name} CHART`,
    },
  },
}); 