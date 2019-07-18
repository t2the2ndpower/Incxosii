import React, { Component } from "react";
import Wrapper from "../Wrapper";
import SubTitle from "../SubTitle";
import Hero from "../Hero";
import SmallImage from "../images/small.png"


class Instructor extends Component {
  // Setting this.state.inst_courses to the inst_courses json array
  state = {
    inst_courses: []
  };

  // Map over this.state.inst_courses and render a CourseCard component for each inst_course object
  render() {
    return (
      <div>
      <Hero backgroundImage={SmallImage}>
          <h1>Incxosi</h1>
          <h2>A one to one coaching platform for those who like to help others</h2>
        </Hero>
      <Wrapper>
        <SubTitle>Course List</SubTitle>
        {/* {this.state.inst_courses.map(inst_courses => (
          <CourseCard
            id={inst_courses.id}
            key={inst_courses.id}
            name={inst_courses.name}
            activeStudents={inst_courses.activeStudents}
          />
        ))} */}
      </Wrapper>
      </div>
    );
  }
}
export default Instructor;





