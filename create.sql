-- create.sql

CREATE TABLE Artist (
    artist_id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255)
);

CREATE TABLE Track (
    track_id SERIAL PRIMARY KEY,
    track_name VARCHAR(255),
    artist_count INTEGER,
    artist_id INTEGER REFERENCES Artist(artist_id),
    released_year INTEGER,
    released_month INTEGER,
    released_day INTEGER,
    bpm INTEGER,
    key INTEGER,
    mode INTEGER,
    danceability_percent FLOAT,
    valence_percent FLOAT,
    energy_percent FLOAT,
    acousticness_percent FLOAT,
    instrumentalness_percent FLOAT,
    liveness_percent FLOAT,
    speechiness_percent FLOAT
);

CREATE TABLE Playlist (
    playlist_id SERIAL PRIMARY KEY,
    track_id INTEGER REFERENCES Track(track_id),
    in_spotify_playlists INTEGER,
    in_apple_playlists INTEGER,
    in_deezer_playlists INTEGER
);

CREATE TABLE Charts (
    chart_id SERIAL PRIMARY KEY,
    track_id INTEGER REFERENCES Track(track_id),
    in_spotify_charts INTEGER,
    in_apple_charts INTEGER,
    in_deezer_charts INTEGER,
    in_shazam_charts INTEGER
);

CREATE TABLE Streams (
    stream_id SERIAL PRIMARY KEY,
    track_id INTEGER REFERENCES Track(track_id),
    streams INTEGER
);