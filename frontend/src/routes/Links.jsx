import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from '../pages/Home';
import SutureService from '../pages/SutureService';

const Links = () => {
  return (
    <Router>
    <Routes>
         <Route path="/home" element={<Home />} />
         <Route path="/" element={<Home />} />
         <Route path="/start" element={<SutureService />} />
      </Routes>
    </Router>
  )
}

export default Links