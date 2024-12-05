import React, { useState } from 'react'

import { Box, Button, Typography, TextField } from '@mui/material'
const StartComponent = (props) => {
  const [deviceID, setDeviceID] = useState(0)
  const [userID, setUserID] = useState(0)

  let startAssessment = () => {
    props.handleStart(deviceID, userID)
  }
  return (
    <Box sx={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100%" }}>
        <Typography variant="h5"  sx={{fontSize: "32px"}}>Start Assessment</Typography>
            <Button onClick={() => {
                startAssessment(deviceID, userID)
                }} variant="contained" sx={{marginBlock: "32px", height: "55px", width: "150px"}}>
                <Typography variant="p" sx={{fontSize: "20px"}}>Start</Typography>
            </Button>
            <TextField label="Device ID" value={deviceID} onChange={(e) => setDeviceID(e.target.value)} />
            <TextField label="User ID" value={userID} onChange={(e) => setUserID(e.target.value)} />
    </Box>
  )
}

export default StartComponent