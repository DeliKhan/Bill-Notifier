import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';

function App() {
  const [data, setdata] = useState({name:""});
  /*
  useEffect(() => {fetch("/welcome").then((res) =>
    res.json().then((data) => {
        // Setting a data from api
        setdata({
            name: data.name + "hi"
        });
    })
  )},[]);
  */
  /*
  useEffect(() => {fetch("/welcome").then((res) =>
    res.json().then((data) => { console.log(data);
    })
  )},[]);
  */
  useEffect(() => {fetch("/welcome").then((res) => console.log(res))});
  return (
    <div className="App">
      <h1>{data.name}</h1>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
