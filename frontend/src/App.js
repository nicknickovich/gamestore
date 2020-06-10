import React from "react";
import {
  BrowserRouter, Switch, Route
} from "react-router-dom";
import "./App.css";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import Users from "./components/Users";
import Games from "./components/Games";


const App = () => {
  return (
    <BrowserRouter>
      <div>
        <Navigation />
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/games">
            <Games />
          </Route>
          <Route path="/users">
            <Users />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
