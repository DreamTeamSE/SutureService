import React, { useState } from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Container } from '@mui/material';
import { start, stop } from '../../../helpers/ActiveServiceHelpers/deviceHelper';
import StartComponent from './ActiveComponents/Metrics/StartComponent';
import VelocityComponent from './ActiveComponents/Metrics/VelocityComponent';
import AccelerationComponent from './ActiveComponents/Metrics/AccelerationComponent';
import RatingComponent from './ActiveComponents/Metrics/RatingComponent';
import EndComponent from './ActiveComponents/Metrics/EndComponent';
import Status from '../../../DTOs/Status'
import Chart from './ActiveComponents/Charts/Chart';
import Metrics from '../../../DTOs/Metrics'
import { pullMetrics } from '../../../helpers/ActiveServiceHelpers/metricsHelper';

const ActiveService = (props) => {

  const [selected, setSelected] = useState(Status.START)

  const [deviceID, setDeviceID] = useState(0)

  const [metrics, setMetrics] = useState({velocity : new Metrics(0,0,0,[]), acceleration : new Metrics(0,0,0,[])})

  const [activeMetrics, setActiveMetrics] = useState(new Metrics(0, 0, 0, []))

  const handleStart = (deviceID) => {
    setDeviceID(deviceID)
    setSelected(Status.STARTED)
    start(deviceID)
  }

  const handleStop = async () => {
    await stop(deviceID)
    const newMetrics = await pullMetrics("123")
    setMetrics(newMetrics)
    setActiveMetrics(newMetrics.velocity)
    setSelected(Status.VELOCITY)
  }

  const handleVelocity = async () => {
    setSelected(Status.VELOCITY)
    setActiveMetrics(metrics.velocity)
  }

  const handleAcceleration = async () => {
    setSelected(Status.ACCELERATION)
    setActiveMetrics(metrics.acceleration)
  }

  const handleSelect = async (select) => {
    setSelected(select)
  }


  return (
    <Box sx={{ 
      display: 'flex', 
      flexDirection: { xs: 'column', md: 'row' }, 
      justifyContent: 'center', 
      alignItems: 'center', 
      padding: 0, 
      height: 'calc(100vh - 80px)' 
    }}>
      <Container sx={{ 
        backgroundColor: 'white', 
        height: '500px', 
        marginTop: '40px', 
        marginInline: '32px', 
        borderRadius: '16px', 
        paddingLeft: '12px !important', 
        paddingRight: '12px !important', 
        paddingTop: '8px', 
        display: 'flex', 
        flexDirection: 'column' 
      }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-around', alignItems: 'center' }}>
          <Button onClick={() => { handleSelect(Status.START) }}>
            Start
          </Button>
          <Button onClick={() => { handleVelocity() }}>
            Velocity
          </Button>
          <Button onClick={() => { handleAcceleration() }}>
            Acceleration
          </Button>
          <Button onClick={() => { handleSelect(Status.RATING) }}>
            Rating
          </Button>
        </Box>
        {selected === Status.START && <StartComponent handleStart={handleStart} />}
        {selected === Status.STARTED && <EndComponent handleStop={handleStop} />}
        {selected === Status.VELOCITY && <VelocityComponent metrics={activeMetrics} />}
        {selected === Status.ACCELERATION && <AccelerationComponent metrics={activeMetrics} />}
        {selected === Status.RATING && <RatingComponent />}
      </Container>
      <Container sx={{ 
        backgroundColor: 'white', 
        height: '500px', 
        marginTop: '40px', 
        marginInline: '32px', 
        borderRadius: '16px' 
      }}>
        <Chart metrics={activeMetrics} selected={selected} />
      </Container>
    </Box>
  )
}

export default ActiveService