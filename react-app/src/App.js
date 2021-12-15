import { useState } from 'react';
import './App.css';
import { Header } from './components/Header/Header';
import { MackInputField } from './components/MackInputField/MackInputField';
import OutField from './components/OutField/OutField';
import Btn from './components/Btn/Btn';
import { Spinner } from './components/Spinner/Spinner';
// f48cebf9b043
function App() {

  function setInputMacHandler(val) {
    setInputMac(val)
  }

  const [res, setRes] = useState('. . .')
  const [inputMac, setInputMac] = useState('')
  const [isLoading, setIsloading] = useState(false)

  const getData = async function (){
    setIsloading(true)
  // e.preventDefault();
  console.log('getting data...')
    try {
      const response = await fetch('http://192.168.50.22:8080?n='+inputMac);
      const json = await response.json();
      const x = json.split(/\n(?!\n)/)
      setRes(x)
      setIsloading(false)
      
    } catch(err) {
        console.log(err.toString()); // Failed to fetch
        setIsloading(false)
        setRes('. . .')
  }
}

  return (
    <div className="App">
      <header className="App-header">
        <Header/>
        <MackInputField inputMac={inputMac} setInputMacHandler={setInputMacHandler}/>
        <Btn getData={getData}/>
        {isLoading
          ? <Spinner/> 
          : <OutField res={res} inputMac={inputMac}/>
        }
      </header>
    </div>
  );
}






export default App;
