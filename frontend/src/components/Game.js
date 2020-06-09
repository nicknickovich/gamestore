import React from "react";

const Game = (props) => {
  return (
    <div>
      <h3>{props.name}</h3>
      <ul>
        <li>{props.description}</li>
        <li>{props.coverImage}</li>
        <li>{props.price}</li>
      </ul>
    </div>
  );
}

export default Game;
