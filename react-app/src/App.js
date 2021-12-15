import { useState } from 'react';
import './App.css';
import { Header } from './components/Header/Header';
import { MackInputField } from './components/MackInputField/MackInputField';
import OutField from './components/OutField/OutField';
import Btn from './components/Btn/Btn';

function App() {

  function setInputMacHandler(val) {
    setInputMac(val)
  }

  const [res, setRes] = useState('. . .')
  const [inputMac, setInputMac] = useState('')

  const getData = async function (){
  // e.preventDefault();
  console.log('getting data...')
    try {
      const response = await fetch('http://192.168.50.22:8080?n='+inputMac);
      const json = await response.json();
      const x = json.split(/\n(?!\n)/)
      setRes(x)
      
    } catch(err) {
        console.log(err.toString()); // Failed to fetch
  }
}

  return (
    <div className="App">
      <header className="App-header">
        <Header/>
        <MackInputField inputMac={inputMac} setInputMacHandler={setInputMacHandler}/>
        <Btn getData={getData}/>
        <OutField res={res} inputMac={inputMac}/>
      </header>
    </div>
  );
}






export default App;
