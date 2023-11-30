import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('❌');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api')
      .then((response) => {
        setMessage(response.data.message);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>Historian</h1>
      <h3>Connected to Backend: {loading ? '🔄 ' : message}</h3>
    </div>
  );
}

export default App;
