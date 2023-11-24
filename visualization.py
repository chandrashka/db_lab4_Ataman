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

import matplotlib.pyplot as plt

# Query 2a Result for Visualization
labels_2a = [row[0] for row in result_2a]
values_2a = [row[1] for row in result_2a]

# Plotting a bar chart for Query 2a
plt.figure(figsize=(8, 5))
plt.bar(labels_2a, values_2a, color='blue')
plt.xlabel('Track Name')
plt.ylabel('Total Streams')
plt.title('Total Streams for Each Track')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig('bar_chart_2a.png')
plt.show()

# Query 2b Result for Visualization
labels_2b = [row[1] for row in result_2b]
values_2b = [row[0] for row in result_2b]

# Plotting a pie chart for Query 2b
plt.figure(figsize=(8, 8))
plt.pie(values_2b, labels=labels_2b, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Percentage of Tracks in Playlists (Spotify, Apple, Deezer)')
plt.savefig('pie_chart_2b.png')
plt.show()

# Query 2c Result for Visualization
labels_2c = [str(row[0]) for row in result_2c]
values_2c = [row[1] for row in result_2c]

# Plotting a bar chart for Query 2c
plt.figure(figsize=(8, 5))
plt.bar(labels_2c, values_2c, color='green')
plt.xlabel('Energy Percent')
plt.ylabel('Number of Tracks in Apple Charts')
plt.title('Number of Tracks in Apple Charts based on Energy Percent')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig('bar_chart_2c.png')
plt.show()
