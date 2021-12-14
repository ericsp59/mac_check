import './App.css';

function WhoAmI (props) {
  const {name, surname, link} = props
  return (
    <div>
      <h1>My name is {name}, surname {surname}</h1>
      <a href={link}>YANDEX</a>
    </div>
  )
}


function AppTest () {
  return (
    <div className='App'>
      <WhoAmI
        name='John'
        surname='Smith'
        link='https://ya.ru'
      />
    </div>
  )
}

export default AppTest