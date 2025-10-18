import './App.css';
import {useEffect, useState} from 'react';


function App() {
  const [data, setData] = useState('Initializing...');
  useEffect(() =>{
    const sse = new EventSource('http://127.0.0.1:8088/ppp');
    function handleStream(e) {
      console.log(e)
      setData(e.data);
    }
    sse.onmessage = e => {handleStream(e)}
    sse.onerror = e => {
      console.log(e)
      sse.close()
    }
    return () => {
      sse.close()
    }
  }, [])
  return (
    <div className="App">
        The last streamed item was: {data}
    </div>
  );
}

export default App;
