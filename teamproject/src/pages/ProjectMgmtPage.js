import React, {useState} from "react";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { useNavigate } from 'react-router-dom';
import Container from '@mui/material/Container';
import TextField from '@mui/material/TextField';


import Projects from "../components/projects/projects";

export default function ProjectMgmtPage() {

  const navigate = useNavigate();

  const logOut = () => {
    navigate("/");
  }


  const projectProps1 = {
    name:"Project 1",
  }

  const [projList, setList] = useState([projectProps1])
  const [projName, setName] = useState()

  const cap1 = 500
  const cap2 = 100
  const [ava1, setAva1] = useState(0)
  const [ava2, setAva2] = useState(0)

  const projectsProps = {
    cap1:cap1,
    cap2:cap2,
    ava1:ava1,
    ava2:ava2
  }

  const createNew = () =>{
    const newProps = {
      name:projName
    }
    setList([...projList, newProps])
  }

  const updateName = (e) =>{
    setName(e.target.value)
  }



  return (
    <Container>

      <Box sx={{display:'flex',
        flexDirection:'row',
        marginTop:2}}>
          <Typography
              component="h1"
              variant="h4"
              color="primary"
              noWrap
              sx={{ flexGrow: 1 }}
            >
            Projects
          </Typography>
          
          <Button variant="contained" color="error" onClick={logOut}>
            Log Out
          </Button>
        </Box>
        <Box sx={{marginTop:2}}>
          <Typography
                component="h1"
                variant="h5"
                noWrap
                sx={{ flexGrow: 1 }}
              >
              HWSet 1 Capacity: {ava1}/{cap1}
            </Typography>
            <Typography
                component="h1"
                variant="h5"
                noWrap
                sx={{ flexGrow: 1 }}
              >
              HWSet 2 Capacity: {ava2}/{cap2}
            </Typography>
        </Box>
        <Box sx={{display: 'flex',
          flexDirection: 'row',
          gap:4, 
          marginTop:3}}>
          <Projects projectList={projList} {...projectsProps}/>
          <Box> 
            <TextField
                  value={projName}
                  onChange={updateName}
                  margin="normal"
                  required
                  fullWidth/>
            <Button variant="contained" color="primary" onClick={createNew}>
              Create New Project
            </Button>
          </Box>
        </Box>
        

    </Container>
  );
}