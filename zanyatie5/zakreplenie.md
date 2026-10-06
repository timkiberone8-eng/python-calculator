# Закрепление занятия 5: базы данных

Займёт около получаса: шпаргалка, три ошибки с занятия и пять задач с проверкой.

Объяснения спрятаны под строками «Подробнее»: открывай, если что-то непонятно.

## 0. Вход

{% include psql-vhod.md %}

## 1. Шпаргалка

Всё, что было на занятии. Строки с `--` это пояснения.

```sql
-- создать таблицу: у каждого столбца имя и тип
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name TEXT,
  age INTEGER,
  birthday DATE,
  is_active BOOLEAN
);

-- добавить несколько строк одной командой
INSERT INTO students (name, age, birthday, is_active) VALUES
  ('Anna', 15, '2010-03-15', true),
  ('Petr', 16, '2009-11-02', true),
  ('Olga', 14, '2011-06-20', false);

-- показать всю таблицу
SELECT * FROM students;

-- отбор: AND требует оба условия сразу (Anna, Petr)
SELECT name FROM students WHERE age > 14 AND is_active = true;

-- отбор: OR хватает одного (Olga)
SELECT name FROM students WHERE age < 15 OR is_active = false;

-- сортировка, DESC значит по убыванию
SELECT * FROM students ORDER BY age DESC;

-- добавить столбец в готовую таблицу (grade это класс в школе)
ALTER TABLE students ADD COLUMN grade INTEGER;

-- изменить: сначала думаем про WHERE, иначе изменится каждая строка
UPDATE students SET grade = 9 WHERE name = 'Anna';

-- удалить строки
DELETE FROM students WHERE is_active = false;

-- удалить таблицу целиком
DROP TABLE students;
```

Типы: `SERIAL` номер ставится сам, `TEXT` текст в одинарных кавычках, `INTEGER` целое число, `DATE` дата в виде `'2010-03-15'`, `BOOLEAN` это `true` или `false`.

После каждой команды psql отвечает, что сделал, например `INSERT 0 3`. Смотри на число в ответе: оно первым показывает, что команда сделала не то.

<details markdown="1">
<summary markdown="span">Подробнее: как читать ответ INSERT 0 3</summary>

- `3` значит, что добавлено 3 строки.
- `0` служебное поле. Когда-то там был номер добавленной строки, в новых версиях PostgreSQL всегда 0.
- У `UPDATE` и `DELETE` число одно: `UPDATE 1` значит «изменена 1 строка», `DELETE 2` значит «удалено 2 строки».

</details>

### Приглашение (prompt): что значит `kiber=#`

{% include psql-klavishi.md %}

## 2. Найди ошибку

Такие ошибки случались на занятии. Сначала подумай, что не так, потом открывай ответ. Проверить руками можно, если в базе есть таблица `students`: её создают первые две команды шпаргалки.

**Ошибка 1.** Набрал и нажал Enter, а psql ничего не делает, только приглашение стало `kiber'#`. Enter ещё раз не помогает.

```sql
INSERT INTO students (name, age) VALUES ('Anna, 15);
```

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

После `Anna` нет закрывающей кавычки. Для psql всё, что дальше, включая `, 15);`, это продолжение имени, поэтому команда не кончается.

Выбраться так:

1. Набери одну кавычку `'` и нажми Enter. Кавычка закрылась, приглашение стало `kiber(#`: скобка после `VALUES` открылась раньше кавычки, а закрывающая `)` попала внутрь текста.
2. Набери `\r` и нажми Enter. Недописанная команда сброшена, в базу ничего не ушло, приглашение снова `kiber=#`.

На экране это выглядит так. Слева от `#` пишет psql, справа то, что набрал ты. Строка без `#` это ответ psql:

```
kiber'# '
kiber(# \r
Буфер запроса сброшен (очищен).
kiber=#
```

Дальше набери правильно:

```sql
INSERT INTO students (name, age) VALUES ('Anna', 15);
```

</details>

**Ошибка 2.**

```sql
INSERT INTO students (name, age, birthday, is_active) VALUES ('Petr', 16, '2009-11-02', 3.80, true);
```

```
ОШИБКА:  INSERT содержит больше выражений, чем целевых столбцов
```

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

Столбцов в скобках четыре, а значений пять: `3.80` лишнее. Значения встают в столбцы по порядку, поэтому их должно быть ровно столько же, сколько столбцов. Убери `3.80`, и команда пройдёт.

</details>

**Ошибка 3.**

```sql
INSERT INTO students (name, age) VALUES ('Ivan', 'fifteen');
```

```
ОШИБКА:  неверный синтаксис для типа integer: "fifteen"
```

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

У `age` тип `INTEGER`, а слово превратить в число нельзя. Нужно `15` без кавычек.

Тонкость: база отказывает, только когда значение невозможно превратить в нужный тип. `'15'` в кавычках она сама превратит в число 15, а `15.7` молча округлит до 16, ошибки не будет.

