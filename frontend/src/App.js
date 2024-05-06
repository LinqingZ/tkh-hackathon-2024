import logo from './logo.svg';
import React, { useState, useEffect, PureComponent } from "react";
import './App.css';

import ReactDiffViewer from 'react-diff-viewer';

function App() {
  const [resume, setResume] = useState({
    improved: ""
  })
  const [file, setFile] = useState()
  const [fileContents, setFileContents] = useState()
  const [showDisplay, setShowDisplay]= useState(false)

  function handleChange(event) {
    setFile(event.target.files[0])
  }
  

  function readFile() {
    const reader = new FileReader()
    console.log(file)
    reader.onload = async function(event) {
      await setFileContents(event.target.result)
    }
    reader.readAsText(file); 
    
    
  }

  useEffect(() => {
    improveResume(fileContents);
    setResume({improved: "loading..."});
  }, [fileContents]);



  const improveResume = async (originalResume) => {
    try {
      console.log(originalResume)
      const response = await fetch('/improve', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ original_resume: originalResume }),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log('data recieved')
      if (originalResume != undefined) {
        setShowDisplay(true)
      }
      setResume({improved: data.improved_resume})
      return data.improved_resume;
    } catch (error) {
      console.error('There was a problem with your fetch operation:', error);
      return null;
    }
  };
  // Using useEffect for single rendering
  useEffect(() => {
      // Using fetch to fetch the api from 
      // flask server it will be redirected to proxy
      fetch("/data").then((res) =>
          res.json().then((data) => {
              // Setting a data from api
              setdata({
                  name: data.Name,
                  age: data.Age,
                  date: data.Date,
                  programming: "hello",
              });
          })
      );
  }, []);

  return (
      <div className="App">
          <header className="App-header">

              <h1> React AI Resume Helper </h1>
              <h3> Please upload your resume</h3>

              <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
              <input type="file" onChange={handleChange}/>
              <button onClick={readFile}>Upload</button>

            </div>
            <br></br>
              
              
            {showDisplay && <ReactDiffViewer oldValue={fileContents} newValue={resume.improved} splitView={true} />}
              


          </header>
      </div>
  );
}

export default App;