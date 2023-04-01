import logo from './logo.svg';
import './App.css';
import SignInPage from './pages/SignInPage';
import ProjectMgmtPage from './pages/ProjectMgmtPage';
import {BrowserRouter,Routes,Route} from "react-router-dom";
import { useState, useEffect } from 'react';

function App() {

  const [username, setUsername] = useState('')

  const signIn = () =>{
    return(
      <SignInPage setUser={setUsername}/>
    )
  }

  const projectMgmt = () =>{
    return(
      <ProjectMgmtPage user={username}/>
    )
  }

  useEffect(()=>{
    console.log(username)
  },[username])

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={signIn} />
        <Route path="/projects" Component={projectMgmt} />
      </Routes>
  </BrowserRouter>
  );
}

export default App;
