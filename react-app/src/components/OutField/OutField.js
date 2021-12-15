import './OutField.css'

const OutField = (props) => {
  const {res, inputMac} = props
  if (res !== '. . .') {
    console.log(res)

    const elements = res.map((elem, key) => {
      if (inputMac.length >= 10) 
      if (elem.replaceAll(':', '').replaceAll('-', '').indexOf(inputMac.trim().toLowerCase().replaceAll(':', '').replaceAll('-', ''))+1 ) 
        return <h6 key={key} className='target'>{elem}</h6>
      return <h6 key={key}>{elem}</h6>
    })
    return (
      <div className='elements'>{elements}</div>
    )
  }
  return <p>{res}</p>
}

export default OutField