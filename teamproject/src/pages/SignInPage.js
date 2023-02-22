import React from "react";
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';

export default function SignInPage() {
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
                />
                <TextField
                  margin="normal"
                  required
                  fullWidth
                  id="password"
                  label="Password"
                  name="password"
                />
          <Button variant="contained" color="primary">
          Sign In
        </Button>
        <Button variant="text" color="primary">
          Create New Account
        </Button>
        </Box>
      </Box>
  </Container>    
    
  );
}