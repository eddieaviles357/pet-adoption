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
('meow', 'cat','https://images.unsplash.com/photo-1519052537078-e6302a4968d4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80', 2, 'Eats banana', true),
('pele', 'cat', 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1686&q=80', 1, 'Easts too fast', true),
('maggie', 'cat', 'https://images.unsplash.com/photo-1589883661923-6476cb0ae9f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80', 3, 'Good to cats', false),
('maggie', 'cat', 'https://images.unsplash.com/photo-1583795128727-6ec3642408f8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1514&q=80', 2, 'Mean to other cats', true),
('persia', 'cat', 'https://images.unsplash.com/photo-1557246565-8a3d3ab5d7f6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80', 3, 'Really likes to cuddle', false);