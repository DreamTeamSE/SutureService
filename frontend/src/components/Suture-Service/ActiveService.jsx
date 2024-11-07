import React, { useState } from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Container, Typography } from '@mui/material';
import StartSection from './StartService';
import SyncDevice from './SyncDevice copy';
import Divider from '@mui/material/Divider';
import StartComponent from './ActiveComponents/Metrics/StartComponent';
import VelocityComponent from './ActiveComponents/Metrics/VelocityComponent';
import AccelerationComponent from './ActiveComponents/Metrics/AccelerationComponent';
import RatingComponent from './ActiveComponents/Metrics/RatingComponent';


const ActiveService = () => {
  let isSync = true
  let isStarted = false



  const Status = Object.freeze({
    START: 'START',
    VELOCITY: 'VELOCITY',
    ACCELERATION: 'ACCELERATION',
    RATING: 'RATING',
  });


  const [selected, setSelected] = useState(Status.START)

  let handleSelect = (select) => {
    setSelected(select)
  }
  return (
    <Box sx={{ display: 'flex', justifyContent: "center", alignItems: "center", padding: 0, height: 'calc(100vh - 80px)' }}>
      <Container sx={{ backgroundColor: "white", height: "500px", marginTop: "40px", marginInline: "32px", borderRadius: "16px", paddingLeft: "12px !important", paddingRight: "12px !important", paddingTop: "8px", display: 'flex', flexDirection: 'column' }}>
          <Box sx={{display: 'flex', justifyContent: 'space-around', alignItems: 'center'}}>
            <Button onClick={() => {handleSelect(Status.START)}}>
                Start
            </Button>
            <Button onClick={() => {handleSelect(Status.VELOCITY)}}>
                Velocity
            </Button>
            <Button onClick={() => {handleSelect(Status.ACCELERATION)}}>
                Acceleration
            </Button>
            <Button onClick={() => {handleSelect(Status.RATING)}}>
                Rating
            </Button>
          </Box>
        {selected === Status.START && <StartComponent setSelected={setSelected}/>}
        {selected === Status.VELOCITY && <VelocityComponent />}
        {selected === Status.ACCELERATION && <AccelerationComponent />}
        {selected === Status.RATING && <RatingComponent />}
      </Container>
      <Container sx={{backgroundColor:"white", height: "500px", marginTop: "40px", marginInline: "32px", borderRadius: "16px"}}>
    </Container>
  </Box>

  )
}

export default ActiveService