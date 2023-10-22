import './App.scss';
import { Route, Routes } from 'react-router-dom';
import Layout from './Components/Layout';
import Home from './Components/Home';
import Form from './Components/Form';
import Results from './Components/Results';

function App() {

  return (
    <>
    <Routes>
    <Route path="/" element = {<Layout />}>
      <Route index element = {<Home />}/>
      <Route path="form" element = {<Form />}/>
      <Route path='results' element = {<Results />}/>
    </Route>
    </Routes> 
    </>
  );
}

export default App;

