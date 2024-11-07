import Metrics from '../DTOs/Metrics'

const pullVelocity = async () => {
  try {
    const response = await fetch('http://localhost:8000/recent/velocity');
    const data = await response.json();
    return new Metrics(data.top, data.average, data.errors, data.points);
  } catch (error) {
    console.error('Error fetching velocity data:', error);
    return new Metrics(); // Return an empty Metrics object or provide default values
  }
};

const pullAcceleration = async () => {
  try {
    const response = await fetch('http://localhost:8000/recent/acceleration');
    const data = await response.json();
    return new Metrics(data.top, data.average, data.errors, data.points);
  } catch (error) {
    console.error('Error fetching acceleration data:', error);
    return new Metrics(); // Return an empty Metrics object or provide default values
  }
};

export { pullVelocity, pullAcceleration };