import logo from './logo.svg';
import './App.css';
import SignInPage from './pages/SignInPage';
import ProjectMgmtPage from './pages/ProjectMgmtPage';
import {BrowserRouter,Routes,Route} from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={SignInPage} />
        <Route path="/projects" Component={ProjectMgmtPage} />
      </Routes>
  </BrowserRouter>
  );
}

export default App;
