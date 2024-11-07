import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from '../pages/Home';
import SutureService from '../pages/SutureService';

const Links = () => {
  return (
    <Routes>
         <Route path="/home" element={<Home />} />
         <Route path="/" element={<Home />} />
         <Route path="/start" element={<SutureService />} />
         <Route path="/about" element={<SutureService />} />
         <Route path="/history" element={<SutureService />} />
         <Route path="/signup" element={<SutureService />} />
         <Route path="/login" element={<SutureService />} />
      </Routes>
  )
}

export default Links