import React from "react";
import "./style.css";

function StudentCourseCard(props) {
  return (
    <div className="cardStudent">
      {/* <div className="content" style={{ color: "red" }}> */}
      <div className="content">
        <ul>
          <li>
            <strong>Course:</strong> {props.name}
          </li>
          <li>
            <strong>Progress:</strong> {props.progress} %
          </li>
        </ul>
      </div>
    </div>
  );
}

export default StudentCourseCard;
