import React from 'react'

const Tab2= (props) => {

return (
    <textarea name="" id="" cols="30" rows="10" onChange={(e)=>{props.settab2(e.target.value) }} value={props.content[1]}>{props.content[1]}</textarea>
  )
}

export default Tab2;