import React from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import {Home} from './containers/pages/Home.jsx';
import {Error404} from './containers/errors/Error404.jsx';


function App() {
  return (
    <div>

      <Router>
        <Routes>
          {/* Error Display */}
          <Route path="*" element={<Error404/>}/>

          {/* Home Display */}
          <Route path="/" element={<Home/>}/>

        </Routes>
      </Router>

    </div>
  );
}

export default App;
