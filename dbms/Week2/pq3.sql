--Problem Statement: Write an SQL statement to find the titles of books authored by an author having first name as 'Joh Paul' and last name as 'Mueller'.
--Database: LIS

select distinct b.title from book_catalogue as b, book_authors as a where b.ISBN_no = a.ISBN_no and a.author_fname = 'Joh Paul' and a.author_lname = 'Mueller'
