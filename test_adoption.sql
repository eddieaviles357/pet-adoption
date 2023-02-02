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

INSERT INTO pets (name,species,photo_url,age,notes, available)
VALUES
('meow', 'cat','https://unsplash.com/photos/LEpfefQf4rU', 2, 'Eats banana', true),
('pele', 'cat', 'https://unsplash.com/photos/LEpfefQf4rU', 1, 'Easts too fast', true),
('maggie', 'cat', 'https://unsplash.com/photos/LEpfefQf4rU', 3, 'Good to cats', false),
('maggie', 'cat', 'https://unsplash.com/photos/LEpfefQf4rU', 2, 'Mean to other cats', true),
('persia', 'cat', 'https://unsplash.com/photos/LEpfefQf4rU', 3, 'Really likes to cuddle', false);