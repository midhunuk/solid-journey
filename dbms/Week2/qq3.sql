--Problem Statement: Write an SQL statement to find the names of players of the team: “All Stars”.
--Database: FLIS

select p.name from teams as t, players as p where t.team_id = p.team_id and t.name = 'All Stars'
