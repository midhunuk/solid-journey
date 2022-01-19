--Problem Statement: Write an SQL statement to find student_fname and student_lname of all students who have issued (borrowed) at least one book.
--Database: LIS

select student_fname, student_lname from students inner join members using(roll_no) where member_no in (select member_no from members inner join book_issue using(member_no) where member_class = 'Student' 
