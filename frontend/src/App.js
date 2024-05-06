import logo from './logo.svg';
import React, { useState, useEffect } from "react";
import './App.css';
import {
  Button,
} from 'react-native';

import TextDiff from './TextDiff';
function App() {
  // usestate for setting a javascript
  // object for storing and using data
  const [data, setdata] = useState({
      name: "",
      age: 0,
      date: "",
      programming: "",
  });
  const [resume, setResume] = useState({
    improved: ""
  })
  const [file, setFile] = useState()
  const [fileContents, setFileContents] = useState()

  const originalFileContent = 'This is the original file content'
  const improvedFileContent = 'This is the improved file content'
  function handleChange(event) {
    setFile(event.target.files[0])
  }
  

  function readFile() {
    const reader = new FileReader()
    console.log(file)
    reader.onload = function(event) {
      // The file's text will be printed here
      setFileContents(event.target.result)
    };
    reader.readAsText(file);
  }


  const improveResume = async (originalResume) => {
    try {
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
              <h1>React and flask</h1>
              {/* Calling a data from setdata for showing */}
              <p>{data.name}</p>
              <p>{data.age}</p>
              <p>{data.date}</p>
              <p>{data.programming}</p>

              <form>
                <h1>React File Upload</h1>
                
              </form>

              <input type="file" onChange={handleChange}/>
              <Button 
              title="Upload"
              color="#841584"
              onPress={readFile}
              />

              <p>File contents:</p>
              <p> {fileContents}</p>
              <TextDiff
                originalFile={originalFileContent}
                improvedFile={improvedFileContent}
              />

          </header>
      </div>
  );
}

export default App;