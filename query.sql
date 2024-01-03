-- Query 2a: Sort streams
SELECT Track.track_name, Streams.streams
FROM Track
JOIN Streams ON Track.track_id = Streams.track_id
ORDER BY Streams.streams DESC

-- Query 2b: Percentage of tracks in playlists that are higher than 50 place
SELECT COUNT(Playlist.track_id) AS playlist_count, 'Spotify' AS platform
FROM Playlist
WHERE Playlist.in_spotify_playlists > 50
UNION
SELECT COUNT(Playlist.track_id) AS playlist_count, 'Apple' AS platform
FROM Playlist
WHERE Playlist.in_apple_playlists > 50
UNION
SELECT COUNT(Playlist.track_id) AS playlist_count, 'Deezer' AS platform
FROM Playlist
WHERE Playlist.in_deezer_playlists > 50;

-- Query 2c: Number of tracks in Spotify charts based on energy percentage that are higher than 100 place
SELECT Track.energy_percent, COUNT(Charts.track_id) AS track_count
FROM Track
JOIN Charts ON Track.track_id = Charts.track_id
WHERE Charts.in_spotify_charts < 100
GROUP BY Track.energy_percent;
