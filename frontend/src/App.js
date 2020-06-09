import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import User from "./components/User";
import Game from "./components/Game";

const BASE_URL = "http://localhost:5000";

const App = () => {
  const [ users, setUsers ] = useState([]);
  const [ games, setGames ] = useState([]);

  useEffect(() => {
    axios
      .get(`${BASE_URL}/api/users`)
      .then(response => {
        setUsers(response.data);
      })
  }, []);

  useEffect(() => {
    axios
      .get(`${BASE_URL}/api/games`)
      .then(response => {
        setGames(response.data);
      })
  }, []);

  const hideUserSection = () => {
    const users = document.getElementById("users");
    if (users.style.display === "none") {
      users.style.display = "block";
    } else {
      users.style.display = "none";
    }
  }

  return (
    <div>
      <div id="games">
        <h2>Games</h2>
        <ul>
          {games.map(game => (
            <Game 
              name={game.name}
              description={game.description}
              price={game.price}
              key={game.name}
            />
          ))}
        </ul>
      </div>
      <button onClick={hideUserSection}>
        Hide/Show users
      </button>
      <div id="users">
      <h2>Users</h2>
        <ul>
          {users.map(user => (
            <User 
              first_name={user.first_name}
              last_name={user.last_name}
              username={user.username}
              account_created={user.account_created}
              email={user.email}
              key={user.username}
            />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
