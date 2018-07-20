-- lists all shows in the database without
-- a genre ID
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT OUTER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
