-- Занятие 5 (04.10), урок 8: упорядочить, изменить, удалить.
-- Продолжаем в базе kiber. Если SQL Shell перезапускал: \c kiber
-- Каждая команда в одну строку, копировать строку целиком.

-- ===== 1. Таблица самолётов (range — дальность в км) =====

CREATE TABLE aircrafts (aircraft_code CHAR(3) PRIMARY KEY, model TEXT, range INTEGER);
INSERT INTO aircrafts VALUES ('773', 'Boeing 777-300', 11100), ('763', 'Boeing 767-300', 7900), ('SU9', 'Sukhoi SuperJet-100', 3000), ('320', 'Airbus A320-200', 5700), ('321', 'Airbus A321-200', 5600), ('319', 'Airbus A319-100', 6700), ('733', 'Boeing 737-300', 4200), ('CN1', 'Cessna 208 Caravan', 1200), ('CR2', 'Bombardier CRJ-200', 2700);

-- ===== 2. Упорядочить =====

SELECT * FROM aircrafts ORDER BY range;
SELECT * FROM aircrafts ORDER BY range DESC;

-- ===== 3. Изменить: сначала WHERE, потом всё остальное =====

UPDATE aircrafts SET range = 3500 WHERE aircraft_code = 'SU9';
SELECT * FROM aircrafts WHERE aircraft_code = 'SU9';

-- А вот что будет без WHERE (на учениках):
UPDATE students SET gpa = 5.00;
SELECT * FROM students;

-- ===== 4. Удалить самолёты с дальностью больше 10 000 и меньше 3 000 =====
-- Сначала попробуй сам. Смотри на число после DELETE.
