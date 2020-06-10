import React, { useState, useEffect } from "react";
import axios from "axios";
import User from "./User";

const BASE_URL = "http://localhost:5000";

const Users = () => {
  const [ users, setUsers ] = useState([]);

  useEffect(() => {
    axios
      .get(`${BASE_URL}/api/users`)
      .then(response => {
        setUsers(response.data);
      })
  }, []);

  return (
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
  );
}

export default Users;
