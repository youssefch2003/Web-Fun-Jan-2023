import React from 'react'

const Tab3= (props) => {

return (
    <textarea name="" id="" cols="30" rows="10" onChange={(e)=>{props.settab3(e.target.value) }} value={props.content[2]}>{props.content[2]}</textarea>
)
}

export default Tab3;