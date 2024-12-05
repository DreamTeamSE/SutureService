import Metrics from '../../DTOs/Metrics'

const API_BASE_URL = import.meta.env.VITE_FASTAPI_IP;

const pullVelocity = async () => {
  try {
    console.log(API_BASE_URL)
    const response = await fetch(`${API_BASE_URL}/recent/velocity`);
    const data = await response.json();
    return new Metrics(data.top, data.average, data.errors, data.points);
  } catch (error) {
    
    console.error('Error fetching velocity data:', error);
    return new Metrics(); // Return an empty Metrics object or provide default values
  }
};

const pullAcceleration = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/recent/acceleration`);
    const data = await response.json();
    return new Metrics(data.top, data.average, data.errors, data.points);
  } catch (error) {
    console.error('Error fetching acceleration data:', error);
    return new Metrics(); // Return an empty Metrics object or provide default values
  }
};

export { pullVelocity, pullAcceleration };
