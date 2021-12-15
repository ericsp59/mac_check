const MackInputField = (props) => {
  const {inputMac, setInputMacHandler} = props
  return (
    <input
        placeholder='Введите MAC'
        type='text'
        value={inputMac}
        onChange={e => setInputMacHandler(e.target.value)}/>
  )
}

export {MackInputField}