import React from "react";
import { useState } from "react";
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import ProjectMgmtPage from "./ProjectMgmtPage";

export default function SignInPage() {

  
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  
  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  }

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const response = await fetch(`http://127.0.0.1:5000/signup/${username}/${password}`, {
      mode: 'no-cors',
      credentials: 'include',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    }).then((response) => {
      console.log(response);
    });
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
                  value={password}
                  onChange={handlePasswordChange}
                />
          <Button variant="contained" color="primary" href="/projects">
          Sign In
        </Button>
        <Button variant="text" color="primary" onClick= {handleSubmit}>
          Create New Account
        </Button>
        </Box>
      </Box>
  </Container>    
    
  );
}