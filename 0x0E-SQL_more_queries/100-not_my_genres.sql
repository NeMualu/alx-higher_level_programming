-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT DISTINCT g.name
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS s ON g.id = s.genre_id
LEFT JOIN tv_shows AS t ON s.show_id = t.id
WHERE t.title IS NULL OR t.title != 'Dexter'
ORDER BY g.name;

