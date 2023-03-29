import React from "react";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

import { useNavigate } from 'react-router-dom';


export default function ProjectMgmtPage() {

  const navigate = useNavigate();

  const logOut = () => {
    navigate("/");
  }

  return (
    <Stack spacing={3} direction="column" alignItems="flex-start" >
        <Typography
              component="h1"
              variant="h4"
              color="primary"
              noWrap
              sx={{ flexGrow: 1 }}
            >
              Projects
            </Typography>
        <Button variant="text" color="primary">
            Project 1
        </Button>
        <Button variant="text" color="primary">
            Project 2
        </Button>
        <Button variant="contained" color="primary">
            Create New Project
        </Button>
        <Button variant="contained" color="secondary" onClick={logOut}>
            Log Out
        </Button>
    </Stack>
  );
}