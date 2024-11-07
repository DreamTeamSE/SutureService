import React from 'react'
import { Box, Button, Typography } from '@mui/material'
const StartComponent = (props) => {

  let startAssessment = () => {
    props.handleStart()
  }
  return (
    <Box sx={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100%" }}>
        <Typography variant="h5"  sx={{fontSize: "32px"}}>Start Assessment</Typography>
            <Button onClick={() => {
                startAssessment()
                }} variant="contained" sx={{marginBlock: "32px", height: "55px", width: "150px"}}>
                <Typography variant="p" sx={{fontSize: "20px"}}>Start</Typography>
            </Button>
    </Box>
  )
}

export default StartComponent