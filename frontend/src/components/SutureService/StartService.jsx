import React from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Typography } from '@mui/material';


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
        <Typography variant='h4'>Device is Not Sync!</Typography>
        <Button variant="contained" color="primary" sx={{width: "256px", marginTop: "32px"}}>
           <Typography variant='h6'>Sync</Typography>
        </Button>
    </Box>
    </>
  )
}

export default StartSection