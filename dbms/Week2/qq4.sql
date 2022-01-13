--Problem Statement: Write an SQL statement to find the first names and the last names (student_fname, student_lname) of  students who belong to the department with department code as 'MCA' and who were born after '2002-06-15'.
--Database: LIS

select student_fname, student_lname from students where department_code = 'MCA' and dob > '2002-06-15'
