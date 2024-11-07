import React from 'react'
import { Box, Button, Typography } from '@mui/material'
const EndComponent = (props) => {

  let stopAssessment = () => {
    props.handleStop()
  }
  return (
    <Box sx={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100%" }}>
        <Typography variant="h5"  sx={{fontSize: "32px"}}>Stop Assessment</Typography>
            <Button onClick={() => {
                stopAssessment()
                }} variant="contained" sx={{marginBlock: "32px", height: "55px", width: "150px"}}>
                <Typography variant="p" sx={{fontSize: "20px"}}>Stop</Typography>
            </Button>
    </Box>
  )
}

export default EndComponent