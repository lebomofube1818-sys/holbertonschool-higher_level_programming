-- 12. No genre
-- List all shows that do not have a genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results sorted by tv_shows.title and tv_show_genres.genre_id
-- Shows without genres should display NULL
-- You can use only one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

