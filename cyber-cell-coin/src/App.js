import React from 'react';
import './App.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Home from './pages';
import SigninPage from './pages/Signin'
import RegisterPage from './pages/Register'
/*import DashboardPage from './pages/Dashboard'*/

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/signin" component={SigninPage} exact />
        <Route path="/Register" component={RegisterPage} exact />
        

      </Switch>
    </Router>
  );
}

export default App;