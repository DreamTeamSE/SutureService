import React from 'react'
import Button  from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Typography } from '@mui/material';
import StartSection from '../components/Home/StartSection';
import SyncDevice from '../components/SutureService/SyncDevice copy';
import ActiveService from '../components/SutureService/ActiveService/ActiveService';



const SutureService = () => {
  let isSync = true
  let isStarted = true
  return (
    <>
    {isSync && !isStarted && <StartSection />}
    {!isSync && <SyncDevice />}
    {isSync && isStarted && <ActiveService />}


    </>
  )
}

export default SutureService