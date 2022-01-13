--Problem Statement: Write an SQL statement to find the match numbers of those matches in which the host team scored more (goals) than the guest team.
--Database: FLIS


select match_num from matches where host_team_score > guest_team_score
