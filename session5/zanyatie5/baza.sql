-- Занятие 5 (04.10), базы данных. SQL Shell (psql).
-- Каждая команда в ОДНУ строку: копируешь строку целиком, вставляешь в SQL Shell, Enter.
-- Строки с "--" — пояснения, их не копировать.
-- Вход: SQL Shell, Enter четыре раза, пароль postgres (при вводе не виден).

-- ===== 1. Своя база на всё занятие =====

CREATE DATABASE kiber;
\c kiber

-- ===== 2. Таблица учеников =====

CREATE TABLE students (id SERIAL PRIMARY KEY, name TEXT, age INTEGER, birthday DATE, gpa NUMERIC(3,2), is_active BOOLEAN);
\dt
INSERT INTO students (name, age, birthday, gpa, is_active) VALUES ('Anna', 15, '2010-03-15', 4.50, true), ('Petr', 16, '2009-11-02', 3.80, true), ('Olga', 14, '2011-06-20', 4.90, false);
SELECT * FROM students;
SELECT name, gpa FROM students WHERE gpa > 4;
SELECT name FROM students WHERE is_active = true;

-- ===== 3. Что база НЕ пропустит (у каждого столбца свой тип) =====

INSERT INTO students (name, age) VALUES ('Ivan', 'twenty');
INSERT INTO students (name, birthday) VALUES ('Ivan', '2010-02-30');
INSERT INTO students (name, gpa) VALUES ('Ivan', 10.5);
