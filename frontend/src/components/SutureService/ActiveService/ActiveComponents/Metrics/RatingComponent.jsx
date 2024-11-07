import React from 'react'
import { Box, Button, Typography } from '@mui/material'
const RatingComponent = (props) => {

  let startAssessment = () => {
    let startStatus = "VELOCITY"
    props.setSelected(startStatus)
  }
  return (
    <Box sx={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100%" }}>
        <Typography variant="h5"  sx={{fontSize: "32px"}}>Rating</Typography>
            <Typography onClick={() => {
                }} color="primary" sx={{marginBlock: "16px", fontSize: "32px"}}>
                    10/10
            </Typography>
    </Box>
  )
}

export default RatingComponent