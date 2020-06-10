import React, { useState, useEffect } from "react";
import axios from "axios";
import Game from "./Game";
import GameForm from "./GameForm";

const BASE_URL = "http://localhost:5000";

const Games = () => {
  const [ games, setGames ] = useState([]);

  const [ newGameName, setNewGameName ] = useState("");
  const [ newGamePrice, setNewGamePrice ] = useState(0);
  const [ newGameCover, setNewGameCover ] = useState("");
  const [ newGameDescription, setNewGameDescription ] = useState("");

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
  </div>
  );
}

export default Games;
