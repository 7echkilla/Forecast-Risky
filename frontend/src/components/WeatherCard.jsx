function WeatherCard({ data }) {
  const temp = data?.main?.temp;
  const desc = data?.weather?.[0]?.description;
  const humidity = data?.main?.humidity;
  const city = data?.name;

  return (
    <div className="bg-white p-6 rounded-2xl shadow-lg w-80 text-center">
        <h2 className="text-2xl font-semibold mb-2">{city}</h2>
        <p className="text-lg capitalize">{desc}</p>
        <p className="text-4xl font-bold mt-2">{temp}°C</p>
        <p className="text-sm text-gray-500">Humidity: {humidity}%</p>
    </div>
  );
}

export default WeatherCard;
