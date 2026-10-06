Всё ниже для Windows. Если у тебя дома Mac или Linux, сначала открой блок «У меня Mac или Linux» {% if include.konspekt %}ниже{% else %}в конце этого раздела{% endif %}.

Открой SQL Shell, нажми Enter четыре раза и введи пароль `postgres` (при вводе его не видно). Потом три команды:

```sql
\! chcp 1251
CREATE DATABASE kiber;
\c kiber
```

Первая чинит русские буквы (почему они ломаются, {% if include.konspekt %}объясняют [слайды с занятия](../urok6/kodirovki.html){% else %}вспомни по [слайдам с занятия](../urok6/kodirovki.html){% endif %}), вторая создаёт базу{% unless include.konspekt %} для задач{% endunless %}, третья подключается к ней. `kiber` это просто имя, можно любое.

Базу создают один раз. В следующий раз сразу `\c kiber`. Если psql пишет `база данных "kiber" уже существует`, значит, она уже есть: переходи к `\c kiber`.

### Основные команды psql

База данных хранит таблицы. Баз может быть много, у каждой свои таблицы. Работать можно только с таблицами той базы, к которой ты подключён: её имя видно в начале строки, например `kiber=#`.

| Что нужно | Команда |
|---|---|
| посмотреть все базы | `\l` |
| подключиться к базе | `\c kiber` |
| вернуться туда, где был сразу после входа | `\c postgres` |
| посмотреть таблицы в текущей базе | `\dt` |
| посмотреть столбцы таблицы и их типы | `\d students` |
| выйти из SQL Shell | `\q` |

<details markdown="1">
<summary markdown="span">Подробнее: можно ли выйти из базы и подключиться к таблице</summary>

Выйти из базы «в никуда» нельзя: psql всегда подключён к какой-то базе. Сразу после входа это база `postgres`, её создал сам PostgreSQL. Поэтому «выйти обратно» значит подключиться к ней: `\c postgres`.

К таблице не подключаются. Таблицу называют прямо в команде: `SELECT * FROM students;`.

В списке `\l` базы `postgres`, `template0` и `template1` служебные, их не трогай. `\d students` покажет и лишнее (например, `nextval(...)` у `id`), смотри на первые два столбца: имя и тип.

</details>

<details markdown="1">
<summary markdown="span">Подробнее: зачем \q, если можно закрыть окно</summary>

В SQL Shell разницы нет: всё, что ты выполнил, уже сохранено в базе, так что окно можно просто закрыть.

`\q` пригодится в Linux и macOS. Там psql запускают в обычном терминале, как `python` в терминале VS Code. `\q` закрывает только psql и возвращает в терминал, а если закрыть окно, закроется весь терминал.

</details>

<details markdown="1">
<summary markdown="span">Дома нет PostgreSQL</summary>

Скачай установщик: [postgresql.org/download/windows](https://www.postgresql.org/download/windows/) → Download the installer → версия 18.6, колонка Windows x86-64. Файл большой, около 400 МБ.

При установке:

| Экран | Что делать |
|---|---|
| Installation Directory, Data Directory | ничего не менять |
| Select Components | снять галочку Stack Builder, остальное оставить |
| Password | `postgres` в оба поля |
| Port | `5432`, не менять |
| Locale | Default locale |
| последний экран | если есть галочка Launch Stack Builder, снять, Finish |

Пароль поставь `postgres`, как в классе. Его спрашивают при каждом входе, а забытый пароль не восстановить: придётся переустанавливать PostgreSQL.

После установки в меню Пуск появится SQL Shell (psql).

</details>

<details markdown="1">
<summary markdown="span">У меня Mac или Linux</summary>

Всё ещё проще: команды SQL те же самые, а `\! chcp 1251` не нужен, русские буквы работают и так. Отличаются только установка, запуск psql и клавиши.

**Linux (Ubuntu).** В терминале:

```
sudo apt install postgresql
sudo -u postgres psql
```

Первая команда ставит PostgreSQL, вторая открывает psql. Один раз задай пароль, как в классе:

```sql
ALTER USER postgres PASSWORD 'postgres';
```

Дальше всё как выше, начиная с `CREATE DATABASE kiber;`. В следующий раз сразу `sudo -u postgres psql`. Ошибки могут быть по-английски, если система на английском.

**Mac.** Скачай установщик: [postgresql.org/download/macosx](https://www.postgresql.org/download/macosx/) → Download the installer → версия 18 для macOS. Экраны те же, что в блоке «Дома нет PostgreSQL», пароль `postgres`. После установки в «Программах», в папке PostgreSQL 18, появится SQL Shell (psql): Enter четыре раза и пароль `postgres`. Шаги для Mac не проверены. Если что-то выглядит иначе, напиши в чат группы.

**Клавиши.** Ctrl+C здесь не закрывает окно, а стирает недописанную команду. Выйти: `\q` или Ctrl+D. Стрелка вверх возвращает команду целиком, даже если она была в несколько строк.

</details>
