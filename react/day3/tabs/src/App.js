import './App.css';
import {useState} from 'react';
import Tab1 from './components/tab1';
import Tab2 from './components/tab2';
import Tab3 from './components/tab3';
function App() {
  const [content,setContent]=useState(['','','']);
  const [num,setNum]=useState(1);

  const settab1 = (cnt)=>{
      setContent([cnt,content[1],content[2]])
      console.log(content);

  }
  const settab2 = (cnt)=>{
    setContent([content[0],cnt,content[2]])
    console.log(content);

  }
  const settab3 = (cnt)=>{
    setContent([content[0],content[1],cnt])
    console.log(content);
  }
  const showContent = () =>{
    if (num === 1){
      return <Tab1 settab1={settab1}  content={content}  />
    }
    else if (num === 2){
      return <Tab2 settab2={settab2}  content={content}  /> 
    }else{
      return <Tab3 settab3={settab3}  content={content}  /> 
    }
  }
  return (
    <div className="App">
      <label onClick={()=>setNum(1)}>tab1</label>
      <label onClick={()=>setNum(2)}>tab2</label>
      <label onClick={()=>setNum(3)}>tab3</label>   <br /><br />
      {showContent()}
    </div>


  );
}

export default App;
