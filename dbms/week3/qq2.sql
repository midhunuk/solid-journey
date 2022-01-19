--Problem Statement: Write an SQL statement to find the name of the youngest player in the team named 'All Stars'.
--Database: FLIS

select name from players where dob = (select max(p.dob) from teams as t inner join players as p using (team_id) where t.name = 'All Stars')
