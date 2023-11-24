CREATE TABLE Track (
    track_id SERIAL PRIMARY KEY,
    track_name VARCHAR(255),
    artist_id INT REFERENCES Artist(artist_id),
    artist_count INT,
    released_year INT,
    released_month INT,
    released_day INT,
    bpm INT,
    key VARCHAR(255),
    mode INT,
    danceability_percent FLOAT,
    valence_percent FLOAT,
    energy_percent FLOAT,
    acousticness_percent FLOAT,
    instrumentalness_percent FLOAT,
    liveness_percent FLOAT,
    speechiness_percent FLOAT
);

CREATE TABLE Artist (
    artist_id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255)
);

CREATE TABLE Playlist (
    playlist_id SERIAL PRIMARY KEY,
    track_id INT REFERENCES Track(track_id),
    in_spotify_playlists INT,
    in_apple_playlists INT,
    in_deezer_playlists INT
);

CREATE TABLE Charts (
    charts_id SERIAL PRIMARY KEY,
    track_id INT REFERENCES Track(track_id),
    in_spotify_charts INT,
    in_apple_charts INT,
    in_deezer_charts INT,
    in_shazam_charts INT
);

CREATE TABLE Streams (
    streams_id SERIAL PRIMARY KEY,
    track_id INT REFERENCES Track(track_id),
    streams INT
);