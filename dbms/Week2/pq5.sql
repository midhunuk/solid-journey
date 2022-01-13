--Problem Statement: Write a SQL statement to display the first name and the last name of students (student_fname,  student_lname) pursuing `PG' courses.
--Database: LIS

select student_fname, student_lname from students where degree = 'MCA'
