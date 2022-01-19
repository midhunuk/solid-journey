--Problem Statement: Write an SQL statement to find the match number of the match held on '2020-05-11' and the name of the main referee who refereed that match. Print match_num first followed by respective main referee name. Note: main referee is to be obtained from the 'referee' attribute.
--Database: FLIS

select match_num, name from match_referees as m inner join referees as r on m.referee = r.referee_id where match_num = (select match_num from matches where match_date = '2020-05-11')
