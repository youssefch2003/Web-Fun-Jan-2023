import React,{useState} from 'react'

const  FormComp = () => {
    const [firstname,setFirstname] = useState("");
    const [lastname,setLastname] = useState("");
    const [email,setEmail] =useState("");
    const [password,setPassword] = useState("");
    const [confirmpassword,setConfirmpassword] = useState("");
    
    const createUser = (e) => {
        e.preventDefault();

        const newUser = {
            firstname,
            lastname,
            email,
            password,
            confirmpassword
        }
        console.log(newUser);
    }

  return (
    <div>
        <form onSubmit={(e)=>{createUser(e)}}>
          
        <fieldset>
            <legend>form form</legend>
              <div>  
                <label htmlFor="">FirstName:</label>
                <input  onChange={(e)=>{setFirstname(e.target.value)}}/>
            </div>
        <div>  
            <label htmlFor="">LastName:</label>
            <input  onChange={(e)=>{setLastname(e.target.value)}}/>
        </div>
        <div>  
            <label htmlFor="">Email:</label>
            <input onChange={(e)=>{setEmail(e.target.value)}} />
        </div>
        <div>  
            <label htmlFor="">password:</label>
            <input  type='password' onChange={(e)=>{setPassword(e.target.value)}} />
        </div>
        <div>  
            <label htmlFor=""> Confirm password:</label>
            <input type='password' onChange={(e)=>{setConfirmpassword(e.target.value)}} />
        </div>
        <button>adddddd</button>
            </fieldset>

     
        </form>
        firstname:{JSON.stringify(firstname)} <br />
            lastname:{JSON.stringify(lastname)} <br />
            email:{JSON.stringify(email)} <br />
            password:{JSON.stringify(password)} <br />
            confirmpassword:{JSON.stringify(confirmpassword)} <br />
        </div>
  )
}

export default FormComp