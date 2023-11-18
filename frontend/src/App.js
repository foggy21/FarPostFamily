import './App.css';
import {BrowserRouter, Routes, Route, Link} from 'react-router-dom';
import {Users} from "./components/Users.js";

function App() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/users" element={<Users/>}/>
        </Routes>
        <Link to='/users'>hello</Link>
      </BrowserRouter>

      
    );
}

export default App;