import React, {Component} from "react";

class PersonCard extends Component {
        constructor(props){
            super(props)
            this.state = {
                person : this.props.person
            }
        }
        increm(){
            this.setState({
                person:{
                ...this.state.person,
                age : this.state.person.age + 1
            } })
        }
        render(){
            const {firstName,lastName,age,hairColor } = this.state.person;
            return <div>
                <div>
                    <h2>{firstName} {lastName}</h2>
                    <p>Age: {age}</p>
                    <p>Hair Color: {hairColor}</p>
                    <button onClick={() => this.increm()}> THIS BUTTON FOR  {firstName} {lastName} AGE</button>
                </div>
            </div>

        }

}
export default PersonCard;