import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <AppBar position="static" color="background" sx={{ boxShadow: 'none', padding: '0 20px' }}>
      <Toolbar>
        {/* Left-aligned title */}
        <Link to="/home" style={{ textDecoration: 'none', color: 'inherit', flexGrow: 1 }}>
          <Typography variant="h5" component="div" fontWeight="bold" color="primary">
            Suture Service
          </Typography>
        </Link>

        {/* Center-aligned menu items, including "Sign Up" */}
        <Box sx={{ display: 'flex', gap: 2 }}>
          <Link to="/start" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">Start</Button>
          </Link>
          <Link to="/history" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">History</Button>
          </Link>
          <Link to="/about" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">About</Button>
          </Link>
          <Link to="/login" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">Login</Button>
          </Link>
          <Link to="/signup" style={{ textDecoration: 'none' }}>
            <Button variant="contained" color="primary">Sign Up</Button>
          </Link>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
