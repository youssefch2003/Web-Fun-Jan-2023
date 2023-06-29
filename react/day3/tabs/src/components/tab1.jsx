import React from 'react'

const Tab1= (props) => {

return (
    <textarea name="" id="" cols="30" rows="10" onChange={(e)=>{props.settab1(e.target.value) }} value={props.content[0]}>{props.content[0]}</textarea>
)
}

export default Tab1;