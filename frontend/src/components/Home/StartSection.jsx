import React from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Typography } from '@mui/material';
import { Link } from 'react-router-dom';


const StartSection = () => {
  return (
    <>
    <Box sx={{
        width: '100%',
        display: 'flex',
        flexDirection: 'column',  
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: '64px' 
      }}>
        <Typography variant='h4'>Making Sutures Services Safer</Typography>
        <Link to="/start" style={{ textDecoration: 'none', color:"white" }}>
          <Button variant="contained" color="primary" sx={{width: "256px", marginTop: "32px"}}>
              <Typography variant='h6'>Start</Typography>
          </Button>
        </Link>
    </Box>
    </>
  )
}

export default StartSection