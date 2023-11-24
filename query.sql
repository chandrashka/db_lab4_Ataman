-- Query 2a: Total streams for each track
SELECT Track.track_name, SUM(Streams.streams) AS total_streams
FROM Track
JOIN Streams ON Track.track_id = Streams.track_id
GROUP BY Track.track_name;

-- Query 2b: Percentage of tracks in Spotify playlists
SELECT COUNT(Playlist.track_id) AS playlist_count, 'Spotify' AS platform
FROM Playlist
WHERE Playlist.in_spotify_playlists > 0
UNION
SELECT COUNT(Playlist.track_id) AS playlist_count, 'Apple' AS platform
FROM Playlist
WHERE Playlist.in_apple_playlists > 0
UNION
SELECT COUNT(Playlist.track_id) AS playlist_count, 'Deezer' AS platform
FROM Playlist
WHERE Playlist.in_deezer_playlists > 0;

-- Query 2c: Number of tracks in Apple charts based on energy percentage
SELECT Track.energy_percent, COUNT(Charts.track_id) AS track_count
FROM Track
JOIN Charts ON Track.track_id = Charts.track_id
WHERE Charts.in_apple_charts > 0
GROUP BY Track.energy_percent;
