import React,{useState} from 'react'
import './todo.css';


function Todo() {
    const [list, setList] = useState([
        'get yellow belt',
        'get python belt'
    ]);
    const [islinelist, setIslinelist] = useState(Array(list.length).fill(false));
    const [item, setItem] = useState("");
    const handelCheckbox =(index)=>{
        const updatedlist = [...islinelist];
        updatedlist[index]= !updatedlist[index];
        console.log(updatedlist[index]);
        setIslinelist(updatedlist)
    }
    const handelform= (e)=>{
        e.preventDefault();
        const newlist = [...list,item];
        setItem("");
        setList(newlist);
        console.log(newlist);
        console.log(islinelist);
        
    }
    const handelremove =(index)=>{
        const deletelist= [...list];
        console.log(islinelist);
        console.log(deletelist);
        if (islinelist[index]===true){
            deletelist.splice(index,1);
            islinelist.splice(index,1);
            console.log(deletelist);
            console.log(islinelist,'akakakakakak');
            setList(deletelist);
        
        }
    }
return (
    <div>
        <h1>TODO LIST </h1>
        <form onSubmit={handelform}>
            <input type="text" onChange={(e)=>{setItem(e.target.value)}}/>
            <input className="btn0" type="submit" value="ADD" />
        </form>
        { list.map((oneitem,idx)=>  
            <div className='sss' key={idx}>
                <p style={{ textDecoration: islinelist[idx] ? 'line-through' : 'none' }}>{oneitem}</p>
                <input type="checkbox" checked={islinelist[idx]} onChange={()=>{handelCheckbox(idx)}} />
                <button className="btn" onClick={()=>handelremove(idx)}>delete</button>  
            </div>   
            
            )}
    </div>

)
}

export default Todo