const Btn = (props) => {
  const text = 'check'
  return <button onClick={props.getData} className='mac-check_btn'>{text}</button>
}

export default Btn