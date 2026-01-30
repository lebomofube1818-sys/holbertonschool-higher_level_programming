-- 13. Number of shows by genre
-- List all genres and the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- Column names: genre, number_of_shows
-- Don't display genres with zero shows
-- Results sorted by number_of_shows in descending order
-- Only one SELECT statement allowed

SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

