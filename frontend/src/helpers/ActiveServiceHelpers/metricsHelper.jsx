import Metrics from '../../DTOs/Metrics'

const API_BASE_URL = import.meta.env.VITE_FASTAPI_IP;

const getRecentMetrics = async (device_id) => {
  try {
    const response = await fetch(`${API_BASE_URL}/metric/get/recent/${device_id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });
    const data = await response.json();
    console.log(data.metrics)
    const metrics = data.metrics
    const calculated_metrics = metrics.calculated_metrics

    let velocity_metrics = new Metrics(calculated_metrics.top_velocity, calculated_metrics.average_velocity, 0, metrics.velocity_list)
    let acceleration_metrics = new Metrics(calculated_metrics.top_acceleration, calculated_metrics.average_acceleration, 0, metrics.acceleration_list)

    console.log(velocity_metrics, acceleration_metrics)
    return {velocity : velocity_metrics, acceleration : acceleration_metrics};
    
  } catch (error) {
    console.error('Error fetching metrics data:', error);
    return { velocity: new Metrics(), acceleration: new Metrics() };
  }
};

const pullMetrics = async (device_id) => {
  const metrics = await getRecentMetrics(device_id);
  return metrics;
};

export { pullMetrics };
