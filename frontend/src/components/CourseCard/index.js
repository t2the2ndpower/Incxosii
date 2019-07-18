import React from "react";
import "./style.css";

function CourseCard(props) {
  return (
    <div className="cardStudent">
      <div className="content">
        <ul>
          <li>
            <strong>Course:</strong> {props.name}
          </li>
          <li>
            <strong>Active Students:</strong> {props.activeStudents}
          </li>
        </ul>
      </div>
    </div>
  );
}

export default CourseCard;
