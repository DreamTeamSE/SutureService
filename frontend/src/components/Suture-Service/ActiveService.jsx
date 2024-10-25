import React from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Container, Typography } from '@mui/material';
import StartSection from './StartService';
import SyncDevice from './SyncDevice copy';
import Divider from '@mui/material/Divider';

const ActiveService = () => {
  let isSync = true
  let isStarted = false
  return (
    <Box sx={{ display: 'flex', justifyContent: 'space-between', padding: 0 }}>
      <Container sx={{backgroundColor:"white", height: "500px", marginTop: "40px", marginInline: "32px", borderRadius: "16px", paddingLeft: "12px !important", paddingRight: "12px !important", paddingTop: "8px"}}>
      <Typography>Date</Typography>
      <Typography>October 25th, 2024</Typography>
      <Divider />
      
      <Typography>Name</Typography>
      <Typography>Max Martin</Typography>
      <Divider />
      
      <Typography>Peak Accelerator</Typography>
      <Typography>1 cm/s^2</Typography>
      <Divider />
      
      <Typography>Average Accelerator</Typography>
      <Typography>1 cm/s^2</Typography>
      <Divider />
      
      <Typography>Peak Velocity</Typography>
      <Typography>1 cm/s^2</Typography>
      <Divider />
      
      <Typography>Average Velocity</Typography>
      <Typography>1 cm/s^2</Typography>
      </Container>
      <Container sx={{backgroundColor:"white", height: "500px", marginTop: "40px", marginInline: "32px", borderRadius: "16px"}}>
  </Container>
  </Box>

  )
}

export default ActiveService