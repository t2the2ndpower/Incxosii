import React, { Component } from "react";
import Hero from "../Hero";
import StudentCourseCard from "../StudentCourseCard";
import Wrapper from "../Wrapper";
import SmallImage from "../images/small.png"
import SubTitle from "../SubTitle";
import API from "../../utils/API";


class Student extends Component {
  state = {
     student_courses: []
  };

  componentDidMount() {
    this.loadStuCourses();
  }

  loadStuCourses = () => {

    API.getStuCourses()
    .then(res => {
      this.setState({ student_courses: res.data })
    })
    .catch(err => console.log(err));
  };


  render() {
    return (
      <div>
        <Hero backgroundImage={SmallImage}>
          <h1>Incxosi</h1>
          <h2>A one to one coaching platform for those who like to help others</h2>
        </Hero>
        {/* <Container style={{ marginTop: 30 }}> */}
        <Wrapper>
          <SubTitle>My Current Courses</SubTitle>
          {this.state.student_courses && this.state.student_courses.map(student_courses => (
            <StudentCourseCard
              id={student_courses.id}
              key={student_courses.id}
              name={student_courses.name}
              progress={student_courses.progress}
            />
          ))}
        </Wrapper>
      </div>
    );
  }
}

export default Student;