</details>

## 3. Задачи

### Подготовка: таблица игр

Скопируй и выполни две команды, по одной. Кнопка «Копировать» в правом верхнем углу блока:

<div class="copyable" markdown="1">

```sql
CREATE TABLE games (
  title TEXT PRIMARY KEY,
  genre TEXT,
  year INTEGER,
  rating NUMERIC(3,1),
  is_free BOOLEAN
);
```

```sql
INSERT INTO games (title, genre, year, rating, is_free) VALUES
  ('Minecraft',        'sandbox',    2011, 9.0, false),
  ('Roblox',           'sandbox',    2006, 7.5, true),
  ('Terraria',         'sandbox',    2011, 9.0, false),
  ('Brawl Stars',      'shooter',    2018, 8.0, true),
  ('Counter-Strike 2', 'shooter',    2023, 8.5, true),
  ('Dota 2',           'moba',       2013, 8.0, true),
  ('Genshin Impact',   'rpg',        2020, 8.5, true),
  ('Hollow Knight',    'platformer', 2017, 9.5, false);
```

</div>

Столбцы: `title` название, `genre` жанр, `year` год выхода, `rating` оценка из 10 (условная, можешь не соглашаться), `is_free` бесплатная ли игра. `PRIMARY KEY` у названия значит, что двух игр с одним названием в таблице не будет.

Новый тип `NUMERIC(3,1)` это число с дробью: всего 3 цифры, из них 1 после точки. Самое большое такое число `99.9`, как раз для оценки вроде `8.5`.

**Проверь себя:** psql ответил `CREATE TABLE`, потом `INSERT 0 8`. `SELECT * FROM games;` показывает 8 строк.

Если пишет `отношение "games" уже существует`, удали старую таблицу командой `DROP TABLE games;` и начни подготовку заново. Если на второй строке `повторяющееся значение ключа`, значит игры уже вставлены, второй раз не нужно.

Задачи набирай руками, не копируй: так команды запомнятся.

### Задача 1. Бесплатные игры

Выведи названия всех бесплатных игр.

**Проверь себя:** 5 строк.

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

```sql
SELECT title FROM games WHERE is_free = true;
```

</details>

### Задача 2. AND и OR

а) Выведи названия и годы игр, которые вышли раньше 2012 года **и** позже 2020 года. Сколько строк получилось и почему?

б) Замени в той же команде `AND` на `OR`.

**Проверь себя:** а) 0 строк, б) 4 строки.

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

```sql
SELECT title, year FROM games WHERE year < 2012 AND year > 2020;
SELECT title, year FROM games WHERE year < 2012 OR year > 2020;
```

`AND` требует, чтобы у одной и той же игры выполнялись оба условия сразу, а выйти одновременно до 2012 и после 2020 года игра не может. `OR` хватает одного условия: Roblox, Minecraft, Terraria и Counter-Strike 2.

</details>

### Задача 3. От новых к старым

Выведи названия и годы всех игр так, чтобы самые новые были сверху.

**Проверь себя:** первая строка Counter-Strike 2, третья Brawl Stars.

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

```sql
SELECT title, year FROM games ORDER BY year DESC;
```

</details>

### Задача 4. Во что ты играл

Добавь в таблицу столбец `played` с типом `BOOLEAN` и поставь `true` тем играм, в которые играл сам. Потом выведи их названия.

**Проверь себя:** сразу после добавления столбца `SELECT * FROM games;` показывает его пустым у всех игр. Число после `UPDATE` равно количеству игр, которые ты назвал.

- `UPDATE 8` значит, что забыт `WHERE` и отмечены все игры. Верни как было: `UPDATE games SET played = false;` и повтори с `WHERE`.
- `UPDATE 0` значит, что название написано не так, как в таблице. Большие буквы, пробелы и цифры важны: `'minecraft'` и `'Minecraft'` для базы разные слова.

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

Например, для Minecraft и Brawl Stars:

```sql
ALTER TABLE games ADD COLUMN played BOOLEAN;
UPDATE games SET played = true WHERE title = 'Minecraft' OR title = 'Brawl Stars';
SELECT title FROM games WHERE played = true;
```

</details>

### Задача 5. Только бесплатные

Удали из таблицы все платные игры. Перед `DELETE` выполни `SELECT` с тем же условием: так ты увидишь, что удалишь, до того, как удалишь.

**Проверь себя:** `SELECT` показывает 3 игры, `DELETE` отвечает `DELETE 3`, в таблице осталось 5 игр.

<details markdown="1">
<summary markdown="span">Показать ответ</summary>

```sql
SELECT title FROM games WHERE is_free = false;
DELETE FROM games WHERE is_free = false;
SELECT * FROM games;
```

</details>

Захочешь пройти задачи заново: `DROP TABLE games;` и снова подготовка.
