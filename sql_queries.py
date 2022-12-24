# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table;"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table
(songplay_id SERIAL PRIMARY KEY,
start_time TIMESTAMP NOT NULL,
user_id INTEGER NOT NULL,
level VARCHAR,
song_id VARCHAR,
artist_id VARCHAR,
session_id INTEGER,
location VARCHAR,
user_agent VARCHAR
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table
(user_id INTEGER PRIMARY KEY,
first_name VARCHAR,
last_name VARCHAR,
gender CHAR(1),
level CHAR(10)
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table
(song_id VARCHAR PRIMARY KEY,
title VARCHAR NOT NULL,
artist_id VARCHAR,
year INTEGER,
duration DECIMAL NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table
(artist_id VARCHAR PRIMARY KEY,
name VARCHAR NOT NULL,
location VARCHAR,
latitude double precision,
longitude double precision
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table
(start_time TIME PRIMARY KEY,
hour SMALLINT,
day SMALLINT,
week SMALLINT,
month SMALLINT,
year SMALLINT,
weekday SMALLINT
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay_table
(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO user_table
(user_id, first_name, last_name, gender, level)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO song_table
(song_id, title, artist_id, year, duration)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artist_table
(artist_id, name, location, latitude, longitude)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time_table
(start_time, hour, day, week, month, year, weekday)
VALUES
(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id
FROM song_table s
LEFT JOIN artist_table a ON s.artist_id = a.artist_id
WHERE s.title = %s
AND a.name = %s
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]