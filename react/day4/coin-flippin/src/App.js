import './App.css';
function tossCoin() {
    return Math.random() > 0.5 ? "heads" : "tails";
}
function App() {
  function fiveHeads() {
    return new Promise( (resolve, reject) => {
        let headsCount = 0;
        let attempts = 0;
        
        const coinflip = ()=> {
          attempts++;
        let result = tossCoin();
        console.log(`${result} was flipped`);
        if(result === "heads") {
            headsCount++;
        } else {
            headsCount = 0;
        }
        
        
        if (headsCount === 5) {
          resolve(`It took ${attempts} tries to flip five "heads"`);
        } else if (attempts > 100) {
          reject(`c bon ${attempts} attempts has been flipped `)
        }
        else {
          coinflip();
        }
      };
      coinflip();
    });
}
fiveHeads()
    .then( res => console.log(res) )
    .catch( err => console.log(err) );
console.log( "When does this run now?" );
  return (
    <div className="App">
      
    </div>
  );
}

export default App;
