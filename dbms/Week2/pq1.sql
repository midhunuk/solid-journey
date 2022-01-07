--Problem Statement: Write a SQL statement to find the name of the manager of the team: “All Stars”.
--Database: FLIS

select m.name from teams as t, managers as m where t.team_id = m.team_id and t.name = 'All Stars'
