import React from "react";
import { Link } from "react-router-dom";
import "./style.css";

// Depending on the current path, this component sets the "active" class on the appropriate navigation link item
function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <Link className='navbar-brand {
                window.location.pathname === "/Home" || window.location.pathname === "/"
                  ? "nav-link active"
                  : "nav-link"
              }' to="/">
        Incxosi
      </Link>
      <div>
        <ul className="navbar-nav">
          {/* <li className="nav-item">
            <Link 
              to="/"
              className={
                window.location.pathname === "/Home" || window.location.pathname === "/"
                  ? "nav-link active"
                  : "nav-link"
              }
            >
              Home
            </Link>
          </li> */}
          <li className="nav-item">
            <Link
              to="/Student"
              className={window.location.pathname === "/Student" ? "nav-link active" : "nav-link"}
            >
              Student
            </Link>
          </li>
          <li className="nav-item">
            <Link
              to="/Instructor"
              className={window.location.pathname === "/Instructor" ? "nav-link active" : "nav-link"}
            >
              Instructor
            </Link>
          </li>
          <li className="nav-item">
            <Link
              to="/Add"
              className={window.location.pathname === "/Add" ? "nav-link active" : "nav-link"}
            >
              Add
            </Link>
          </li>

        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
