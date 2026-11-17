# Проектирование базы данных (ER-диаграмма)

## 1. Основные сущности
В системе используются три основные таблицы:

### 1.1. User (Пользователи) — уже реализована тимлидом
- id (Primary Key, Integer) — уникальный идентификатор.
- email (String, Unique) — электронная почта (логин).
- hashed_password (String) — хэш пароля.
- created_at (DateTime) — дата регистрации.

### 1.2. Category (Категории)
- id (Primary Key, Integer) — уникальный идентификатор.
- name (String) — название категории (например, "Работа", "Учеба").
- user_id (Foreign Key to User.id) — владелец категории.
- created_at (DateTime) — дата создания.

### 1.3. Task (Задачи)
- id (Primary Key, Integer) — уникальный идентификатор.
- title (String) — заголовок задачи.
- description (Text, Nullable) — подробное описание.
- status (Boolean) — статус (True = выполнено, False = не выполнено). По умолчанию False.
- due_date (DateTime, Nullable) — дедлайн (срок выполнения).
- user_id (Foreign Key to User.id) — владелец задачи.
- category_id (Foreign Key to Category.id, Nullable) — категория задачи (может быть пустой).
- created_at (DateTime) — дата создания.
- updated_at (DateTime) — дата последнего обновления.

## 2. Связи между таблицами
- User 1 — N Category: У одного пользователя может быть много категорий.
- User 1 — N Task: У одного пользователя может быть много задач.
- Category 1 — N Task: В одной категории может быть много задач. При удалении категории задачи не удаляются (связь обнуляется).
