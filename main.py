import psycopg2

# Connect to PostgreSQL
conn = conn = psycopg2.connect("dbname='spotify' user='Ataman' host='localhost' password='postgres'")

# Create a cursor
cur = conn.cursor()

# Query 2a
query_2a = """
SELECT Track.track_name, SUM(Streams.streams) AS total_streams
FROM Track
JOIN Streams ON Track.track_id = Streams.track_id
GROUP BY Track.track_name;
"""
cur.execute(query_2a)
result_2a = cur.fetchall()
print("Query 2a Result:")
for row in result_2a:
    print(row)

# Query 2b
query_2b = """
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
"""
cur.execute(query_2b)
result_2b = cur.fetchall()
print("\nQuery 2b Result:")
for row in result_2b:
    print(row)

# Query 2c
query_2c = """
SELECT Track.energy_percent, COUNT(Charts.track_id) AS track_count
FROM Track
JOIN Charts ON Track.track_id = Charts.track_id
WHERE Charts.in_apple_charts > 0
GROUP BY Track.energy_percent;
"""
cur.execute(query_2c)
result_2c = cur.fetchall()
print("\nQuery 2c Result:")
for row in result_2c:
    print(row)

# Close communication with the database
cur.close()
conn.close()