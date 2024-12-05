import React, { useState, useEffect } from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Container } from '@mui/material';
import StartComponent from './ActiveComponents/Metrics/StartComponent';
import VelocityComponent from './ActiveComponents/Metrics/VelocityComponent';
import AccelerationComponent from './ActiveComponents/Metrics/AccelerationComponent';
import RatingComponent from './ActiveComponents/Metrics/RatingComponent';
import VelocityChart from './ActiveComponents/Charts/Chart';
import EndComponent from './ActiveComponents/Metrics/EndComponent';
import Status from '../../../DTOs/Status'
import Chart from './ActiveComponents/Charts/Chart';
import Metrics from '../../../DTOs/Metrics'
import { pullAcceleration, pullVelocity } from '../../../helpers/ActiveServiceHelpers/metricsHelper';

const ActiveService = () => {

  const [selected, setSelected] = useState(Status.START)

  let handleSelect = async (select) => {
    await getMetrics(select)
    setSelected(select)
  }

  let handleStop = async () => {
    await getMetrics(Status.VELOCITY)
    setSelected(Status.VELOCITY)
  }

  let handleStart = () => {

    setSelected(Status.STARTED)
  }

  let getMetrics = async (selected) => {
    let newMetrics = metrics
    if (selected === Status.ACCELERATION) {
      newMetrics = await pullAcceleration()
    } else if (selected === Status.VELOCITY) {
      newMetrics = await pullVelocity()
    } 
    setMetrics(newMetrics)
}

  const [metrics, setMetrics] = useState(new Metrics())

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
          <Button onClick={() => { handleSelect(Status.VELOCITY) }}>
            Velocity
          </Button>
          <Button onClick={() => { handleSelect(Status.ACCELERATION) }}>
            Acceleration
          </Button>
          <Button onClick={() => { handleSelect(Status.RATING) }}>
            Rating
          </Button>
        </Box>
        {selected === Status.START && <StartComponent handleStart={handleStart} />}
        {selected === Status.STARTED && <EndComponent handleStop={handleStop} />}
        {selected === Status.VELOCITY && <VelocityComponent metrics={metrics} />}
        {selected === Status.ACCELERATION && <AccelerationComponent metrics={metrics} />}
        {selected === Status.RATING && <RatingComponent />}
      </Container>
      <Container sx={{ 
        backgroundColor: 'white', 
        height: '500px', 
        marginTop: '40px', 
        marginInline: '32px', 
        borderRadius: '16px' 
      }}>
        <Chart metrics={metrics} selected={selected} />
      </Container>
    </Box>
  )
}

export default ActiveService