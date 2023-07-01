import './App.css';
import {useState} from "react";

function App() {
  const [pokemon, setPokemon] = useState([]);
  const fetchpoke = ()=>{
      fetch("https://pokeapi.co/api/v2/pokemon/?offset=1&limit=807")
      .then((response)=>{
        return response.json();
      }).then((jsonres)=>{
        console.log(jsonres);
        setPokemon(jsonres.results);
      })
      .catch((errobj)=>{
        console.log("xxxxxxxxxx errorr",errobj);
      })
  }

  return (
    <div className="App">
     <button onClick={fetchpoke}>FETCH POKEMON </button>
     <ul>
     {pokemon.map((onepok)=>(
        <li key={onepok.id}>{onepok.name}</li>
     ))}
      </ul>
    </div>
  );
}

export default App;
