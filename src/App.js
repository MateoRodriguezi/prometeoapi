import React, { Component }  from 'react';
import {Provider} from 'react-redux'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Home from './containers/pages/home';
import Error404 from './containers/errors/Error404';

function App() {
  return (
    <Provider>
      <Router>
        <Routes>
          <Route path="*" element={<Error404/>}/>
          <Route path="/" element={<Home/>}/>
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
