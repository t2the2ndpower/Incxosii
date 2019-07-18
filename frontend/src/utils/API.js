import axios from "axios";

export default {
    // Gets all instructor courses
    getInstCourses: function () {
        return axios.get("/api/inst");
    },
    // Gets all student courses
    getStuCourses: function () {
        return axios.get("/api/stu");
    },
    // Gets the student courses with the given stu_id
    getStuCourse: function (id) {
        return axios.get("/api/stu/" + id);
    },
    // Deletes the course with the given id
    deleteCourse: function (id) {
        return axios.delete("/api/inst/" + id);
    },
    // Saves a course to the database
    saveCourse: function (courseData) {
        return axios.post("/api/course", courseData);
    }
};
