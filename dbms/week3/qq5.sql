--Problem Statement: Write an SQL statement to find the book titles and the number of copies of the books which has the word 'Database' in their title.
--Database: LIS

select title, count(title) from book_catalogue inner join book_copies using(isbn_no) where isbn_no in (select isbn_no from book_catalogue where title like '%Database%') group by title
