-- Урок 8: изменить, удалить, упорядочить. Таблица самолётов со слайдов.
--
-- Конспект, а не скрипт: команды вводятся в SQL Shell (psql) по одной.
-- Как войти и что делать дома с русскими буквами — в начале session4/urok6/test2.sql.
--
-- Самостоятельное задание на слайде 19 работает с таблицей aircrafts,
-- но сама таблица в уроке не создаётся. Здесь она есть: скопируй
-- CREATE TABLE и INSERT в psql, дальше по заданиям.


CREATE DATABASE air;

\c air

CREATE TABLE aircrafts (
    aircraft_code CHAR(3) PRIMARY KEY,
    model TEXT,
    range INTEGER
);

-- range — дальность полёта в километрах.
INSERT INTO aircrafts (aircraft_code, model, range) VALUES
    ('773', 'Boeing 777-300', 11100),
    ('763', 'Boeing 767-300', 7900),
    ('SU9', 'Sukhoi SuperJet-100', 3000),
    ('320', 'Airbus A320-200', 5700),
    ('321', 'Airbus A321-200', 5600),
    ('319', 'Airbus A319-100', 6700),
    ('733', 'Boeing 737-300', 4200),
    ('CN1', 'Cessna 208 Caravan', 1200),
    ('CR2', 'Bombardier CRJ-200', 2700);


-- 1. Столбцы в своём порядке, строки по алфавиту модели.

SELECT model, aircraft_code, range FROM aircrafts ORDER BY model;

-- По убыванию: ORDER BY range DESC


-- 2. Не все строки, а по условию: дальность от 4 до 6 тысяч км.

SELECT model, aircraft_code, range FROM aircrafts
WHERE range >= 4000 AND range <= 6000;
-- Airbus A320-200, Airbus A321-200, Boeing 737-300


-- 3. UPDATE без WHERE меняет ВСЕ строки. Показать на чужой таблице,
-- не на этой: ответ psql будет UPDATE 9, у всех самолётов одна дальность.
-- Обратно не отменить. Сначала пиши WHERE, потом всё остальное.


-- Самостоятельное задание (слайд 19)

-- а) У самолёта SU9 дальность 3500. Вывести изменённую строку.
UPDATE aircrafts SET range = 3500 WHERE aircraft_code = 'SU9';
SELECT * FROM aircrafts WHERE aircraft_code = 'SU9';
-- UPDATE 1 — psql пишет, сколько строк изменилось. Полезно смотреть.

-- б) Удалить самолёт CN1.
DELETE FROM aircrafts WHERE aircraft_code = 'CN1';

-- в) Удалить самолёты с дальностью больше 10 000 и меньше 3 000 км.
--
-- По-русски тут «и», а в SQL нужно OR. Самолёта, у которого дальность
-- одновременно больше 10 000 и меньше 3 000, не бывает:
--   ... WHERE range > 10000 AND range < 3000;   → DELETE 0, ничего не удалено
DELETE FROM aircrafts WHERE range > 10000 OR range < 3000;
-- DELETE 2: Boeing 777-300 и Bombardier CRJ-200
-- (Cessna уже удалена в пункте б)

SELECT * FROM aircrafts ORDER BY range;
-- Осталось шесть, от SU9 (3500) до Boeing 767-300 (7900).
