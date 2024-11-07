import { Container, Typography, Box } from '@mui/material'
import React from 'react'

const AccelerationComponent = (props) => {
  return (
    <Box sx={{display: "flex", flexDirection: "column", justifyContent: "space-evenly", height: "100%"}}>
        <Container sx={containerStyles}>
            <Typography variant="h6" sx={{fontSize: fonts.title}} >Top Acceleration</Typography>
            <Typography variant="p" color="primary" sx={{fontSize: fonts.metric}}>{props.metrics.top} m/s<sup>2</sup></Typography>
        </Container>
        <Container sx={containerStyles}>
            <Typography variant="h6" sx={{fontSize: fonts.title}}>Average Acceleration</Typography>
            <Typography variant="p" color="primary" sx={{fontSize: fonts.metric}}>{props.metrics.average} m/s<sup>2</sup></Typography>
        </Container>
        <Container sx={containerStyles}>
            <Typography variant="h6" sx={{fontSize: fonts.title}}>Errors</Typography>
            <Typography variant="p" color="primary" sx={{fontSize: fonts.metric}}>{props.metrics.errors}</Typography>
        </Container>
    </Box>
  )
}

let containerStyles = {display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"}
let fonts = {title: "28px", metric: "24px"}
export default AccelerationComponent