--Problem Statement: Write an SQL statement to find the colors of the home-jersey and the away-jersey (jersey_home_color, jersey_away_color) used by the team: 'All Stars'.
--Database: FLIS

select jersey_home_color, jersey_away_color from teams where name = 'All Stars'
