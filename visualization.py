import psycopg2
import matplotlib.pyplot as plt

# Connect to PostgreSQL
conn = psycopg2.connect("dbname='spotify' user='ataman' host='localhost' password='postgres'")
cur = conn.cursor()

# Query 2b: Percentage of tracks in playlists that are higher than 50 place
query_2b = """
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
"""
cur.execute(query_2b)
result_2b = cur.fetchall()

# Visualization for Query 2b
labels_2b = [row[1] for row in result_2b]
values_2b = [row[0] for row in result_2b]

plt.figure(figsize=(8, 8))
plt.pie(values_2b, labels=labels_2b, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Percentage of tracks in playlists that are higher than 50 place')
plt.savefig('pie_chart_2b.png')
plt.show()

# Query 2a: Sort streams
query_2a = """
SELECT Track.track_name, Streams.streams
FROM Track
JOIN Streams ON Track.track_id = Streams.track_id
ORDER BY Streams.streams DESC
"""
cur.execute(query_2a)
result_2a = cur.fetchall()

# Visualization for Query 2a
labels_2a = [row[0] for row in result_2a]
values_2a = [row[1] for row in result_2a]

plt.figure(figsize=(10, 6))
plt.barh(labels_2a, values_2a, color='skyblue')
plt.xlabel('Total Streams')
plt.ylabel('Track Name')
plt.title('Total Streams for Each Track (Sorted)')
plt.tight_layout()
plt.savefig('bar_chart_2a.png')
plt.show()



# Query 2c: Number of tracks in Spotify charts based on energy percentage that are higher than 100 place
query_2c = """
SELECT Track.energy_percent, COUNT(Charts.track_id) AS track_count
FROM Track
JOIN Charts ON Track.track_id = Charts.track_id
WHERE Charts.in_spotify_charts < 100
GROUP BY Track.energy_percent;
"""
cur.execute(query_2c)
result_2c = cur.fetchall()

# Visualization for Query 2c
labels_2c = [str(row[0]) for row in result_2c]
values_2c = [row[1] for row in result_2c]

plt.figure(figsize=(10, 6))
plt.bar(labels_2c, values_2c, color='green')
plt.xlabel('Energy Percent')
plt.ylabel('Number of Tracks in Spotify Charts')
plt.title('Number of tracks in Spotify charts based on energy percentage that are higher than 100 place')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig('bar_chart_2c.png')
plt.show()

# Close communication with the database
cur.close()
conn.close()