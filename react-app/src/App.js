import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          MAC_CHECK 
        </h1>
        <input className="mac-check_input" />
        <button href='http://192.168.50.22:8080' onClick={getData} className='mac-check_btn'>check</button>
      </header>
    </div>
  );
}

async function getData(e){
  // e.preventDefault();
  console.log(123)
  try {
    const response = await fetch('http://192.168.50.22:8080');
    const json = await response.json();
    console.log(json)
  } catch(err) {
    alert(err); // Failed to fetch
  }
}

export default App;
