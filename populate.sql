INSERT INTO Artist (artist_name)
VALUES
('Latto, Jung Kook'),
('Myke Towers'),
('Olivia Rodrigo'),
('Taylor Swift'),
('Bad Bunny');

INSERT INTO Track (track_id, track_name, artist_count, artist_id, released_year, released_month, released_day, bpm, key, mode, danceability_percent, valence_percent, energy_percent, acousticness_percent, instrumentalness_percent, liveness_percent, speechiness_percent)
VALUES
(1, 'Seven (feat. Latto) (Explicit Ver.)', 2, 1, 2023, 7, 14, 125, 4, 2, 0.80, 0.89, 0.83, 0.31, 0, 0.08, 0.04),
(2, 'LALA', 1, 2, 2023, 3, 23, 92, 1, 1, 0.71, 0.61, 0.74, 0.07, 0, 0.10, 0.04),
(3, 'vampire', 1, 3, 2023, 6, 30, 138, 5, 1, 0.51, 0.32, 0.53, 0.17, 0, 0.31, 0.06),
(4, 'Cruel Summer', 1, 4, 2019, 8, 23, 170, 4, 2, 0.55, 0.58, 0.72, 0.11, 0, 0.11, 0.15),
(5, 'WHERE SHE GOES', 1, 5, 2023, 5, 18, 144, 9, 1, 0.65, 0.23, 0.80, 0.14, 63, 0.11, 0.06);

INSERT INTO Playlist (track_id, in_spotify_playlists, in_apple_playlists, in_deezer_playlists)
VALUES
(1, 553, 43, 263),
(2, 1474, 48, 126),
(3, 1397, 94, 207),
(4, 7858, 116, 207),
(5, 3133, 84, 133);

INSERT INTO Charts (track_id, in_spotify_charts, in_apple_charts, in_deezer_charts, in_shazam_charts)
VALUES
(1, 147, 141381703, 45, 10),
(2, 48, 133716286, 58, 14),
(3, 113, 140003974, 91, 14),
(4, 100, 800840817, 125, 12),
(5, 50, 303236322, 87, 15);

INSERT INTO Streams (track_id, streams)
VALUES
(1, 141381703),
(2, 133716286),
(3, 140003974),
(4, 800840817),
(5, 303236322);