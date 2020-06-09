import React from "react";

const GameForm = (props) => {
  return (
    <div>
      <form onSubmit={props.onSubmit}>
        <div>
          Name:
          <input
            value={props.nameValue}
            onChange={props.nameOnChange}
          />
        </div>
        <div>
          Price:
          <input
            type="number"
            value={props.priceValue}
            onChange={props.priceOnChange}
          />
        </div>
        <div>
          Cover Image:
          <input
            value={props.coverValue}
            onChange={props.coverOnChange}
          />
        </div>
        <div>
          Description:
          <textarea
            value={props.descriptionValue}
            onChange={props.descriptionOnChange}
          ></textarea>
        </div>
        <div>
          <button type="submit">Add</button>
        </div>
      </form>
    </div>
  );
}

export default GameForm;
