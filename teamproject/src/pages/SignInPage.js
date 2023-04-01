import React from "react";
import { useState } from "react";
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import ProjectMgmtPage from "./ProjectMgmtPage";

import { useNavigate } from 'react-router-dom';



export default function SignInPage({setUser}) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  
  const navigate = useNavigate();
  
  
  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  }

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  }

  async function createAccount(event) {
    event.preventDefault();
    const response = await fetch(`http://127.0.0.1:5000/signup/${username}/${password}`, {
      // credentials: 'include',
      mode: 'cors',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
    setUsername("");
    setPassword("");
    const resp = await response.json();
    console.log(resp);
    alert(resp["msg"]);
  }

  async function login(event) {
    event.preventDefault();
    const response = await fetch(`http://127.0.0.1:5000/login/${username}/${password}`, {
      mode: 'cors',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
    setUsername("");
    setPassword("");
    const resp = await response.json();
    console.log(resp);
    alert(resp["msg"]);
    
    if (resp["msg"] === 'Login Successful') {
      navigate('/projects');
      setUser(username)
    }
  }

  return (
    <Container component="main" maxWidth="xs">
      <Box sx={{
        marginTop: 8,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}>
        <Box component="form" sx={{ mt: 1 }}>
          <TextField
                  margin="normal"
                  required
                  fullWidth
                  id="username"
                  label="Username"
                  name="username"
                  value={username}
                  onChange={handleUsernameChange}
                />
                <TextField
                  margin="normal"
                  required
                  fullWidth
                  id="password"
                  label="Password"
                  name="password"
                  type={"password"}
                  value={password}
                  onChange={handlePasswordChange}
                />
          <Button variant="contained" color="primary" onClick={login}>
          Sign In
        </Button>
        <Button variant="text" color="primary" onClick= {createAccount}>
          Create New Account
        </Button>
        </Box>
      </Box>
  </Container>    
    
  );
}