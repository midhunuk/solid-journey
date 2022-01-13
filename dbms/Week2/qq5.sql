--Problem Statement: Write an SQL statement to find the first names and the last names of faculty  (faculty_fname, faculty_lname) who belong to the department: 'Computer Science'.
--Database: LIS

select faculty_fname, faculty_lname from faculty where department_code = 'CS'
