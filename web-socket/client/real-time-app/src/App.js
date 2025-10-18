
import React, { useEffect } from 'react';

function App() {
  var ws = null;
  useEffect(() => {
    ws = new WebSocket("ws://localhost:8088/ws")
    ws.onopen = () => ws.send("Connected to React! sending from frontend")
    ws.onmessage = (e) => {
      console.log(e.data)
    } 
  })
  

  return (
    <div className="App">
      hellow world
    </div>
  );
}

export default App;
