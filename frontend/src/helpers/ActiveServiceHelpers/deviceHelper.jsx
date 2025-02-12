import Metrics from '../../DTOs/Metrics'

const API_BASE_URL = import.meta.env.VITE_FASTAPI_IP;

const start = async (device_id) => {
  try {
    const response = await fetch(`${API_BASE_URL}/device/control`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: "maxmartin54321@gmail.com",
            control: "start",
            device_id: device_id
        })
    });
  } catch (error) {
    console.error('Error fetching metrics data:', error);
  }
};

const stop = async (device_id) => {
  try {
    const response = await fetch(`${API_BASE_URL}/device/control`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: "maxmartin54321@gmail.com",
            control: "stop",
            device_id: device_id
        })
    });
  } catch (error) {
    console.error('Error fetching metrics data:', error);
  }
};

export { start, stop };
