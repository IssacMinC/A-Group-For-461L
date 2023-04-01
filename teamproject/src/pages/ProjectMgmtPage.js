import React, {useState, useEffect} from "react";
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
  const [projName, setName] = useState("")
  const [joinProjName, setJoinProjName] = useState("")

  const [cap1, setCap1] = useState(0)
  const [cap2, setCap2] = useState(0)
  const [ava1, setAva1] = useState(0)
  const [ava2, setAva2] = useState(0)

  async function getCap1(){
    const response = await fetch(`http://127.0.0.1:5000/getHWCap/HWSet1`, {
      mode: 'cors',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }, 
    });
    const data = await response.json()
    setCap1(data["capacity"])
  }

  async function getCap2(){
    const response = await fetch(`http://127.0.0.1:5000/getHWCap/HWSet2`, {
      mode: 'cors',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }, 
    });
    const data = await response.json()
    setCap2(data["capacity"])
  }

  async function getAva1(){
    const response = await fetch(`http://127.0.0.1:5000/getHWAvail/HWSet1`, {
      mode: 'cors',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }, 
    });
    const data = await response.json()
    setAva1(data["availability"])
  }

  async function getAva2(){
    const response = await fetch(`http://127.0.0.1:5000/getHWAvail/HWSet2`, {
      mode: 'cors',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }, 
    });
    const data = await response.json()
    setAva2(data["availability"])
  }

  async function createProject(){
    const response = await fetch(`http://127.0.0.1:5000/createProject/${projName}`, {
      mode: 'cors',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }, 
    });
    const data = await response.json()
    const message = data["msg"]
    if (message === "created project"){
      createNew()
    }
    alert(message)
  }

  async function joinProject(){
    const response = await fetch(`http://127.0.0.1:5000/joinProject/${joinProjName}`, {
      mode: 'cors',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }, 
    });
    const data = await response.json()
    const message = data["msg"]
    if (message === "joined "+ joinProjName){
      addProjToList()
    }
    alert(message)
  }

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
    setName("")
  }

  const addProjToList = () =>{
    const newProps = {
      name:joinProjName
    }
    setList([...projList, newProps])
    setJoinProjName("")
  }

  const updateName = (e) =>{
    setName(e.target.value)
  }

  const updateJoinProjName = (e) =>{
    setJoinProjName(e.target.value)
  }


  useEffect(() => {
    getCap1()
    getCap2()
    getAva1()
    getAva2()
  }, [])

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
          <Box sx={{display: 'flex',
          flexDirection: 'column'}}> 
            <TextField
                  value={projName}
                  onChange={updateName}
                  margin="normal"
                  required
                  fullWidth/>
            <Button variant="contained" color="primary" onClick={createProject}>
              Create New Project
            </Button>
            <TextField
                  value={joinProjName}
                  onChange={updateJoinProjName}
                  margin="normal"
                  required
                  fullWidth/>
            <Button variant="contained" color="primary" onClick={joinProject}>
              Join Project
            </Button>
            
          </Box>
        </Box>
        
        

    </Container>
  );
}