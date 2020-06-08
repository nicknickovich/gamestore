import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import User from "./components/User";

const BASE_URL = "http://localhost:5000";

const App = () => {
  const [ users, setUsers ] = useState([]);

  useEffect(() => {
    axios
      .get(`${BASE_URL}/api/users`)
      .then(response => {
        console.log(response.data);
        setUsers(response.data);
      })
  }, [])
  return (
    <div>
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

export default App;
