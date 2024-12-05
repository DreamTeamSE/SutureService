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
import 'chartjs-adapter-date-fns';
import Status from '../../../../../DTOs/Status';
import { getChartData, getChartOptions } from './chartConfig';
import { generateTimeLabels, getChartName } from './chartUtils';

ChartJS.register(
  CategoryScale,
  LinearScale,
  TimeScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
);

const Chart = ({ metrics, selected }) => {
  const [labels, setLabels] = useState([]);
  const [name, setName] = useState(Status.VELOCITY);

  useEffect(() => {
    if (metrics) {
      setLabels(generateTimeLabels(metrics));
      setName(getChartName(selected, Status));
    }
  }, [metrics, selected]);

  return (
    <div style={{ width: '100%', height: '100%' }}>
      <Line 
        data={getChartData(labels, metrics, name)} 
        options={getChartOptions(name)} 
      />
    </div>
  );
};

export default Chart;
