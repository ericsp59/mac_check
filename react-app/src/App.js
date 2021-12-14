import { useState } from 'react';
import './App.css';



const Header = () => {
  return <h2>MAC FINDER</h2>
}

const Field = (props) => {
  const {inputMac, setInputMacHandler} = props
  return (
    <input
        placeholder='Введите MAC'
        type='text'
        value={inputMac}
        onChange={e => setInputMacHandler(e.target.value)}/>
  )
}

const Btn = (props) => {
  const text = 'check'
  return <button onClick={props.getData} className='mac-check_btn'>{text}</button>
}


const OutField = (props) => {
    return (
      <p>{`${props.res}`}</p>
    )
}



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
      const response = await fetch('http://192.168.50.22:8080');
      const json = await response.json();
      // console.log(res)
      setRes(json.split(',').toString())
      // console.log(res)
    } catch(err) {
        console.log(err); // Failed to fetch
  }
}

  

  return (
    <div className="App">
      <header className="App-header">
        <Header/>
        <Field inputMac={inputMac} setInputMacHandler={setInputMacHandler}/>
        <Btn getData={getData}/>
        <OutField res={res} />
      </header>
    </div>
  );
}






export default App;
