import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect } from "react";

const io = require("socket.io-client");

function App() {
  
  let socket = io("http://localhost:5000");
  const [ msg, setMsg ] = useState("");
  const [ d, setD ] = useState();
    
  socket.on("data", function (msg) {
    console.log("Received Data :: " + msg.date + " :: " + msg.value);
    setMsg(msg.value);
    setD(msg.date);
  })
  return (
    <div className="App">
      <header className="App-header">
        
        <p>
          value is {msg} and time is {d}
        </p>
        
      </header>
    </div>
  );
}

export default App;
