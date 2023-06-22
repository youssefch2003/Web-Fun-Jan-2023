import React from 'react'

const PersonCard = ({person,idx}) => {
  return (
    <div>
        {idx}
        -----{person.firstName} {person.lastName} <br />
    __________{person.age}_____ <br />
    ****{person.hairColor}****
    <hr />
    </div>
  )
}

export default PersonCard