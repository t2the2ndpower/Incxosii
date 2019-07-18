import React, { Component } from "react";
import SubTitle from "../SubTitle";
import Hero from "../Hero";
import SmallImage from "../images/small.png"
import Wrapper from "../Wrapper";

class Add extends Component {

  constructor(props) {
    super(props);
    this.onChangeCourseName = this.onChangeCourseName.bind(this);
    this.onChangeCourseDetails = this.onChangeCourseDetails.bind(this);
    this.onSubmit = this.onSubmit.bind(this);

    this.state = {
      course_name: '',
      course_details: ''
    }
  }
  onChangeCourseName(e) {
    this.setState({
      course_name: e.target.value
    });
  }
  onChangeCourseDetails(e) {
    this.setState({
      course_details: e.target.value
    })
  }

  onSubmit(e) {
    e.preventDefault();
    alert(`The values are ${this.state.course_name}, ${this.state.course_details}`);
    this.setState({
      course_name: '',
      course_details: ''
    })
  }

  render() {
    return (
      <div>
        <Hero backgroundImage={SmallImage}>
          <h1>Incxosi</h1>
          <h2>A one to one coaching platform for those who like to help others</h2>
        </Hero>
        <Wrapper>
          <SubTitle>Add Course Details and Tasks</SubTitle>
          <div style={{ marginTop: 10 }} className="container">
            <form onSubmit={this.onSubmit} >
              <div className="form-group">
                <label>Course Name:  </label>
                <input
                  type="text"
                  className="form-control"
                  value={this.state.course_name}
                  onChange={this.onChangeCourseName}
                />
              </div>

              <div className="form-group">
                <label>Course Details: </label>
                <br></br>
                <textarea className="form-control"
                  value={this.state.course_details}
                  onChange={this.onChangeCourseDetails}
                  rows={2}
                />
              </div>

              <div className="form-group">
                <input type="submit" value="Add Course" className="btn btn-primary" style={{ float: "right", marginBottom: 10 }}
                disabled = {!(this.state.course_name && this.state.course_details)}
                />
              </div>
            </form>
          </div>
        </Wrapper>
      </div>
    );
  }
}

export default Add;





