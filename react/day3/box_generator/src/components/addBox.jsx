import React,{useState} from "react";
import './Boxs.css';


const Boxs = (props) => {
    const [colors,setColor] = useState("");
    const [box,setBox]= useState([]);

const boxAction =(e)=>{
    e.preventDefault();
    console.log(colors);
    setBox([...box,colors])
    console.log(box);
    setColor("");


}
const stylebox =(onecolor)=>{
    return{
        height : "150px",
        width :"150px",
        background : onecolor
    }
   

}


    return (
        <div>
            <form onSubmit={ boxAction }>
            color <input type="text" onChange ={ (e)=> setColor(e.target.value) } value={colors} />
            <button>ADD</button>
            </form>
            <br /><br />
            <div className="container">
            {box.map((onecolor,idx)=>{
                return <div key={idx} style={stylebox(onecolor)} ></div>
            
            })}</div>




        </div>



)
}
export default Boxs