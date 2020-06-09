import React from "react";

const User = (props) => {
  return (
    <div>
      <h3>{props.first_name} {props.last_name}</h3>
      <ul>
        <li>{props.username}</li>
        <li>{props.account_created}</li>
        <li>{props.email}</li>
      </ul>
    </div>
  );
}

export default User;
