-- 16. List shows and genres
-- List all shows and their linked genres from hbtn_0d_tvshows
-- If a show has no genre, display NULL
-- Display columns: tv_shows.title - tv_genres.name
-- Results sorted ascending by show title and genre name
-- Only one SELECT statement allowed

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

