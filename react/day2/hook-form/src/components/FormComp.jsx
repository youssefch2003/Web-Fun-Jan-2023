import React,{useState} from 'react'

const  FormComp = () => {
    const [firstname,setFirstname] = useState("");
    const [lastname,setLastname] = useState("");
    const [email,setEmail] =useState("");
    const [password,setPassword] = useState("");
    const [confirmpassword,setConfirmpassword] = useState("");
    const [firstnameerr,setFirstnameerr] = useState("");
    const [lastnameerr,setLastnameerr] = useState("");
    const [emailerr,setEmailerr] =useState("");
    const [passworderr,setPassworderr] = useState("");
    const [confirmpassworderr,setConfirmpassworderr] = useState("");
    const [submitstatus, setSubmitstatus] = useState(false);
    
    const createUser = (e) => {
        e.preventDefault();

        const newUser = {
            firstname,
            lastname,
            email,
            password,
            confirmpassword
        }
        setSubmitstatus(true);

    }


    const validateFirstname = (e) =>{
        setFirstname(e.target.value)

        if(e.target.value.length < 3){
            setFirstnameerr("First Name must be at least 2 characters")
        }else{
            setFirstnameerr("");
        }

    }
    const validateLastname = (e) => {
        setLastname(e.target.value)
        if(e.target.value.length < 3){
            setLastnameerr("Last Name must be at least 2 characters")
        }else{
            setLastnameerr("");
        }
        
    }
    const validateEmail = (e) => {
        setEmail(e.target.value)
        if(e.target.value.length < 5){
            setEmailerr(" the field must be at least 5 characters.")
        }else{
            setEmailerr("");
        }
        
    }
    const validatePassword = (e) => {
        setPassword(e.target.value)
        if(e.target.value.length < 8){
            setPassworderr(" the field must be at least 5 characters.")
        }else{
            setPassworderr("");
        }
        
    }
    const validateConfirmpassword = (e) => {
        setConfirmpassword(e.target.value)
        if((e.target.value.length < 8) && (e.target.value !== password )){
            setConfirmpassworderr(" the field must be at least 5 characters.")
        }else{
            setConfirmpassworderr("");
        }
        
    }


  return (
    <div>
        <form onSubmit={(e)=>{createUser(e)}}>
        {
            submitstatus ? 
            <h3>form submited</h3> :
            <h3>Welcome</h3> 
            }
          
        <fieldset>
            <legend>form form</legend>
              <div>  
                <label htmlFor="">FirstName:</label>
                <input onChange= {validateFirstname}/>
                {
                    firstnameerr ?
                    <p style={{color:'red'}}>{ firstnameerr }</p> :
                    null
                }
            </div>
            <div>  
            <label htmlFor="">LastName:</label>
            <input  onChange={validateLastname}/>
            {
                    lastnameerr ?
                    <p style={{color:"red"}}>{ lastnameerr }</p> :
                    ''
                }
        </div>
        <div>  
            <label htmlFor="">Email:</label>
            <input onChange={validateEmail} />
            {
                    emailerr ?
                    <p style={{color:"red"}}>{ emailerr }</p> :
                    null
                    
            }
        </div>
        <div>  
            <label htmlFor="">password:</label>
            <input  type='password' onChange={validatePassword} />
            {
                    passworderr ?
                    <p style={{color:"red"}}>{ passworderr }</p> :
                    null
                    
            }
        </div>
        <div>  
            <label htmlFor=""> Confirm password:</label>
            <input type='password' onChange={validateConfirmpassword} />
            {
                    confirmpassworderr ?
                    <p style={{color:"red"}}>{ confirmpassworderr }</p> :
                    null
                    
            }
        </div>
        <button>adddddd</button>
            </fieldset>

     
        </form>
        </div>
  )
}

export default FormComp