import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          MAC_CHECK! 
        </h1>
        <input className="mac-check_input" />
        <button onClick={getData} className='mac-check_btn'>check</button>
        <OutputBlock />
      </header>
      
    </div>
  );
}

function OutputBlock() {
  let x = '123123123'
  function setX(a) {
    this.x = a
  } 
  return (
    <div>
      <span>{x}</span>
    </div>
  );
}

async function getData(){
  // e.preventDefault();
  console.log(123)
  try {
    const response = await fetch('http://192.168.50.22:8080');
    const json = await response.json();
    console.log(typeof(json))
    OutputBlock.setX(json)
    
  } catch(err) {
    alert(err); // Failed to fetch
  }
}

export default App;
