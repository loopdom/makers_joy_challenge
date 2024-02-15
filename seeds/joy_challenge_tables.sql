DROP TABLE IF EXISTS quotes;
DROP SEQUENCE IF EXISTS quotes_id_seq;
DROP TABLE IF EXISTS songs;
DROP SEQUENCE IF EXISTS songs_id_seq;

CREATE SEQUENCE IF NOT EXISTS songs_id_seq;
CREATE TABLE songs (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  link text,
  mood text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS quotes_id_seq;
CREATE TABLE quotes (
  id SERIAL PRIMARY KEY,
  content text,
  author text,
  mood text
);

-- Seed the table with data 
-- songs first

INSERT INTO songs
(name, description, link, mood)
values('Belfast', 'something classic', 'https://www.youtube.com/watch?v=d5vGjCoQM1s', 'reflective');
INSERT INTO songs
(name, description, link, mood)
values('Why', 'something banging', 'https://www.youtube.com/watch?v=BmTj8zkDBbM', 'bitter');
INSERT INTO songs
(name, description, link, mood)
values('Alien Observer', 'something from space', 'https://www.youtube.com/watch?v=eVqFnuaW4JQ', 'reflective');

-- quotes second

INSERT INTO quotes
(content, author, mood)
values('All that you touch You Change. All that you Change Changes you. The only lasting truth Is Change.', 'Octavia Butler', 'reflective');

INSERT INTO quotes
(content, author, mood)
values('The child in each of us Knows paradise.Paradise is home. Home as it was Or home as it should have been. Paradise is one`s own place, One`s own people, One`s own world, Knowing and known, Perhaps even Loving and loved. Yet every child Is cast from paradise- Into growth and new community, Into vast, ongoing Change.', 'Octavia Butler' , 'reflective');

INSERT INTO quotes
(content, author, mood)
values('Kindness eases change. Love quiets fear. And a sweet and powerful Positive obsession Blunts pain, Diverts rage, And engages each of us In the greatest, The most intense Of our chosen struggles', 'Octavia Butler', 'reflective');

INSERT INTO quotes
(content, author, mood)
values('Hell is other people', 'J Paul Sarte','bitter');

INSERT INTO quotes
(content, author, mood)
values('So it`s true when all is said and done, grief is the price we pay for love ', 'E.A Bucchianeri','sad');


