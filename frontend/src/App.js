import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import User from "./components/User";
import Game from "./components/Game";
import GameForm from "./components/GameForm";

const BASE_URL = "http://localhost:5000";

const App = () => {
  const [ users, setUsers ] = useState([]);
  const [ games, setGames ] = useState([]);

  const [ newGameName, setNewGameName ] = useState("");
  const [ newGamePrice, setNewGamePrice ] = useState(0);
  const [ newGameCover, setNewGameCover ] = useState("");
  const [ newGameDescription, setNewGameDescription ] = useState("");

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

  const addGame = (event) => {
    event.preventDefault();
    const newGame = {
      name: newGameName,
      price: newGamePrice,
      cover_image: newGameCover,
      description: newGameDescription
    };
    axios
      .post(`${BASE_URL}/api/games`, newGame)
      .then(response => {
        setGames(games.concat(response.data));
        setNewGameName("");
        setNewGamePrice(0);
        setNewGameCover("");
        setNewGameDescription("");
      })
  }

  const hideUserSection = () => {
    const users = document.getElementById("users");
    if (users.style.display === "none") {
      users.style.display = "block";
    } else {
      users.style.display = "none";
    }
  }

  const gameNameChange = (event) => {
    setNewGameName(event.target.value);
  }

  const gamePriceChange = (event) => {
    setNewGamePrice(event.target.value);
  }

  const gameCoverChange = (event) => {
    setNewGameCover(event.target.value);
  }

  const gameDescriptionChange = (event) => {
    setNewGameDescription(event.target.value);
  }

  return (
    <div>
      <h2>Add Game</h2>
      <GameForm
        nameValue={newGameName}
        nameOnChange={gameNameChange}
        priceValue={newGamePrice}
        priceOnChange={gamePriceChange}
        coverValue={newGameCover}
        coverOnChange={gameCoverChange}
        descriptionValue={newGameDescription}
        descriptionOnChange={gameDescriptionChange}
        onSubmit={addGame}
      />
      <div id="games">
        <h2>Games</h2>
        <ul>
          {games.map(game => (
            <Game 
              name={game.name}
              description={game.description}
              coverImage={game.cover_image}
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
