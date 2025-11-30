import { useState } from "react";
import axios from "axios";
import WeatherCard from "./components/WeatherCard";

function App() {
  const [city, setCity] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const fetchWeather = async () => {
    setError("");
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/weather?city=${city}`);
      setData(res.data);
    } catch (err) {
      setError("Could not fetch weather data.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-blue-100 to-blue-300 text-gray-800">
      <h1 className="text-3xl font-bold mb-4">☀️ Will It Rain on My Parade?</h1>
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter a city"
          className="p-2 rounded border border-gray-400"
        />
        <button
          onClick={fetchWeather}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Check
        </button>
      </div>
      {error && <p className="text-red-600">{error}</p>}
      {data && <WeatherCard data={data} />}
    </div>
  );
}

export default App;