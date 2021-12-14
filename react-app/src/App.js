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
    const {res} = props
    if (res !== '. . .') {
      console.log(res)
      const elements = res.map(elem => {
        return <h6>{elem}</h6>
      })
      return (
        <div className='elements'>{elements}</div>
      )
    }
    return <p>{res}</p>



    

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
      const response = await fetch('http://192.168.50.22:8080?n='+inputMac);
      const json = await response.json();
      console.log(json)
      const x = json.split(/\n(?!\n)/)
      console.log(typeof(res))
      setRes(x)
      
    } catch(err) {
        console.log(err.toString()); // Failed to fetch
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
