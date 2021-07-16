import './App.css';
import React, { useEffect, useState } from 'react';
import ReactWordcloud from 'react-wordcloud';
import axios from 'axios'

function App() {
  const [words, setWords] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:5000/').then(response => {
      console.log("SUCCESS", response)
      setWords(response.data.words)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>Twitter Word Cloud</p>
        <div>{words ? 
          <ReactWordcloud words={words} />
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default App;