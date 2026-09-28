-- Урок 7: типы данных PostgreSQL.
--
-- Конспект, а не скрипт: команды вводятся в SQL Shell (psql) по одной.
-- Как войти и что делать дома с русскими буквами — в начале urok6/test2.sql.
--
-- ЛОВУШКА СЛАЙДОВ: слайды 7–11 про типы написаны для другой базы, MySQL.
-- TINYINT и DATETIME в PostgreSQL нет, база прямо об этом скажет:
--   CREATE TABLE t (a TINYINT);   → ОШИБКА: тип "tinyint" не существует
--   CREATE TABLE t (a DATETIME);  → ОШИБКА: тип "datetime" не существует
-- Типы ниже — из методички, они для PostgreSQL верные.
--
--   INTEGER        целое число              возраст, количество
--   TEXT           строка любой длины       имена, комментарии
--   VARCHAR(n)     строка не длиннее n      логины, коды
--   BOOLEAN        true / false             учится ли ученик
--   DATE           дата                     день рождения
--   TIMESTAMP      дата и время             когда зарегистрировался
--   REAL           дробное, приблизительно  температура
--   NUMERIC(p,s)   дробное, точно           деньги, оценки
--   SERIAL         целое, растёт само       id


-- 1. Повторение урока 6: база, таблица, строка, вывод.

CREATE DATABASE practice;

\c practice

CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO test (name, age) VALUES ('Алексей', 25);

\dt

SELECT * FROM test;


-- 2. Таблица, где у каждого столбца свой тип.

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    gpa NUMERIC(3,2),
    is_active BOOLEAN,
    birthday DATE,
    registered_at TIMESTAMP
);

-- Дата пишется строкой в одинарных кавычках, год-месяц-день.
-- CURRENT_TIMESTAMP — «прямо сейчас», база подставит сама.
INSERT INTO students (name, age, gpa, is_active, birthday, registered_at)
VALUES
    ('Иван', 18, 4.25, true, '2006-09-01', CURRENT_TIMESTAMP),
    ('Оля', 17, 4.75, false, '2007-03-15', CURRENT_TIMESTAMP);

SELECT * FROM students;

-- В выводе true и false выглядят как t и f.


-- 3. Выборка по условию.

SELECT * FROM students WHERE is_active = true;   -- только Иван
SELECT * FROM students WHERE gpa > 4.5;          -- только Оля


-- 4. Что тип не пропустит. Каждая команда ниже нарочно с ошибкой.

-- NUMERIC(3,2): всего три цифры, две после запятой. Максимум 9.99.
INSERT INTO students (name, gpa) VALUES ('Петя', 10.5);
-- ОШИБКА: переполнение поля numeric

-- Лишний знак после запятой не ошибка, база округлит: ляжет 4.26.
INSERT INTO students (name, gpa) VALUES ('Петя', 4.256);

-- Тридцатого февраля не бывает, и база это знает.
INSERT INTO students (name, birthday) VALUES ('Вася', '2007-02-30');
-- ОШИБКА: значение поля типа date/time вне диапазона: "2007-02-30"

-- BOOLEAN по-русски не понимает.
INSERT INTO students (name, is_active) VALUES ('Коля', 'да');
-- ОШИБКА: неверный синтаксис для типа boolean: "да"


-- 5. Почему деньги не в REAL. Десять раз по 10 копеек:

SELECT sum(x) FROM (SELECT 0.1::real AS x FROM generate_series(1, 10)) s;
-- 1.0000001

SELECT sum(x) FROM (SELECT 0.1::numeric(8,2) AS x FROM generate_series(1, 10)) s;
-- 1.00
--
-- REAL хранит число приблизительно. Для температуры это не страшно,
-- для денег — копейки, которые ниоткуда взялись.


-- 6. Удалить строку и таблицу.

DELETE FROM students WHERE name = 'Иван';

DROP TABLE students;

-- Базу practice можно удалить так же, как test2 на уроке 6:
-- \c postgres
-- DROP DATABASE practice;
