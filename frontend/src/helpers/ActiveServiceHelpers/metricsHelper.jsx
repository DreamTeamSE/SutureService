import Metrics from '../../DTOs/Metrics'

const API_BASE_URL = import.meta.env.VITE_FASTAPI_IP;

const unsubscribeDevice = async (deviceID, userID) => {
  try {
    const response = await fetch(`${API_BASE_URL}/unsubscribe`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id: deviceID, 
            userID: userID
        })
    });
    const data = await response.json();
    let velocity = new Metrics(data.velocity.top, data.velocity.average, data.velocity.errors, data.velocity.points);
    let acceleration = new Metrics(data.acceleration.top, data.acceleration.average, data.acceleration.errors, data.acceleration.points);
    return {acceleration, velocity};
  } catch (error) {
    
    console.error('Error fetching velocity data:', error);
    return new Metrics(); // Return an empty Metrics object or provide default values
  }
};



const pullAcceleration = async (deviceID, userID) => {
  let metrics = await unsubscribeDevice(deviceID, userID)
  console.log(metrics.acceleration)
  return metrics.acceleration
};

const pullVelocity = async (deviceID, userID) => {
  let metrics = await unsubscribeDevice(deviceID, userID)
  console.log(metrics.velocity)
  return metrics.velocity
};

export { pullVelocity, pullAcceleration };
