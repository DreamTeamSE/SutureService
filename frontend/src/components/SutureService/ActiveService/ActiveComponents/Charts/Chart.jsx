import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  TimeScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import 'chartjs-adapter-date-fns'; // Required to use date-fns adapter for date formatting
import Status from '../../DTOs/Status';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, TimeScale, LineElement, PointElement, Title, Tooltip, Legend);




const Chart = (props) => {


    let [labels, setLabels] = useState([])

    let [name, setName] = useState("VELOCITY")
    let generateLabels = () => {

        if (props.metrics) {
          console.log(props.metrics)
          const labels = props.metrics.points.map((_, index) => `2024-01-01T00:00:${String(index).padStart(2, '0')}`);
          setLabels(labels)
      }

    }

    let generateName = () => {
      console.log(props.selected)
      if (props.selected === Status.ACCELERATION) {
        setName(Status.ACCELERATION)
      }

      if (props.selected === Status.VELOCITY) {
        setName(Status.VELOCITY)
      }
    }
    useEffect(() => {
    
        generateLabels()
        generateName()
    }, [props.metrics])


  // Data and options for the chart
  const data = {
    labels: labels,
    datasets: [
      {
        label: name,
        data: props.metrics.points,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        fill: false,
      },
    ],
  };

  const options = {
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
          text: 'Velocity',
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
  };

  return (
    <div style={{ width: '100%', height: '100%' }}>
      <Line data={data} options={options} />
    </div>
  );
};

export default Chart;
