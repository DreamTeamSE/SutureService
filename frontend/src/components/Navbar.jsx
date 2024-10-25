import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';

function Navbar() {
  return (
    <AppBar position="static" color="background" sx={{ boxShadow: 'none', padding: '0 20px' }}>
      <Toolbar>
        {/* Left-aligned title */}
        <Typography variant="h5" component="div" fontWeight="bold" color="primary" sx={{ flexGrow: 1 }}>
          Suture Service
        </Typography>

        {/* Center-aligned menu items, including "Sign Up" */}
        <Box sx={{ display: 'flex', gap: 2 }}>
          <Button color="inherit">Start</Button>
          <Button color="inherit">History</Button>
          <Button color="inherit">About</Button>
          <Button color="inherit">Login</Button>
          <Button variant="contained" color="primary">Sign Up</Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
