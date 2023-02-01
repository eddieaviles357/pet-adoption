-- from the terminal run:
-- psql < blogly.sql

DROP DATABASE IF EXISTS adoption;

CREATE DATABASE adoption;

\c adoption

CREATE TABLE pets
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age SMALLINT,
    notes TEXT,
    available BOOLEAN DEFAULT true
);

INSERT INTO pets (name,species,photo_url,age,notes)
VALUES
('meow', 'American Wirehair Cat','https://unsplash.com/photos/LEpfefQf4rU', 2, 'Eats banana'),
('pele', 'Abyssinian Cat', 'https://unsplash.com/photos/LEpfefQf4rU', 1, 'Easts too fast'),
('maggie', 'Bengal Cat', 'https://unsplash.com/photos/LEpfefQf4rU', 3, 'Mean to other cats'),
('persia', 'Bombay Cat', 'https://unsplash.com/photos/LEpfefQf4rU', 3, 'Really likes to cuddle');