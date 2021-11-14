import './App.css';
import HomePage from './Pages/HomePage/Components/HomePage';

function App() {
  return (
    <div>
      <h3 className="h">Hello world</h3>
      <HomePage name = "mansoor"/>
      <HomePage name= "armaan"/>
      <HomePage/>
      <HomePage/>
    </div>
  );
}

export default App;
