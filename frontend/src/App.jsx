import { useState } from 'react'

import './App.css';

function App() {

  const [plate, setPlate] = useState('')
  const [result, setResult] = useState({})
  const [loading, setLoading] = useState(false)

  const handleChangePlate = (e) => {
    setPlate(e.target.value)
  }

  const handleGetCar = () => {
    setResult({});
    setLoading(true);
    (async () => {
      try {
        const res = await (
          await fetch(
            `http://${window.location.hostname}:5000/get_car?plate=${plate}`
          )
        ).json()
        setLoading(false)
        if (res['car']) {
          setResult(res.car)
        } else {
          setResult(res)
        }
        setPlate('')
      }
      catch (err) {
        setLoading(false)
        console.error(err)
      }
    })()
  }

  return (
    <div className='background'>
      <div className='paper'>
        <h3>Get Car Name</h3>
        <input
          type='search'
          value={plate}
          placeholder='provide a car plate'
          onChange={handleChangePlate}
          onKeyDown={e => { if (e.key === 'Enter') { handleGetCar() } }}
        />
        <input
          type='button'
          value='Get Car'
          onClick={handleGetCar}
        />
      </div>
      <div className='paper'>
        {result?.plate &&
          <>
            <p>Car found:</p>
            <ul>
              <li>
                <h5 className='label'> Plate:</h5> {result?.plate}
              </li>
              <li>
                <h5 className='label'> Model:</h5> {result?.model}
              </li>
            </ul>
          </>
        }
        {result?.warning &&
          <p>{result.warning}</p>
        }
        {loading &&
          <p className='loading'>Searching for plate {plate}</p>
        }
      </div>
    </div>
  );
}

export default App;
