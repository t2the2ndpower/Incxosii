import React from 'react';
import ReactDOM from 'react-dom';

class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      age: null,
      errormessage: '',
      description: ""
    };
  }
  myChangeHandler = (event) => {
    let nam = event.target.name;
    let val = event.target.value;
    let err = '';
    if (nam === "age") {
      if (val !=="" && !Number(val)) {
        err = <strong>Your age must be a number</strong>;
      }
    }
    this.setState({errormessage: err});
    this.setState({[nam]: val});
  }
  render() {
    return (
      <form>
      {/* <h1>Hello {this.state.username} {this.state.age}</h1> */}
      <p>Enter The Course Name:</p>
      <input
        type='text'
        name='coursename'
        onChange={this.myChangeHandler}
      />
      <br/><br/>
      <textarea value={this.state.description} />
      </form>
    );
  }
}

export default MyForm;