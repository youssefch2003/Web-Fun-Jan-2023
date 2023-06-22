import logo from './logo.svg';
import './App.css';
import PersonCard from './components/PersonCard';
function App() {
  const person = [
    {
      firstName : "John",
        lastName:"Doe",
        age:30,
        hairColor:"Brown"
    },
    {
      firstName:"Jane",
      lastName:"Smith",
      age:25,
      hairColor:"Blonde"
    },
    { firstName:"Michael",
    lastName:"Johnson",
    age:40,
    hairColor:"Black"
    },
    {
      firstName:"Emily",
      lastName:"Davis",
      age:35,
      hairColor:"Red"
    }
  ]
  return (
    <div className="App">
      {person.map((person,idx)=> (
        <PersonCard key={idx} person = {person}/>
      ))}
      
    </div>
  );
}
export default App;
