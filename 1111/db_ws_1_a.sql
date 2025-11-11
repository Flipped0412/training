CREATE TABLE songs (
  id INTEGER PRIMARY key,
  title TEXT,
  artist TEXT,
  album TEXT,
  genre TEXT,
  duration INTEGER
);

INSERT INTO songs (title, artist, album, genre, duration)
VALUES ('love dive', 'ive', 'lovedive', 'kpop', 181);

INSERT INTO songs (title, artist, album, genre, duration)
VALUES ('love', 'ive', 'lovedive', 'kpop', 181);

INSERT INTO songs (title, artist, album, genre, duration)
VALUES ('dive', 'ive', 'lovedive', 'kpop', 1821);

INSERT INTO songs (title, artist, album, genre, duration)
VALUES ('aaaa', 'ddddd', 'lovedive', 'kpop', 131);

INSERT INTO songs (title, artist, album, genre, duration)
VALUES ('bbbb', 'wwww', 'lovedive', 'kpop', 141);

SELECT * FROM songs;

UPDATE songs
set title = 'like'
WHERE title = 'love';